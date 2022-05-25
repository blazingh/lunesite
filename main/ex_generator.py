import random
import json


def gen_wod(c_level, c_equip, c_risk, c_space, c_muscle, c_time, c_goal):

    c_time = int(c_time)
    c_level = int(c_level)
    c_space = int(c_space)

    with open('main/exercise_data.json') as f:
        data = json.load(f)["ex_list"]

    ex_list = []
    fin_list = []

    def ex_count_f():
        if c_goal == "tone":
            return c_time // 3 + random.randint(0, 1)
        if c_goal == "gain":
            return c_time // 5 + random.randint(0, 1)
        if c_goal == "lose":
            return c_time // 4 + random.randint(0, 1)


    ex_count = ex_count_f()

    def filter_list():

        for i in data:
            if c_goal == "tone":
                if int(i["Level"]) != c_level:
                    continue
            if c_goal == "gain":
                if int(i["Level"]) < c_level:
                    continue
            if c_goal == "lose":
                if int(i["Level"]) >= c_level:
                    continue
            if int(i["Space"]) > c_space:
                continue
            if not all(mcl in c_muscle for mcl in i["Muscle"]):
                continue
            if i["Equip"][0] != "none":
                if  not all(equip in c_equip  for equip in i["Equip"]):
                    continue
            if i["Risk"][0] != "none":
                if all(rsk in c_risk for rsk in i["Risk"]):
                    continue
            ex_list.append(i)

        random.shuffle(ex_list)
        random.shuffle(c_muscle)


    def pick_from_list():

        for m in c_muscle:
            for e in ex_list:
                if len(fin_list) < ex_count:
                    if m in e["Muscle"]:
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
            round_count, round_time, rest_time = rep_round(i["Time"])
            wod_script.append({"name": i["Name"], "work": round_time, "rest": rest_time, "round": round_count})


    filter_list()
    pick_from_list()
    gen_wod()


    return wod_script