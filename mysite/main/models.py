from django.db import models

class Exercise(models.Model):

    motion_choices = [("static","static"),("dynamic","dynamic")]
    level_choices = [("beginner","beginner"),("average","average"),("intermediate","intermediate"),("athlete","athlete")]
    space_choices = [("minimal","minimal"),("some","some"),("large","large")]

    name = models.CharField(max_length=30)
    motion = models.CharField(max_length=10, choices=motion_choices, default="dynamic")
    level = models.CharField(max_length=12, choices=level_choices, default="beginner")
    time = models.IntegerField()
    space = models.CharField(max_length=10, choices=space_choices, default="minimal")
    details = models.TextField()

    def __str__(self):
        return self.name

class Exercise_muscle(models.Model):

    muscle_choices = [
        ("neck","neck"),("shoulder","shoulder"),("bicep","bicep"),
        ("forarm","forarm"),("chest","chest"),("core","core"),
        ("score","score"),("tricep","tricep"),("trap","trap"),
        ("lats","lats"),("lowback","lowback"),("hamstring","hamstring"),
        ("glute","glute"),("calf","calf"),("shin","shin"),
        ("quad","quad"),
        ]

    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    muscle = models.CharField(max_length=15, choices=muscle_choices)

    def __str__(self):
        return self.muscle

class Exercise_risk(models.Model):

    risk_choices = [
        ("wrist","wrist"),("elbow","elbow"),
        ("shoulder","shoulder"),("neck","neck"),("lowback","lowback"),
        ("knee","knee"),("ankle","ankle"),
    ]

    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    risk = models.CharField(max_length=12, choices=risk_choices)

    def __str__(self):
        return self.exercise.name

class Exercise_equip(models.Model):

    equip_choices = [
        ("rope","rope"),("band","band"),
        ("box","box"),("kettlebell","kettlebell"),("dumbbell","dumbbell"),
        ("ball","ball"),("bar","bar"),
    ]

    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    equipement = models.CharField(max_length=12, choices=equip_choices)

    def __str__(self):
        return self.exercise.name