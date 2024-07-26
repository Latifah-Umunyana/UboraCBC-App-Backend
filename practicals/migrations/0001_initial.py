# Generated by Django 5.0.6 on 2024-07-06 20:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Practicals',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=50)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher_details')),
            ],
        ),
    ]
