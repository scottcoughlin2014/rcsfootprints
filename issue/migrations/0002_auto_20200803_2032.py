# Generated by Django 3.0.9 on 2020-08-03 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='fo_tickets_topic',
            new_name='fp_tickets_topic',
        ),
    ]