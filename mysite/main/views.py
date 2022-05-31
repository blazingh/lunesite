from django.shortcuts import render
from django.http import HttpResponse, request
from main.exercise_handler import add_exe, fetch_exe, update_exe, generate_exe

def nothing(request):

    exercise_data = fetch_exe()

    context = {
        "ex_list" : exercise_data["ex_list"],
        "muscle_list" : exercise_data["muscle_list"],
        "equip_list" : exercise_data["equip_list"],
        "risk_list" : exercise_data["risk_list"]
    }

    return render(request, "main/index.html", context)


def add_ex(request):

    if request.method == "POST":

        name = request.POST.get("name")
        equip = request.POST.getlist("equip")
        muscle = request.POST.getlist("muscle")
        level = request.POST.get("level")
        risk = request.POST.getlist("risk")
        time = request.POST.get("time")
        space = request.POST.get("space")
        motion = request.POST.get("motion")
        details = request.POST.get("details")

        context = {
            "feedback" : add_exe(name, equip, muscle, level, risk, time, space, motion, details)
        }

        return render(request, "main/adder.html", context)

    return render(request, "main/adder.html")


def gen_ex(request):

    if request.method == "POST":

        equip = request.POST.getlist("equip")
        muscle = request.POST.getlist("muscle")
        level = request.POST.get("level")
        risk = request.POST.getlist("risk")
        time = request.POST.get("time")
        space = request.POST.get("space")
        goal = request.POST.get("goal")

        context = {
            "wod": generate_exe(level, equip, risk, space, muscle, time, goal)
        }
        
        return render(request, "main/workout.html", context)

    return render(request, "main/generator.html")


def wod_page(request):

    return
