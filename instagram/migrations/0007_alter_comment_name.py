# Generated by Django 3.2.8 on 2021-10-16 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0006_alter_comment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
