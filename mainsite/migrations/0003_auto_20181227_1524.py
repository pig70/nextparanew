# Generated by Django 2.1.1 on 2018-12-27 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20181227_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='originalstory',
            name='original_story_author_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='original_author_image', to='userprofile.AuthorProfile'),
        ),
    ]