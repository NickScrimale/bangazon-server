# Generated by Django 4.1.5 on 2023-01-21 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bangazonapi', '0003_paymenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost', models.FloatField()),
                ('date_created', models.DateField()),
                ('completed', models.BooleanField()),
                ('quantity', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazonapi.user')),
            ],
        ),
    ]
