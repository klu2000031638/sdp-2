from django.http import HttpResponse
from django.shortcuts import render , redirect
from store.forms import ProductCreate, OrdersViews
from store.models.orders import Order




def Admin(request):
    upload = ProductCreate()
    o = Order.objects.all()
    if request.method == 'POST':
        upload = ProductCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            
            return redirect('Admin')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        
        return render(request, 'admin-panel.html', {'upload_form':upload, 'orders':o})



#csv
import csv
def exportcsv(request):
    ord = Order.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=orders.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Quantity', 'Price','Customer ID' ,'Product ID', 'Address', 'Phone Number','Date','Status'])
    ords = ord.values_list('id','quantity', 'price', 'customer_id', 'product_id', 'address', 'phone', 'date', 'status')
    for std in ords:
        writer.writerow(std)      
    
    return response  