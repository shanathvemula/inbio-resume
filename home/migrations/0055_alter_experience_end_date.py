# Generated by Django 5.0.1 on 2024-02-06 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0054_alter_experience_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
