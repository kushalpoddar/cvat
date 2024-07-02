# Generated by Django 4.2.6 on 2024-04-05 04:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("engine", "0078_labeledimage_transcript_labeledtrack_transcript"),
    ]

    operations = [
        migrations.AddField(
            model_name="labeledimage",
            name="age",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="labeledimage",
            name="gender",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="labeledimage",
            name="locale",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="labeledshape",
            name="age",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="labeledshape",
            name="gender",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="labeledshape",
            name="locale",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="labeledtrack",
            name="age",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="labeledtrack",
            name="gender",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="labeledtrack",
            name="locale",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="trackedshape",
            name="age",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="trackedshape",
            name="gender",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="trackedshape",
            name="locale",
            field=models.TextField(default=""),
        ),
    ]