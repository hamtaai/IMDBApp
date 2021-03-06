# Generated by Django 2.1.2 on 2018-10-16 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('season', models.IntegerField()),
                ('episode', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('status', models.BooleanField()),
                ('air_time', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'episodes',
            },
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries'},
        ),
        migrations.AddField(
            model_name='entry',
            name='next_episode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.Episode'),
        ),
    ]
