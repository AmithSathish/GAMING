
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [

    ]
    operations = [
        migrations.CreateModel(
            name='tablename',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtstr1', models.CharField(default='', max_length=255, null=True)),
                ('dtstr2', models.CharField(max_length=255)),
            ],
        ),
    ]
