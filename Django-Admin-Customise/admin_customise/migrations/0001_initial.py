# Generated by Django 5.2 on 2025-04-05 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('publish_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('author', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=20)),
            ],
        ),
    ]
