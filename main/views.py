from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406414776',
        'name': 'Kenzie Nibras Tradezqi',
        'class': 'PBP D',
        'product_list' : product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }

    return render(request, "main.html", context)

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
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "show_product.html", context)


def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.get(pk=product_id)
        xml_data = serializers.serialize("xml", [product_item])
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product_item = Product.objects.get(pk=product_id)
        json_data = serializers.serialize("json", [product_item])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_xml(request):
    products = Product.objects.all()
    xml_data = serializers.serialize("xml", products)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    products = Product.objects.all()
    json_data = serializers.serialize("json", products)
    return HttpResponse(json_data, content_type="application/json")

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
@csrf_exempt
def create_product_ajax(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return JsonResponse({"status": "success", "message": "Product created successfully!"}, status=201)
        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

@login_required(login_url='/login')
def get_product_json(request, id):
    product = get_object_or_404(Product, pk=id)
    # Pastikan hanya pemilik yang bisa mengambil data untuk diedit
    if product.user != request.user:
        return JsonResponse({"status": "error", "message": "Unauthorized"}, status=403)

    data = {
        "name": product.name,
        "price": product.price,
        "description": product.description,
        "thumbnail": product.thumbnail,
        "category": product.category,
        "is_featured": product.is_featured,
    }
    return JsonResponse(data)


@login_required(login_url='/login')
@csrf_exempt
def edit_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.user != request.user:
        return JsonResponse({"status": "error", "message": "Unauthorized"}, status=403)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success", "message": "Product updated successfully!"})
        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)


@login_required(login_url='/login')
@csrf_exempt
def delete_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.user != request.user:
        return JsonResponse({"status": "error", "message": "Unauthorized"}, status=403)

    if request.method == "POST": # Menggunakan POST untuk keamanan
        product.delete()
        return JsonResponse({"status": "success", "message": "Product deleted successfully!"})
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

@csrf_exempt
def register_ajax(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Registration successful!'}, status=201)
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def login_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response_data = {'status': 'success', 'message': 'Login successful!'}
            # Buat response JSON dan set cookie di dalamnya
            response = JsonResponse(response_data)
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid credentials'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
# Hapus view edit_product dan delete_product yang lama jika ada
# View create_product juga tidak akan digunakan lagi untuk render form, tapi bisa dibiarkan
# def create_car(request):
#     form = CarForm(request.POST or None)

#     if form.is_valid() and request.method == "POST":
#         car_entry = form.save(commit = False)
#         car_entry.user = request.user
#         car_entry.save()
#         return redirect('main:show_main')

#     context = {'form': form}
#     return render(request, "create_car.html", context)

# def add_employee(request):
#     employee = Employee.objects.create(
#         name = "Adam",
#         age = 20,
#         persona = "Mahasiswa Fasilkom Angkatan 2007"
#     )

#     return HttpResponse(content = employee.name)

# # Create your views here.
