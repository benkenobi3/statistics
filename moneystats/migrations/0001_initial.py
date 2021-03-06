# Generated by Django 3.0.4 on 2020-05-19 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('date', models.DateTimeField()),
                ('cash_check', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='moneystats.Check')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='moneystats.Category')),
            ],
        ),
    ]
