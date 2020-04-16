# Generated by Django 3.0.5 on 2020-04-15 17:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment', '0003_delete_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetail',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='payment.Base')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=150)),
                ('PayType', models.IntegerField(choices=[(2, 'Full_Payment'), (1, 'Partial_Sattlement'), (0, 'Advance_Pay')], default='Full_Payment')),
                ('amount', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=250)),
            ],
            bases=('payment.base',),
        ),
        migrations.CreateModel(
            name='RazorpayResponsew',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='payment.Base')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('response', models.TextField()),
                ('status', models.CharField(choices=[(2, 'Success'), (1, 'Pending'), (0, 'Failed')], max_length=2)),
                ('relation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='payment.PaymentDetail')),
            ],
            bases=('payment.base',),
        ),
    ]
