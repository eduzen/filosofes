# Generated by Django 2.1.3 on 2018-11-28 21:30

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('headline', models.CharField(max_length=800, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(null=True, upload_to='post-img/%Y/%m/%d')),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('published_date', models.DateField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]