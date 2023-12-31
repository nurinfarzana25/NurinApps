import datetime
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from django.shortcuts import render
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Sum
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponseRedirect, JsonResponse
import json


@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)

    if request.method == "POST":
        action = request.POST.get('action')
        item_id = request.POST.get('item_id')

        try:
            item = Item.objects.get(id=item_id)

            if action == "increase":
                item.amount += 1
                item.save()
            elif action == "decrease":
                if item.amount > 1:
                    item.amount -= 1
                    item.save()
            elif action == "remove":
                item.delete()

        except Item.DoesNotExist:
            pass
    
    total_stok = items.aggregate(total_stok=Sum('amount'))['total_stok'] or 0
    total_item = items.count()


    context = {
        'name': request.user.username,
        'class': 'PBP C',
        'items': items,
        'total_stok': total_stok,
        'total_item': total_item,
        'last_login': request.COOKIES['last_login']
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)



def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json") 

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Get product berdasarkan ID
    product = Item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, product_id):
    if request.method == 'DELETE':
        Item.objects.filter(id=product_id).delete()

        return JsonResponse({'status':'success'})

def get_product_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_ajax(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        try:
            product = Item.objects.get(pk=id)
            product.amount += 1
            product.save()
            return HttpResponse(status=201)  # Status CREATED
        except Item.DoesNotExist:
            return HttpResponseNotFound("Product not found")

    return HttpResponseNotFound()

@csrf_exempt
def remove_ajax(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        try:
            product = Item.objects.get(pk=id)
            product.amount -= 1
            product.save()
            if product.amount <= 0:
                product.delete()
            return HttpResponse(status=201)  # Status CREATED
        except Item.DoesNotExist:
            return HttpResponseNotFound("Product not found")

    return HttpResponseNotFound()

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        berat = request.POST.get("berat")
        amount = request.POST.get("amount")
        image = request.POST.get("image")
        user = request.user

        new_product = Item(name=name, price=price, description=description, berat=berat, amount=amount, image=image, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            price = int(data["price"]),
            description = data["description"],
            amount = data["amount"],
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
