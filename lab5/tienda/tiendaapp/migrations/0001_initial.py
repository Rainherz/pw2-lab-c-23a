# Generated by Django 4.2.2 on 2023-06-20 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ArtNom', models.CharField(max_length=50, null=True)),
                ('ArtDes', models.TextField(help_text='Ingresa la descripción del artículo', max_length=1000, null=True)),
                ('ArtSto', models.IntegerField(default=0)),
                ('ArtPreUni', models.FloatField(default=0)),
                ('ArtEstReg', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CliDNI', models.CharField(max_length=8, unique=True)),
                ('CliApePat', models.CharField(max_length=20)),
                ('CliNom', models.CharField(max_length=20)),
                ('CliEstReg', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MarNom', models.CharField(max_length=20)),
                ('MarEstReg', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PedidoCabecera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PedCabFec', models.DateField()),
                ('PedCabEstReg', models.BooleanField(default=True)),
                ('PedCabCodCli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendaapp.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='TipoArticulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TipArtNom', models.CharField(max_length=20)),
                ('TipArtEstReg', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VenDNI', models.CharField(max_length=8, unique=True)),
                ('VenApePat', models.CharField(max_length=20)),
                ('VenNom', models.CharField(max_length=20)),
                ('VenEstReg', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PedidoDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PedDetCantidad', models.IntegerField(default=0)),
                ('PedDetPreUniArt', models.FloatField(default=0.0)),
                ('PedDetSubtotal', models.FloatField(default=0.0)),
                ('PedDetTot', models.FloatField(default=0.0)),
                ('PedDetEstReg', models.BooleanField(default=True)),
                ('PedDetArtCod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendaapp.articulo')),
                ('PedDetCodCab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='tiendaapp.pedidocabecera')),
            ],
        ),
        migrations.AddField(
            model_name='pedidocabecera',
            name='PedCabCodVen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendaapp.vendedor'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='ArtMarCod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tiendaapp.marca'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='ArtTipCod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tiendaapp.tipoarticulo'),
        ),
    ]
