# Generated by Django 4.1.5 on 2023-01-23 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Disease",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
            ],
            options={"db_table": "disease", "managed": True,},
        ),
    ]