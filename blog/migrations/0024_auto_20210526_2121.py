# Generated by Django 3.1.7 on 2021-05-26 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20210526_2120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlelikeandunlike',
            old_name='blog',
            new_name='blog_like',
        ),
        migrations.RenameField(
            model_name='articlelikeandunlike',
            old_name='own_user',
            new_name='user_like',
        ),
    ]