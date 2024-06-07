# Generated by Django 4.2.13 on 2024-06-07 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(default='@gmail.com', max_length=254)),
                ('image', models.ImageField(upload_to='images/')),
                ('about_emp', models.TextField()),
                ('programming_status', models.CharField(choices=[('Full Stack', 'Full Stack'), ('Backend Development', 'Backend Development'), ('Frontend Development', 'Frontend Development'), ('UX-UI development', 'UX-UI development')], max_length=100, null=True)),
                ('rezume', models.FileField(upload_to='rezume/')),
                ('date_of_birth', models.DateField()),
                ('github', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]