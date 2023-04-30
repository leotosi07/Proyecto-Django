# Generated by Django 4.2 on 2023-04-30 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.animal')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('stock', models.PositiveIntegerField()),
                ('brand', models.CharField(max_length=50)),
                ('fecha_de_carga', models.DateField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos/')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.animal')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.categoria')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]