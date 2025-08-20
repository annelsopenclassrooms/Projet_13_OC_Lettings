from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_copy_data'),
    ]

    operations = [
        migrations.RunSQL("DROP TABLE IF EXISTS oc_lettings_site_profile;"),
    ]
