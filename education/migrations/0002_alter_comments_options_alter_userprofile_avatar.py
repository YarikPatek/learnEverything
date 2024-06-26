# Generated by Django 4.0.5 on 2022-08-07 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['id'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='education/images/avatar.png', upload_to='photos/%Y/%m/%d/', verbose_name='Аватар пользователя'),
        ),
    ]
