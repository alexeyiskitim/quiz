# Generated by Django 3.2.7 on 2021-10-21 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0011_rename_quizquestionresult_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Текст вопроса'),
        ),
    ]