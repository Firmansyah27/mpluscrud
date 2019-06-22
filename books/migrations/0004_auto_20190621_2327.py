# Generated by Django 2.2.2 on 2019-06-21 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20190621_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='type_of_book',
            field=models.CharField(blank=True, choices=[('novel', 'NOVEL'), ('documentation', 'Documentation'), ('other', 'Other')], max_length=200, null=True),
        ),
    ]
