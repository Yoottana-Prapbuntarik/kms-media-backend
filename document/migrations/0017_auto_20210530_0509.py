# Generated by Django 3.1.7 on 2021-05-29 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0016_remove_documentreview_document_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentreview',
            name='document_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='document.documenttype'),
        ),
    ]