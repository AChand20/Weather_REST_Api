# Generated by Django 2.1 on 2019-03-07 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=10)),
                ('metric', models.CharField(max_length=10)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('value', models.DecimalField(decimal_places=1, max_digits=10)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='weather',
            unique_together={('location', 'metric', 'year', 'month', 'value')},
        ),
    ]
