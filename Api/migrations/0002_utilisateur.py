# Generated by Django 2.2.4 on 2019-08-29 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_utilisateur', models.CharField(max_length=50)),
                ('pseudo', models.CharField(max_length=50)),
                ('droit', models.CharField(max_length=50)),
                ('etat', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
