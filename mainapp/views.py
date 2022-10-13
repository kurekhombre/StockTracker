from django.shortcuts import render

# Create your views here.
def stock_picker(request):
    return render(request, 'mainapp/stocktracker.html')