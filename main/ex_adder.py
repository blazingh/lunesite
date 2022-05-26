import json

def add_exe(name, equip, muscle, level, risk, time, type, space, motion):

   with open('main/exercise_data.json') as f:
      data = json.load(f)

      for e in data["ex_list"]:
         if e['Name'] == name.title():
            return f"{e['Name']} already exists"

      if len(muscle) < 0:
         return "No muscles where selected"
            
   ex = {
            "Name": name.title(),
            "Equip": equip,
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

   return f"{ex['Name']} has been added to the list"
