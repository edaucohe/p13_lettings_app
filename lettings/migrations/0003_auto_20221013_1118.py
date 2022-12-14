# Generated by Django 3.0 on 2022-10-13 09:18
from django.apps import apps as global_apps
from django.db import migrations


def forwards(apps, schema_editor):
    try:
        old_letting_model = apps.get_model('oc_lettings_site', 'Letting')
    except LookupError:
        # The old app isn't installed.
        return

    new_address_model = apps.get_model('lettings', 'Address')
    new_letting_model = apps.get_model('lettings', 'Letting')
    objs = [
        new_letting_model(
            title=old_letting_instance.title,
            address=new_address_model(pk=old_letting_instance.address.pk),
        ) for old_letting_instance in old_letting_model.objects.all()
    ]
    new_letting_model.objects.bulk_create(objs=objs)


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0002_auto_20221013_1037'),
        ('oc_lettings_site', '0002_auto_20221012_1745'),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]

    if global_apps.is_installed('oc_lettings_site'):
        dependencies.append(('oc_lettings_site', '0002_auto_20221012_1745'))
