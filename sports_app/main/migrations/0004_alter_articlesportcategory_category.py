# Generated by Django 4.0.3 on 2022-03-25 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_articlesportcategory_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesportcategory',
            name='category',
            field=models.CharField(max_length=30),
        ),
    ]
