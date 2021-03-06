from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_auto_20160214_0355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField()),
                ('finishTime', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='activity',
            name='approx_time',
            field=models.IntegerField(),
        ),
    ]
