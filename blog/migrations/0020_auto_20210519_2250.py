# Generated by Django 3.1.7 on 2021-05-19 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20210516_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='cate_image',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.blogcategory'),
        ),
    ]