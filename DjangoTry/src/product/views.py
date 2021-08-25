from django.shortcuts import get_object_or_404, redirect, render

from product.models import Product
from product.forms import ProductForm
# Create your views here.\
def product_view_create(request):
    form =  ProductForm(request.POST or None)
    print(form.is_valid())
    if form.is_valid():
        # print(form.is_valid())
        form.save()
        form=ProductForm()
    context={
        'form':form
    }
    return render(request,'products/product_create.html',context)

def product_view_detail(request,id):
    try:
        obj = get_object_or_404(Product,id=id)
        context = {
            "object":obj
        }
        return render(request,"products/product_detail.html",context)
    except:
        return render(request,"templates/nofound.html")
def product_view_list(request):
    obj = Product.objects.all()
    context = {
        "object":obj
    }
    return render(request,"products/product_list.html",context)
def product_view_delete(request,id):
    try:
        obj = get_object_or_404(Product,id=id)
        if request.method == "POST":
            obj.delete()
            return redirect('../')
        context = {
             "object":obj
        }
        return render(request,"products/product_delete.html",context)
    except:
        print(f"no existe {id}")
        return redirect('../')