# Generated by Django 5.0.6 on 2024-07-01 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testadl', '0002_pelicula_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('actualizacion', models.DateTimeField(auto_now=True)),
                ('cliente_activo', models.BooleanField(default=True)),
            ],
        ),
    ]
