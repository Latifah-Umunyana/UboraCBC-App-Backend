# Generated by Django 5.0.6 on 2024-07-06 19:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_questions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student_details')),
            ],
        ),
    ]
