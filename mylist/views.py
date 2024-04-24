from django.shortcuts import render
from .models import ShoppingItem

# Create your views here.
def mylist(request):
    if request.method == 'POST':
        print('Received data : ', request.POST['itemName'])
        #adding items to database
        ShoppingItem.objects.create(name = request.POST['itemName'] )


    return render(request, 'shoplist.html')
