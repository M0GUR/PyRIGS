# Generated by Django 2.0.13 on 2019-12-06 21:24

from django.db import migrations, models, transaction
import re

def forwards(apps, schema_editor):
    AssetModel = apps.get_model('assets', 'Asset')
    with transaction.atomic():
        for row in AssetModel.objects.all():

            row.asset_id = row.asset_id.upper()
            asset_search = re.search("^([A-Z0-9]*?[A-Z]?)([0-9]+)$", row.asset_id)
            if asset_search is None: # If the asset_id doesn't have a number at the end
                row.asset_id += "1"
            
            asset_search = re.search("^([A-Z0-9]*?[A-Z]?)([0-9]+)$", row.asset_id)
            row.asset_id_prefix = asset_search.group(1)
            row.asset_id_number = int(asset_search.group(2))

            row.save(update_fields=['asset_id', 'asset_id_prefix', 'asset_id_number'])
class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_auto_20190108_0202_squashed_0014_auto_20191017_2052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asset',
            options={'ordering': ['asset_id_prefix', 'asset_id_number'], 'permissions': (('asset_finance', 'Can see financial data for assets'), ('view_asset', 'Can view an asset'))},
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_id_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_id_prefix',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_id',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.RunPython(
            code=forwards,
            reverse_code=migrations.operations.special.RunPython.noop,
        ),
    ]