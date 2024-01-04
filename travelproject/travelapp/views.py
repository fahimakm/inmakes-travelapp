from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#def demo(request):
 #   return HttpResponse("hello world")

def demo(request):
    return render(request,"index.html")
    #def about(request):
     #   return render(request,"about.html")
    #def contact(request):
    #    return HttpResponse("hai")
def addition(request):
    n1=int(request.GET['num1'])
    n2 = int(request.GET['num2'])
    res=n1+n2
    return render(request,'about.html',{'result':res})