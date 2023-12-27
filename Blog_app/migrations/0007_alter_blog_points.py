# Generated by Django 4.2.6 on 2023-12-24 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Blog_app", "0006_blog_points_alter_points_point"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="points",
            field=models.ForeignKey(
                default=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Blog_app.points",
            ),
        ),
    ]