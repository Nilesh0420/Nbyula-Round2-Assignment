# Generated by Django 2.2.25 on 2022-01-27 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0005_auto_20220128_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='course',
            field=models.OneToOneField(help_text='Select any course created by you!', on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='teachers.TeacherCourse'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='number_of_questions',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='time',
            field=models.IntegerField(help_text='Duration of the quiz in seconds'),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.TextField()),
                ('quiz', models.ForeignKey(help_text='Select the same quiz whose questions you are viewing!', on_delete=django.db.models.deletion.CASCADE, related_name='question', to='teachers.Quiz')),
            ],
        ),
    ]
