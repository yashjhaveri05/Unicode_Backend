from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
import requests 
from .models import City
from .forms import CityForm
from .task1 import Task1

#Task 1,2 using dynamic url
def task(request, x, y):
    data = Task1(x,y)
    print(data)
    return JsonResponse(Task1(x,y), safe=False)

# Searching and Adding Weather according to City To Database using POST request
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=d9f018ab094f5f7a34df0ec41f79c368'

    err_msg = ''
    message = ''
    message_class = ''

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()
            
            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()

                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'No Such City Found!'
            else:
                city_names = City.objects.filter(name=new_city)
                if city_names.exists():
                    for city_name in city_names:
                        total = int(city_name.count) + 1
                    city_names.update(count=total)
                err_msg = 'City Already Exists!!'
        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City added successfully!'
            message_class = 'is-success'
    form = CityForm()

    cities = City.objects.all()
    weather_data = []
    for city in cities:
        res = requests.get(url.format(city)).json()
        city_weather = {
            'city' : city.name,
            'temperature' : res['main']['temp'],
            'description' : res['weather'][0]['description'],
            'icon' : res['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    total = City.objects.all().count()
    context = {
        'weather_data' : weather_data,
        'form' : form,
        'message' : message,
        'message_class' : message_class,
        'total': total,
    }
    return render(request, 'weather/index.html', context)

# Deleting particular city from DB
def delete_city(request, city_name):
    City.objects.get(name=city_name).delete() 
    return redirect('/')

# Weather of the city search form for GET request
def weather_search(request):
    return render(request, 'weather/weather.html')

# Increasing the count if the searched city already exists in the DB
def view_weather(request):
    if request.method == 'GET':
        city = request.GET['city']
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=d9f018ab094f5f7a34df0ec41f79c368'
    res = requests.get(url.format(city)).json()
    city_weather = {
            'city' : city,
            'temperature' : res['main']['temp'],
            'description' : res['weather'][0]['description'],
        }
    context = {
        'city_weather' : city_weather
    }
    if res['cod'] == 200:
        city_names = City.objects.filter(name=city)
        all_cities = City.objects.all()
        if city_names.exists():
            for city_name in city_names:
                total = int(city_name.count) + 1
            city_names.update(count=total)
    return render(request, 'weather/weather.html', context)

# Getting the top_three most searched cities
def top_three(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=d9f018ab094f5f7a34df0ec41f79c368'
    cities = City.objects.all().order_by('-count')[:3]
    res1 = requests.get(url.format(cities[0])).json()
    res2 = requests.get(url.format(cities[1])).json()
    res3 = requests.get(url.format(cities[2])).json()
    city_one = {
        'city' : cities[0].name,
        'temperature' : res1['main']['temp'],
        'description' : res1['weather'][0]['description'],
    }
    city_two = {
        'city' : cities[1].name,
        'temperature' : res2['main']['temp'],
        'description' : res2['weather'][0]['description'],
    }
    city_three = {
        'city' : cities[2].name,
        'temperature' : res3['main']['temp'],
        'description' : res3['weather'][0]['description'],
    }
    context = {
        'city_one' : city_one,
        'city_two' : city_two,
        'city_three' : city_three,
        'cities': cities
    }
    return render(request, 'weather/top_three.html', context)

# search form for entering the username using GET request
def user_search(request):
    return render(request, 'weather/github.html')

# getting github user information based on the GET search request
def github(request):
    if request.method == 'GET':
        username = request.GET['username']
    url = 'https://api.github.com/users/{}'
    res = requests.get(url.format(username)).json()
    user_info = {
        'name' : res['name'],
        'image' : res['avatar_url'],
        'link' : res['url'],
        'location' : res['location'],
        'bio' : res['bio'],
        'public_repos' : res['public_repos'],
        'followers' : res['followers'],
        'following' : res['following'], 
        'created' : res['created_at'][0:10],
        'update' : res['updated_at'][0:10],
    }
    context = {
        'user_info' : user_info,
    }
    return render(request, 'weather/github.html', context)