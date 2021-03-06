# Generated by Django 4.0.5 on 2022-06-06 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instapp', '0012_image_likess'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='likess',
        ),
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='likes',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_likes', to='instapp.image'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_likes', to='instapp.profile'),
        ),
    ]
