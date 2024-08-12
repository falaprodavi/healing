# Generated by Django 5.0.7 on 2024-08-05 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidade', models.CharField(max_length=100)),
                ('icone', models.ImageField(blank=True, null=True, upload_to='icones')),
            ],
        ),
    ]
