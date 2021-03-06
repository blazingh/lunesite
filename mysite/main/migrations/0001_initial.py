# Generated by Django 4.0.4 on 2022-05-27 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('motion', models.CharField(choices=[('st', 'static'), ('dy', 'dynamic')], default='dynamic', max_length=2)),
                ('level', models.CharField(choices=[('1', 'beginner'), ('2', 'average'), ('3', 'intermediate'), ('4', 'athlete')], default='2', max_length=1)),
                ('time', models.IntegerField()),
                ('space', models.CharField(choices=[('1', 'minimal'), ('2', 'some'), ('3', 'large')], default='2', max_length=1)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_1', models.CharField(choices=[('--', '--'), ('wrist', 'wrist'), ('elbow', 'elbow'), ('shoulder', 'shoulder'), ('neck', 'neck'), ('lowback', 'lowback'), ('knee', 'knee'), ('ankle', 'ankle'), ('none', 'none')], default='--', max_length=12)),
                ('risk_2', models.CharField(choices=[('--', '--'), ('wrist', 'wrist'), ('elbow', 'elbow'), ('shoulder', 'shoulder'), ('neck', 'neck'), ('lowback', 'lowback'), ('knee', 'knee'), ('ankle', 'ankle'), ('none', 'none')], default='--', max_length=12)),
                ('risk_3', models.CharField(choices=[('--', '--'), ('wrist', 'wrist'), ('elbow', 'elbow'), ('shoulder', 'shoulder'), ('neck', 'neck'), ('lowback', 'lowback'), ('knee', 'knee'), ('ankle', 'ankle'), ('none', 'none')], default='--', max_length=12)),
                ('risk_4', models.CharField(choices=[('--', '--'), ('wrist', 'wrist'), ('elbow', 'elbow'), ('shoulder', 'shoulder'), ('neck', 'neck'), ('lowback', 'lowback'), ('knee', 'knee'), ('ankle', 'ankle'), ('none', 'none')], default='--', max_length=12)),
                ('risk_5', models.CharField(choices=[('--', '--'), ('wrist', 'wrist'), ('elbow', 'elbow'), ('shoulder', 'shoulder'), ('neck', 'neck'), ('lowback', 'lowback'), ('knee', 'knee'), ('ankle', 'ankle'), ('none', 'none')], default='--', max_length=12)),
                ('risk_6', models.CharField(choices=[('--', '--'), ('wrist', 'wrist'), ('elbow', 'elbow'), ('shoulder', 'shoulder'), ('neck', 'neck'), ('lowback', 'lowback'), ('knee', 'knee'), ('ankle', 'ankle'), ('none', 'none')], default='--', max_length=12)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Muscle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muscle_1', models.CharField(choices=[('neck', 'neck'), ('shoulder', 'shoulder'), ('bicep', 'bicep'), ('forarm', 'forarm'), ('chest', 'chest'), ('core', 'core'), ('score', 'score'), ('tricep', 'tricep'), ('trap', 'trap'), ('lat', 'lat'), ('lowback', 'lowback'), ('hamstring', 'hamstring'), ('glute', 'glute'), ('calf', 'calf'), ('shin', 'shin'), ('quad', 'quad'), ('none', 'none'), ('--', '--')], default='--', max_length=15)),
                ('muscle_2', models.CharField(choices=[('neck', 'neck'), ('shoulder', 'shoulder'), ('bicep', 'bicep'), ('forarm', 'forarm'), ('chest', 'chest'), ('core', 'core'), ('score', 'score'), ('tricep', 'tricep'), ('trap', 'trap'), ('lat', 'lat'), ('lowback', 'lowback'), ('hamstring', 'hamstring'), ('glute', 'glute'), ('calf', 'calf'), ('shin', 'shin'), ('quad', 'quad'), ('none', 'none'), ('--', '--')], default='--', max_length=15)),
                ('muscle_3', models.CharField(choices=[('neck', 'neck'), ('shoulder', 'shoulder'), ('bicep', 'bicep'), ('forarm', 'forarm'), ('chest', 'chest'), ('core', 'core'), ('score', 'score'), ('tricep', 'tricep'), ('trap', 'trap'), ('lat', 'lat'), ('lowback', 'lowback'), ('hamstring', 'hamstring'), ('glute', 'glute'), ('calf', 'calf'), ('shin', 'shin'), ('quad', 'quad'), ('none', 'none'), ('--', '--')], default='--', max_length=15)),
                ('muscle_4', models.CharField(choices=[('neck', 'neck'), ('shoulder', 'shoulder'), ('bicep', 'bicep'), ('forarm', 'forarm'), ('chest', 'chest'), ('core', 'core'), ('score', 'score'), ('tricep', 'tricep'), ('trap', 'trap'), ('lat', 'lat'), ('lowback', 'lowback'), ('hamstring', 'hamstring'), ('glute', 'glute'), ('calf', 'calf'), ('shin', 'shin'), ('quad', 'quad'), ('none', 'none'), ('--', '--')], default='--', max_length=15)),
                ('muscle_5', models.CharField(choices=[('neck', 'neck'), ('shoulder', 'shoulder'), ('bicep', 'bicep'), ('forarm', 'forarm'), ('chest', 'chest'), ('core', 'core'), ('score', 'score'), ('tricep', 'tricep'), ('trap', 'trap'), ('lat', 'lat'), ('lowback', 'lowback'), ('hamstring', 'hamstring'), ('glute', 'glute'), ('calf', 'calf'), ('shin', 'shin'), ('quad', 'quad'), ('none', 'none'), ('--', '--')], default='--', max_length=15)),
                ('muscle_6', models.CharField(choices=[('neck', 'neck'), ('shoulder', 'shoulder'), ('bicep', 'bicep'), ('forarm', 'forarm'), ('chest', 'chest'), ('core', 'core'), ('score', 'score'), ('tricep', 'tricep'), ('trap', 'trap'), ('lat', 'lat'), ('lowback', 'lowback'), ('hamstring', 'hamstring'), ('glute', 'glute'), ('calf', 'calf'), ('shin', 'shin'), ('quad', 'quad'), ('none', 'none'), ('--', '--')], default='--', max_length=15)),
                ('muscle_7', models.CharField(choices=[('neck', 'neck'), ('shoulder', 'shoulder'), ('bicep', 'bicep'), ('forarm', 'forarm'), ('chest', 'chest'), ('core', 'core'), ('score', 'score'), ('tricep', 'tricep'), ('trap', 'trap'), ('lat', 'lat'), ('lowback', 'lowback'), ('hamstring', 'hamstring'), ('glute', 'glute'), ('calf', 'calf'), ('shin', 'shin'), ('quad', 'quad'), ('none', 'none'), ('--', '--')], default='--', max_length=15)),
                ('muscle_8', models.CharField(choices=[('neck', 'neck'), ('shoulder', 'shoulder'), ('bicep', 'bicep'), ('forarm', 'forarm'), ('chest', 'chest'), ('core', 'core'), ('score', 'score'), ('tricep', 'tricep'), ('trap', 'trap'), ('lat', 'lat'), ('lowback', 'lowback'), ('hamstring', 'hamstring'), ('glute', 'glute'), ('calf', 'calf'), ('shin', 'shin'), ('quad', 'quad'), ('none', 'none'), ('--', '--')], default='--', max_length=15)),
                ('muscle_9', models.CharField(choices=[('neck', 'neck'), ('shoulder', 'shoulder'), ('bicep', 'bicep'), ('forarm', 'forarm'), ('chest', 'chest'), ('core', 'core'), ('score', 'score'), ('tricep', 'tricep'), ('trap', 'trap'), ('lat', 'lat'), ('lowback', 'lowback'), ('hamstring', 'hamstring'), ('glute', 'glute'), ('calf', 'calf'), ('shin', 'shin'), ('quad', 'quad'), ('none', 'none'), ('--', '--')], default='--', max_length=15)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Equip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipement_1', models.CharField(choices=[('--', '--'), ('rope', 'rope'), ('band', 'band'), ('box', 'box'), ('kettlebell', 'kettlebell'), ('dumbbell', 'dumbbell'), ('ball', 'ball'), ('bar', 'bar'), ('none', 'none')], default='--', max_length=12)),
                ('equipement_2', models.CharField(choices=[('--', '--'), ('rope', 'rope'), ('band', 'band'), ('box', 'box'), ('kettlebell', 'kettlebell'), ('dumbbell', 'dumbbell'), ('ball', 'ball'), ('bar', 'bar'), ('none', 'none')], default='--', max_length=12)),
                ('equipement_3', models.CharField(choices=[('--', '--'), ('rope', 'rope'), ('band', 'band'), ('box', 'box'), ('kettlebell', 'kettlebell'), ('dumbbell', 'dumbbell'), ('ball', 'ball'), ('bar', 'bar'), ('none', 'none')], default='--', max_length=12)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.exercise')),
            ],
        ),
    ]
