# Generated by Django 2.2.2 on 2019-06-22 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20190621_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='type_of_book',
            field=models.CharField(blank=True, choices=[('Novel', 'Novel'), ('Documentation', 'Documentation'), ('Other', 'Other')], max_length=200, null=True),
        ),
    ]