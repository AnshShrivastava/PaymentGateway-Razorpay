# Generated by Django 3.0.5 on 2020-04-16 17:24

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_auto_20200416_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='razorpayresponse',
            name='response',
            field=jsonfield.fields.JSONField(),
        ),
    ]
