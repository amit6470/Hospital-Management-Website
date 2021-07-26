from django.shortcuts import render,HttpResponse

# Create your views here.
def hey(request):
    return HttpResponse("<h1> hello </h1>")
def index(request):
    return render(request,"index.html")
def blog(request):
    return render(request,"blog-single.html")
def appointment(request):
    return render(request,"appointment.html")