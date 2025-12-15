# Ex.04 Design a Website for Server Side Processing
## Date:

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
```
urls.py

from django.urls import path
from mathapp import views
urlpatterns = [
    path('', views.mileage, name='mileage'),
]

views.py

from django.shortcuts import render
def mileage(request):
    km = int(request.POST.get('distance', 0))
    lt = int(request.POST.get('fuel', 0))
    mileage = km * lt if request.method == 'POST' else 0
    print("Distance=",km)
    print("Fuel=",lt)
    print("Mileage=",mileage)
    return render(request, 'mathapp/math.html', {'km': km, 'lt': lt, 'mileage': mileage})


math.html


<html>
<head>
    <title>CSS Box Model</title>
    <style>
        body {
            background-color: rgb(112, 169, 89);
        }
        .box {
            width: 700px;
            margin: 150px auto;
            background-color: cyan;
            padding: 30px;
            border: 5px solid orangered;
            text-align: center;
        }
    </style>
</head>

<body>
    <div class="box">
        <h1>Mileage Calculator</h1>
        <h3>Dhanush Rajan.T(25013743)</h3>

        <form method="POST">
            <input type="hidden" name="csrfmiddlewaretoken" value="NCcC8DdzT3XuntIBlnp5ERMMH45Xn15FA1ORPxFZ3Cku6EbbsEAdmGewsKhdlq5M">
    

            <label>Distance:</label>
            <input type="number" name="distance" value="12">
            <br><br>

            <label>Fuel:</label>
            <input type="number" name="fuel" value="2">
            <br><br>

            <button type="submit">Calculate</button>
            <br><br>

            <label>Mileage (KM/Litre):</label>
            <input type="number" value="24" readonly> km/l
        </form>
    </div>
</body>
</html>

```


## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (28)-1.png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot (27).png>)

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
