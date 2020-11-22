# Generated by Django 3.1.1 on 2020-10-24 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CATEGORIA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='COMUNA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DOCUMENTO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FORMA_PAGO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PRODUCTO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_barra', models.IntegerField(default=None)),
                ('nombre', models.CharField(default=None, max_length=200)),
                ('descripcion', models.CharField(default=None, max_length=200)),
                ('stock', models.IntegerField(default=None)),
                ('precio_venta', models.IntegerField(default=None)),
                ('precio_compra', models.IntegerField(default=None)),
                ('imagen', models.ImageField(default=None, upload_to='productos')),
            ],
        ),
        migrations.CreateModel(
            name='REGION',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=None, max_length=200)),
                ('numeracion', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='VENTA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=None)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('documento', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='almacen.documento')),
                ('forma_pago', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='almacen.forma_pago')),
            ],
        ),
        migrations.CreateModel(
            name='TIPO_PRODUCTO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=None, max_length=200)),
                ('categoria', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='almacen.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='SUCURSAL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=None, max_length=200)),
                ('descripcion', models.TextField(default=None, max_length=200)),
                ('direccion', models.CharField(default=None, max_length=200)),
                ('imagen', models.FileField(default=None, max_length=200, upload_to='')),
                ('comuna', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='almacen.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='LOCALIDAD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=None, max_length=200)),
                ('region', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='almacen.region')),
            ],
        ),
        migrations.CreateModel(
            name='ENTREGA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default=None, max_length=254)),
                ('direccion', models.CharField(default=None, max_length=100)),
                ('comuna', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='almacen.comuna')),
                ('venta', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='almacen.venta')),
            ],
        ),
        migrations.CreateModel(
            name='DETALLE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=None)),
                ('producto', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='almacen.producto')),
                ('sucursal', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='almacen.sucursal')),
                ('venta', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='almacen.venta')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='localidad',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='almacen.localidad'),
        ),
    ]