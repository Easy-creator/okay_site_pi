# Generated by Django 5.0 on 2024-03-29 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loader', '0010_fakekey'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fakekey',
            options={'ordering': ['-date'], 'verbose_name': 'ZFake Keys', 'verbose_name_plural': 'ZFake Keys'},
        ),
    ]
