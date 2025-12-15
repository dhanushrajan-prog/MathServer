from django.shortcuts import render
def mileage(request):
    km = int(request.POST.get('distance', 0))
    lt = int(request.POST.get('fuel', 0))
    mileage = km * lt if request.method == 'POST' else 0
    print("Distance=",km)
    print("Fuel=",lt)
    print("Mileage=",mileage)
    return render(request, 'mathapp/math.html', {'km': km, 'lt': lt, 'mileage': mileage})