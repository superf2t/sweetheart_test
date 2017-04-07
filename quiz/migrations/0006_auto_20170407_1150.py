# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 11:50
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0005_auto_20170406_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='selectedanswer',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='selectedanswer',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='selectedanswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='selectedanswer',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='selectedanswer',
            name='user',
        ),
        migrations.AddField(
            model_name='quiz',
            name='questions',
            field=models.ManyToManyField(to='quiz.Question'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='SelectedAnswer',
        ),
        migrations.AddField(
            model_name='quiz',
            name='user_answers',
            field=models.ManyToManyField(to='quiz.UserAnswer'),
        ),
    ]
