from django.shortcuts import render
from django.http import HttpResponse, request
import json
from main.ex_adder import add_exe
from main.ex_generator import gen_wod


def nothing(request):

    with open('main/exercise_data.json') as f:
        data = json.load(f)

    return render(request, "main/index.html", data)


def add_ex(request):

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
            "name": add_exe(name, equip, muscle, level, risk, time, type, space, motion)
        }

        return render(request, "main/adder.html", dict)

    return render(request, "main/adder.html")


def gen_ex(request):

    if request.method == "GET":
        return render(request, "main/generator.html")

    equip = request.POST.getlist("equip")
    muscle = request.POST.getlist("muscle")
    level = request.POST.get("level")
    risk = request.POST.getlist("risk")
    time = request.POST.get("time")
    space = request.POST.get("space")
    goal = request.POST.get("goal")

    dict = {
        "wod": gen_wod(level, equip, risk, space, muscle, time, goal)
    }
        
    if request.method == "POST":
        return render(request, "main/workout.html", dict)


def wod_page(request):

    return
