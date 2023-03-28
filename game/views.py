from django.shortcuts import render

# Create your views here.
def page(request):
    return render(request,"index.html")
def page2(request):
    return render(request,"browse.html")
def page3(request):
    return render(request,"details.html")
def page4(request):
    return render(request,"streams.html")