# Generated by Django 3.1.7 on 2021-05-29 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0013_documentreview_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentreview',
            name='document_template',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='document.documenttemplate'),
            preserve_default=False,
        ),
    ]