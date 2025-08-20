from django.db import migrations

def forwards(apps, schema_editor):
    # Modèles "historiques" (figés) au moment de la migration
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    # OldAddress = apps.get_model('oc_lettings_site', 'Address')  # pas indispensable en direct
    Letting = apps.get_model('lettings', 'Letting')
    Address = apps.get_model('lettings', 'Address')

    # On repart d’une table neuve -> on recrée une Address pour chaque Letting
    for old in OldLetting.objects.select_related('address').all():
        old_addr = old.address
        addr = Address.objects.create(
            number=old_addr.number,
            street=old_addr.street,
            city=old_addr.city,
            state=old_addr.state,
            zip_code=old_addr.zip_code,
            country_iso_code=old_addr.country_iso_code,
        )
        Letting.objects.create(
            title=old.title,
            address=addr,
        )

def backwards(apps, schema_editor):
    # Si on annule la migration, on supprime tout ce qu’on a importé
    Letting = apps.get_model('lettings', 'Letting')
    Address = apps.get_model('lettings', 'Address')
    Letting.objects.all().delete()
    Address.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
        #('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
