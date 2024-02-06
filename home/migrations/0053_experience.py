# Generated by Django 5.0.1 on 2024-02-06 03:43

import django.db.models.deletion
import modelcluster.fields
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0052_alter_professional_how_much_percentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('company_name', wagtail.fields.RichTextField()),
                ('designation', wagtail.fields.RichTextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('responsibilities', wagtail.fields.RichTextField()),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='home.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
