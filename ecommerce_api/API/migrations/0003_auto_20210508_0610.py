# Generated by Django 3.1.2 on 2021-05-08 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
        ('API', '0002_auto_20210508_0610'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='userId',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='API.QuantityProduct'),
        ),
        migrations.AddField(
            model_name='order',
            name='userId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='productSlug',
            field=models.SlugField(default='', max_length=500, unique=True),
        ),
        migrations.AddField(
            model_name='productdetails',
            name='brand',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]