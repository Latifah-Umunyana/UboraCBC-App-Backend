# Generated by Django 5.0.6 on 2024-07-06 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student_questions', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher_answers',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('answer', models.TextField()),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_questions.student_questions')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher_details')),
            ],
        ),
    ]