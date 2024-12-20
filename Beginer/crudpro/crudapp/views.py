from django.shortcuts import render
from django.http import HttpResponse
from .models import Shoes



def saveshoes(request):
    if request.method=='POST':
        name=request.POST['sName']
        brand=request.POST['sbrand']
        size=request.POST['size']
        stype=request.POST['stype']
        price=request.POST['price']
        status=request.POST['status']
        new_shoe=Shoes(sName=name,sbrand=brand,size=size,stype=stype,price=price,status=status)
        Shoes.save(new_shoe)
        return HttpResponse("<h1>Success ....</h1>")
    else:
        return render(request, 'Addshoes.html')
    
def getAllShoes(request):
    shoeList = Shoes.objects.all()
    return render(request, 'shoeList.html', {'sList': shoeList})

def updateshoes(request):
    if request.method=='POST':
        shoe_id=request.POST['sId']
        name=request.POST['sName']
        brand=request.POST['sbrand']
        size=request.POST['size']
        stype=request.POST['stype']
        price=request.POST['price']
        status=request.POST['status']
        data=Shoes.objects.filter(sId=shoe_id)
        data.update(sName=name,sbrand=brand,size=size,stype=stype,price=price,status=status)
        return HttpResponse("<h1>Success ....</h1>")
    else:
        return render(request, 'Updateshoe.html')
    
    
def getShoeById(request,sId):
    data=Shoes.objects.filter(sId=sId)
    return render(request,"Updateshoe.html",{"shoe":data})

def deleteShoeById(request,sId):
    data=Shoes.objects.filter(sId=sId)
    data.delete
    return HttpResponse("<h1>Success ....</h1>")

# Create your views here.
