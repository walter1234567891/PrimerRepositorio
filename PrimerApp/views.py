from django.shortcuts import render

# Create your views here.
def visaInicio(request):
    return render(request,'index.html')