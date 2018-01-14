# Generated by Django 2.0.1 on 2018-01-08 12:43

from django.db import migrations, models
import yamlfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('engine', models.CharField(default='reclass', max_length=32)),
                ('metadata', yamlfield.fields.YAMLField(blank=True, null=True)),
                ('status', models.CharField(default='unknown', max_length=32)),
            ],
            options={
                'verbose_name_plural': 'Inventories',
            },
        ),
    ]