# Generated by Django 4.0.5 on 2022-06-16 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_user_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, null=True, verbose_name='Юзернейм'),
        ),
    ]