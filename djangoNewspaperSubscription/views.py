import email

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Subscriber


def index_page(request):
    return render(request, "insert.html")


def edit_page(request):
    return render(request, "edit.html")


def table_page(request):
    return render(request, "table.html")


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        city = request.POST.get('city')
        area = request.POST.get("area")
        estate = request.POST.get("estate")
        house_number = request.POST.get("house_number")
        copies = request.POST.get("copies")
        months = request.POST.get("months")

        query = Subscriber(name=name,
                           email=email,
                           age=age,
                           gender=gender,
                           country=country,
                           city=city,
                           area=area,
                           estate=estate,
                           house_number=house_number,
                           copies=copies,
                           months=months)
        query.save()
        return redirect("/")

    return render(request, 'table.html')


def deleteData(request, id):
    d = Subscriber.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, 'insert.html')


def update_Data(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        country = request.POST.get("country")
        city = request.POST.get("city")
        area = request.POST.get("area")
        estate = request.POST.get("estate")
        house_number = request.POST.get("house_number")
        copies = request.POST.get("copies")
        months = request.POST.get("months")

        update_info = Subscriber.objects.get(id=id)
        update_info.name = name
        update_info.email = email
        update_info.age = age
        update_info.gender = gender
        update_info.country = country
        update_info.city = city
        update_info.area = area
        update_info.estate = estate
        update_info.house_number = house_number
        update_info.copies = copies
        update_info.months = months
        update_info.save()

        messages.success(request, 'Updated successfully')
        return redirect("/")

    d = Subscriber.objects.get(id=id)
    context = {"d": d}
    return render(request, 'edit.html', context)
def pay