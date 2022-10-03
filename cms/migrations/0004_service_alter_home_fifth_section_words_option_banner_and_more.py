# Generated by Django 4.1.1 on 2022-09-30 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_alter_home_fifth_section_words'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='título')),
                ('description', models.TextField(blank=True, verbose_name='descripción')),
                ('image', models.ImageField(upload_to='services', verbose_name='imagen')),
                ('button', models.CharField(max_length=255, verbose_name='botón')),
                ('button_url', models.URLField(verbose_name='url del botón')),
            ],
            options={
                'verbose_name': 'servicio',
            },
        ),
        migrations.AlterField(
            model_name='home',
            name='fifth_section_words',
            field=models.CharField(help_text='separadas por coma', max_length=255, verbose_name='palabras'),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='título')),
                ('description', models.TextField(blank=True, verbose_name='descripción')),
                ('image', models.ImageField(upload_to='options', verbose_name='imagen')),
                ('button', models.CharField(max_length=255, verbose_name='botón')),
                ('button_url', models.URLField(verbose_name='url del botón')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='cms.home')),
            ],
            options={
                'verbose_name': 'opción',
                'verbose_name_plural': 'opciones',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='título')),
                ('description', models.TextField(blank=True, verbose_name='descripción')),
                ('image', models.ImageField(upload_to='carousel', verbose_name='imagen')),
                ('subtitle', models.CharField(max_length=255, verbose_name='subtítulo')),
                ('button', models.CharField(max_length=255, verbose_name='botón')),
                ('button_url', models.URLField(verbose_name='url del botón')),
                ('short_title', models.CharField(max_length=255, verbose_name='título corto')),
                ('short_description', models.CharField(max_length=255, verbose_name='descripción corta')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousel', to='cms.home')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='home',
            name='services',
            field=models.ManyToManyField(to='cms.service', verbose_name='servicios'),
        ),
    ]
