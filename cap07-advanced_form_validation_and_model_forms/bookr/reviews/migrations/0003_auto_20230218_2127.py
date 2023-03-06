# Generated by Django 3.1 on 2023-02-18 21:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0002_auto_20230218_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reviews.publisher'),
        ),
        migrations.AlterField(
            model_name='bookcontributor',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reviews.book'),
        ),
        migrations.AlterField(
            model_name='bookcontributor',
            name='contributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reviews.contributor'),
        ),
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.ForeignKey(help_text='The Book that this review is for.', on_delete=django.db.models.deletion.PROTECT, to='reviews.book'),
        ),
        migrations.AlterField(
            model_name='review',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]