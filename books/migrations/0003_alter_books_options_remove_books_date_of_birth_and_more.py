# Generated by Django 4.2.13 on 2024-06-11 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_tag_alter_books_options_reviewbooks_bookage"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="books",
            options={"verbose_name": "Книгу", "verbose_name_plural": "Книги"},
        ),
        migrations.RemoveField(
            model_name="books",
            name="date_of_birth",
        ),
        migrations.RemoveField(
            model_name="books",
            name="email",
        ),
        migrations.RemoveField(
            model_name="books",
            name="github",
        ),
        migrations.RemoveField(
            model_name="books",
            name="programming_status",
        ),
        migrations.RemoveField(
            model_name="books",
            name="rezume",
        ),
    ]
