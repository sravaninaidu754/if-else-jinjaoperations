from django.shortcuts import render

# Create your views here.
def if_else(request):
    d={'a':10,'b':20}
    return render(request,'if-else.html',d)