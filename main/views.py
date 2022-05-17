from django.shortcuts import render
from django.http import HttpResponse, request
from django.template import Context, Template
import json
import main.exercise_fet as fet



def nothing(request):

    with open('main/exercise_data.json') as f:
        data = json.load(f)

    return render(request, "main/index.html", data)

def home(request):

    if request.method == "POST":

        name = request.POST.get("name")
        equip = request.POST.getlist("equip")
        muscle = request.POST.getlist("muscle")
        level = request.POST.get("level")
        risk = request.POST.getlist("risk")
        time = request.POST.get("time")
        type = request.POST.get("type")
        space = request.POST.get("space")
        motion = request.POST.get("motion")


        dict = {
            "name": name
        }

        fet.add_ex(name, equip, muscle, level, risk, time, type, space, motion)

        name = request.POST.get("name")

        return render(request, "main/adder.html", dict)

    return render(request, "main/adder.html")
