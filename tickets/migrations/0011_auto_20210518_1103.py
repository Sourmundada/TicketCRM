# Generated by Django 3.1.4 on 2021-05-18 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0010_auto_20210517_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Ongoing', 'Ongoing'), ('Completed', 'Completed'), ('Archived', 'Archived')], default='Draft', max_length=100),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
