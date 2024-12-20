from django.shortcuts import render

# Create your views here.

def display(request):
    return render(request, 'AddEmployee.html')

def saveemp(request):
    if request.method == 'POST':
        eid=request.POST['eId']
        name=request.POST['fname']
        email=request.POST['email']
        password=request.POST['password']
        address=request.POST['address']
        conatct=request.POST['contact']
        print(eid)
        print(name)
        print(email)
        print(password)
        print(address)
        print(conatct)
    return render(request, 'success.html')
        
def displayfood(request):
    return render(request, 'food.html')

def savefood(request):
    if request.method == 'POST':
        F_id=request.POST['fId']
        F_name=request.POST['fname']
        F_price=request.POST['price']
        F_type=request.POST['type']
        print(F_id)
        print(F_name)
        print(F_price)
        print(F_type)
        return render(request,'success.html')