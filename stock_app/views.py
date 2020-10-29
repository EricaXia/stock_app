from django.shortcuts import render

# Create your views here.
def stock_app(request):
    return render(request, 'hello_world.html', {})