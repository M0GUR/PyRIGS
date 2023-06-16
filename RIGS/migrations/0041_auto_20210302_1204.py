# Generated by Django 3.1.7 on 2021-03-02 12:04

import RIGS.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RIGS', '0040_auto_20210302_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='meet_info',
        ),
        migrations.RemoveField(
            model_name='event',
            name='payment_method',
        ),
        migrations.RemoveField(
            model_name='event',
            name='payment_received',
        ),
        migrations.AddField(
            model_name='profile',
            name='dark_theme',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='auth_request_to',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='event',
            name='collector',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='collected by'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='purchase_order',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='PO'),
        ),
        migrations.AlterField(
            model_name='eventauthorisation',
            name='account_code',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='eventauthorisation',
            name='uni_id',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='University ID'),
        ),
        migrations.AlterField(
            model_name='eventchecklist',
            name='extinguishers_location',
            field=models.CharField(blank=True, default='', help_text='Location of fire extinguishers', max_length=255),
        ),
        migrations.AlterField(
            model_name='eventchecklist',
            name='hs_location',
            field=models.CharField(blank=True, default='', help_text='Location of Safety Bag/Box', max_length=255),
        ),
        migrations.AlterField(
            model_name='eventchecklist',
            name='w1_description',
            field=models.CharField(blank=True, default='', help_text='Description', max_length=255),
        ),
        migrations.AlterField(
            model_name='eventchecklist',
            name='w2_description',
            field=models.CharField(blank=True, default='', help_text='Description', max_length=255),
        ),
        migrations.AlterField(
            model_name='eventchecklist',
            name='w3_description',
            field=models.CharField(blank=True, default='', help_text='Description', max_length=255),
        ),
        migrations.AlterField(
            model_name='eventitem',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='address',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='payment',
            name='method',
            field=models.CharField(blank=True, choices=[('C', 'Cash'), ('I', 'Internal'), ('E', 'External'), ('SU', 'SU Core'), ('T', 'TEC Adjustment')], default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='person',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='api_key',
            field=models.CharField(blank=True, default='', editable=False, max_length=40),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=13),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='general_notes',
            field=models.TextField(blank=True, default='', help_text='Did you have to consult a supervisor about any of the above? If so who did you consult and what was the outcome?'),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='persons_responsible_structures',
            field=models.TextField(blank=True, default='', help_text='Who are the persons on site responsible for their use?'),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='power_notes',
            field=models.TextField(blank=True, default='', help_text='Did you have to consult a supervisor about any of the above? If so who did you consult and what was the outcome?'),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='power_plan',
            field=models.URLField(blank=True, default='', help_text="Upload your power plan to the <a href='https://nottinghamtec.sharepoint.com/'>Sharepoint</a> and submit a link", validators=[RIGS.models.validate_url]),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='rigging_plan',
            field=models.URLField(blank=True, default='', help_text="Upload your rigging plan to the <a href='https://nottinghamtec.sharepoint.com/'>Sharepoint</a> and submit a link", validators=[RIGS.models.validate_url]),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='sound_notes',
            field=models.TextField(blank=True, default='', help_text='Did you have to consult a supervisor about any of the above? If so who did you consult and what was the outcome?'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='address',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='venue',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='venue',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='venue',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]
