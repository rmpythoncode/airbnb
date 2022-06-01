import requests
from django.shortcuts import render

# Create your views here.


def rooms(request):
    response = requests.get('http://127.0.0.1:8000/api/v1/rooms/')
    data = response.json()

    d = data['results']

    print(type(d))

    return render(request, 'web/index.html', {
        "data": data,
        "response": response,
    })


# def home(request):
#     # get the list of todos
#     response = requests.get('https://jsonplaceholder.typicode.com/todos/')
#     # transfor the response to json objects
#     todos = response.json()
#     print(type(todos))
#     return render(request, "web/home.html", {"todos": todos})
