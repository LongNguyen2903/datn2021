# Generated by Django 2.2 on 2021-11-14 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main1', '0002_auto_20211114_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='U_id',
            field=models.IntegerField(default='88401', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='UpdateAt',
            field=models.DateTimeField(),
        ),
    ]
