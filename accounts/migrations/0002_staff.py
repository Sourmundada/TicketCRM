# Generated by Django 3.1.4 on 2021-05-16 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.account')),
            ],
            options={
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staff',
            },
            bases=('accounts.account',),
        ),
    ]
