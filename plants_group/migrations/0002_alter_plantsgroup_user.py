# Generated by Django 4.1.5 on 2023-01-24 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("member", "0001_initial"),
        ("plants_group", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plantsgroup",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="member.member",
            ),
        ),
    ]