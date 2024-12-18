# Generated by Django 4.2.5 on 2023-12-07 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_text', models.CharField(max_length=140)),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='date posted')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('likers', models.ManyToManyField(related_name='likers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
