# Generated by Django 3.2.9 on 2022-03-26 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220326_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
