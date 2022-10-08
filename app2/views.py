from django.shortcuts import render

# Create your views here.
def three(request):
    return render(request,'three.html')

def four(request):
    return render(request,'four.html')

def five(request):
    return render(request,'five.html')
