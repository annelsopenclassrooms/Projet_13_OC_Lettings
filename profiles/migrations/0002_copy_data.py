from django.conf import settings
from django.db import migrations

def forwards(apps, schema_editor):
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    Profile = apps.get_model('profiles', 'Profile')

    # Récupère le modèle User swappable (ex: 'auth.User')
    app_label, model_name = settings.AUTH_USER_MODEL.split('.')
    User = apps.get_model(app_label, model_name)

    for old in OldProfile.objects.all():
        # Associe par ID pour être robuste
        try:
            user = User.objects.get(pk=old.user_id)
        except User.DoesNotExist:
            continue

        # Évite l’erreur d’unicité si un profile existe déjà
        Profile.objects.update_or_create(
            user=user,
            defaults={'favorite_city': old.favorite_city or ''},
        )

def backwards(apps, schema_editor):
    Profile = apps.get_model('profiles', 'Profile')
    Profile.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        #('oc_lettings_site', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
