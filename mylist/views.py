from django.shortcuts import render
from .models import ShoppingItem

# Create your views here.
def mylist(request):
    if request.method == 'POST':
        print('Received data : ', request.POST['itemName'])
        #adding items to database
        ShoppingItem.objects.create(name = request.POST['itemName'] )
    all_items = ShoppingItem.objects.all()
    # ShoppingItem.objects.get()/filter() sind auch sinnvolle Varianten
    print (all_items)
    return render(request, 'shoplist.html', {'all_items' : all_items})
