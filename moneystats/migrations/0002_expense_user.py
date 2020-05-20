# Generated by Django 3.0.4 on 2020-05-20 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moneystats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]