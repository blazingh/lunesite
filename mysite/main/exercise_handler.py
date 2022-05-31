import random
from .models import Exercise, Exercise_equip, Exercise_muscle, Exercise_risk


def add_exe(name, equip, muscle, level, risk, time, space, motion, details):

   name = name.title()

   for i in Exercise.objects.all():
      if name == i.name:
         return f"{i} Already Exist In The Library"

   exercise = Exercise(name = name, level = level, time = time, space = space, motion = motion, details=details)
   exercise.save()

   for i in muscle:
      ex_muscle = Exercise_muscle(exercise = exercise, muscle = str(i))
      ex_muscle.save()

   for i in risk:
      ex_risk = Exercise_risk(exercise = exercise, risk = str(i))
      ex_risk.save()

   for i in equip:
      ex_equip = Exercise_equip(exercise = exercise, equipement = str(i))
      ex_equip.save()

   return f"{name} Has Been Added To The Library"


def fetch_exe():

   all_exercises = Exercise.objects.all()

   data = {
      "ex_list" : all_exercises,
      "muscle_list" : {},
      "equip_list" : {},
      "risk_list" : {}
   }

   for i in all_exercises:

      muscle_list = Exercise_muscle.objects.all().filter(exercise=i).values_list("muscle", flat=True)
      risk_list = Exercise_risk.objects.all().filter(exercise=i).values_list("risk", flat=True)
      equip_list = Exercise_equip.objects.all().filter(exercise=i).values_list("equipement", flat=True)

      data["muscle_list"][i.name] = list(muscle_list)
      data["risk_list"][i.name] = list(risk_list)
      data["equip_list"][i.name] = list(equip_list)

   return data


def update_exe():
   pass


def generate_exe(c_level, c_equip, c_risk, c_space, c_muscle, c_time, c_goal):

    c_time = int(c_time)

    def c_level_f():
        if c_level == "beginner":
            return 1
        if c_level == "average":
            return 2
        if c_level == "intermediate":
            return 3
        if c_level == "athlete":
            return 4
    
    def c_space_f():
        if c_space == "minimal":
            return 1
        if c_space == "some":
            return 2
        if c_space == "large":
            return 3

    data = fetch_exe()

    ex_list = []
    fin_list = []

    def ex_count_f():
        if c_goal == "tone":
            return c_time // 3 + random.randint(0, 1)
        if c_goal == "gain":
            return c_time // 5 + random.randint(0, 1)
        if c_goal == "lose":
            return c_time // 4 + random.randint(0, 1)
    
    c_space = c_space_f()

    c_level = c_level_f()

    ex_count = ex_count_f()

    def filter_list():

        for i in data["ex_list"]:
            if c_goal == "tone":
                if int(i.level) != c_level:
                    continue
            if c_goal == "gain":
                if int(i.level) != c_level + 1:
                    continue
            if c_goal == "lose":
                if int(i.level) != c_level - 1:
                    continue
            if int(i.space) > c_space:
                continue
            if not all(mcl in c_muscle for mcl in data["muscle_list"][i.name]):
                continue
            if data["equip_list"][i.name][0] != "none":
                if  not all(equip in c_equip  for equip in data["equip_list"][i.name]):
                    continue
            if data["risk_list"][i.name][0] != "none":
                if all(rsk in c_risk for rsk in data["risk_list"][i.name]):
                    continue
            ex_list.append(i)

        random.shuffle(ex_list)
        random.shuffle(c_muscle)


    def pick_from_list():

        for m in c_muscle:
            for e in ex_list:
                if len(fin_list) < ex_count:
                    if m in data["muscle_list"][e.name]:
                        if e not in fin_list:
                            fin_list.append(e)
                            break
        
        while len(fin_list) < ex_count:
            if len(ex_list) > len(fin_list):
                ran_ex = random.choice(ex_list)
                if ran_ex not in fin_list:
                    fin_list.append(ran_ex)
                continue
            break


    def rep_round(rep_time):

        if c_goal == "tone":
            ex_rep = 12
            ex_round = 3
            ex_work = int(rep_time) * ex_rep + random.randint(0, 2)
            ex_rest = ex_work
            
        if c_goal == "gain":
            ex_rep = 5
            ex_round = 5
            ex_work = int(rep_time) * ex_rep + random.randint(0, 2)
            ex_rest = int(ex_work * 2.1)


        if c_goal == "lose":
            ex_rep = 18
            ex_round = 4
            ex_work = int(rep_time) * ex_rep + random.randint(0, 2)
            ex_rest = int(ex_work * 0.7)


        return ex_round, ex_work, ex_rest


    def gen_wod():

        global wod_script

        wod_script = []
        
        for i in fin_list:
            round_count, round_time, rest_time = rep_round(i.time)
            wod_script.append({"name": i.name, "work": round_time, "rest": rest_time, "round": round_count, "details": i.details})


    filter_list()
    pick_from_list()
    gen_wod()


    return wod_script