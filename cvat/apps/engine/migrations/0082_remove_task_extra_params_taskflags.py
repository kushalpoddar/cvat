# Generated by Django 4.2.13 on 2024-08-20 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("engine", "0081_task_extra_params"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="extra_params",
        ),
        migrations.CreateModel(
            name="TaskFlags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_librivox", models.BooleanField(default=False)),
                ("is_vctx", models.BooleanField(default=False)),
                ("is_voxceleb", models.BooleanField(default=False)),
                ("is_librispeech", models.BooleanField(default=False)),
                ("is_voxpopuli", models.BooleanField(default=False)),
                ("is_tedlium", models.BooleanField(default=False)),
                ("is_commonvoice", models.BooleanField(default=False)),
                (
                    "task",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="flags",
                        to="engine.task",
                    ),
                ),
            ],
        ),
    ]