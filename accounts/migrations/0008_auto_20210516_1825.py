# Generated by Django 3.1.4 on 2021-05-16 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210516_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assigned_to',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.PROTECT, to='accounts.staff'),
        ),
    ]
