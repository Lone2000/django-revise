# Generated by Django 3.2.6 on 2022-09-09 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_choice_votes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Celebrities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateTimeField(verbose_name='DOB')),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]