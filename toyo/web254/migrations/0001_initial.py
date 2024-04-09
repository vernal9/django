# Generated by Django 4.0.1 on 2022-04-21 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='daily',
            fields=[
                ('IDENTIFY', models.CharField(db_column='IDENTIFY', max_length=10, primary_key=True, serialize=False)),
                ('WORK_DATE', models.CharField(db_column='WORK_DATE', max_length=10)),
                ('CREATE_USER_ID', models.CharField(db_column='CREATE_USER_ID', max_length=6)),
                ('MEMO', models.TextField(db_column='MEMO')),
            ],
            options={
                'verbose_name': '個人日誌',
                'db_table': '[toyo_web].[dbo].[EMPLOYEE_DIARY_HEAD]',
                'ordering': ['WORK_DATE'],
            },
        ),
    ]
