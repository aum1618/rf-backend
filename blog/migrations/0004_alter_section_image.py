# Generated by Django 4.2.2 on 2023-06-23 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_section_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='section_images/'),
        ),
    ]
