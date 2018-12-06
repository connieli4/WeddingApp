from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_auto_20160214_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='approx_time',
            field=models.IntegerField(null=True),
        ),
    ]
