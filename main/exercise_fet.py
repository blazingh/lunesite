import json

def add_ex(name, equip, muscle, level, risk, time, type, space, motion):

   with open('main/exercise_data.json') as f:
      data = json.load(f)

   ex = {
            "Name": name,
            "Equipment": equip,
            "Muscle": muscle,
            "Level": level,
            "Risk": risk,
            "Time": time,
            "Type": type,
            "Space": space,
            "Motion": motion
         }

   data["ex_list"].append(ex)

      
   with open('main/exercise_data.json', 'w') as f:
      json.dump(data, f, indent = 3)
