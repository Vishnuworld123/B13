from django.shortcuts import render, redirect
from django.http import request, JsonResponse, HttpResponse
from .models import Product
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def welcome(request):
    data = {
        "message": "Hello from Django!",
        "status": "success"
    }
    return JsonResponse(data)


def plain_text_view(request):
    return HttpResponse("Hello, this is plain text.")


def html_view(request):
    html_content = "<h1>Welcome to Django</h1><p>This is an HTML response.</p>"
    return HttpResponse(html_content)


def greet_user(request):
    name = request.GET.get('name', 'Guest')
    return JsonResponse({"message": f"Hello, {name}!"})


def hello_template_view(request):
    nm = request.GET.get("name", "Guest")
    context = {
        'name': nm  # you can make this dynamic with request.GET.get('name')
    }
    return render(request, 'home.html', context)

def users_list_view(request):
    users = ['Anjali', 'Ravi', 'Aman', 'Pooja']
    return render(request, 'users.html', {'users': users})

@login_required
def get_products(request):
    print("in get_products")
    # all_prod = Product.objects.all() # select * from product;
    all_prod = Product.objects.filter(is_deleted=False) # select * from product where is_deleted=false;
    return render(request, "products.html", {"products": all_prod})

@csrf_exempt
@login_required
def create_product(request):
    if request.method == "POST":
        pid = request.POST.get("prod_id")
        name = request.POST["nm"]
        descr = request.POST["desc"]
        price = request.POST["prc"]
        qty = request.POST["qty"]
        if not pid:
            Product.objects.create(name=name, description=descr, price=price, qty=qty)
        else:
            prod_obj = Product.objects.get(id=pid)
            prod_obj.name = name
            prod_obj.description = descr
            prod_obj.price = price
            prod_obj.qty = qty
            prod_obj.save()

        return redirect("get_all_products")

    else:
        return render(request, "create_product.html")

@csrf_exempt
def hard_delete_product(request, pid):
    Product.objects.get(id=pid).delete()
    return redirect("get_all_products")

@csrf_exempt
def soft_delete_product(request, pid):
    prod_obj = Product.objects.get(id=pid)
    prod_obj.is_deleted = True
    prod_obj.save()
    return redirect("get_all_products")


def update_product(request, pid):
    prod = Product.objects.get(id=pid)
    return render(request, "create_product.html", {"product": prod})

@csrf_exempt
def upload_csv(request):
    if request.method == "POST":
        csv_file = request.FILES.get("csv_file")
        if not csv_file.name.endswith('.csv'):
            return HttpResponse("Please upload a valid CSV file.")
        
        df = pd.read_csv(csv_file)

        required_cols = {'name', 'description', 'price', 'qty'}
        if not required_cols.issubset(df.columns):
            return HttpResponse("Please upload a CSV with valid columns.")

        for _, row in df.iterrows():
            # TODO: bulk_create for performance
            # Product(
            #     name=row['name'],
            #     description=row['description'],
            #     price=row['price'],
            #     qty=row['qty'],
            #     created_by="System"  # Assuming 'System' is a placeholder for the user creating the product
            # )

            Product.objects.create(
                name=row['name'],
                description=row['description'],
                price=row['price'],
                qty=row['qty'],
                created_by=User.objects.get(username='admin')  # Assuming 'System' is a placeholder for the user creating the product
            )
        return HttpResponse("CSV uploaded and products created successfully.")
                # insert into product (name, description, price, qty) values (row['name'], row['description'], row['price'], row['qty']), (row['name'], row['description'], row['price'], row['qty']), (row['name'], row['description'], row['price'], row['qty'])
        
        # return redirect("get_all_products")
    
    return render(request, "upload_csv.html")

def download_csv(request):
    pass