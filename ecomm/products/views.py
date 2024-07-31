from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from products.models import *
from django.contrib import messages
from products.forms import *
# Create your views here.
def home(request):
    return render(request, 'products/index.html')

def collections(request):
    category = Category.objects.filter(status=0)
    return render(request, 'products/collections.html', context={"category": category})

def collectionsview(request, slug):
    if (Category.objects.filter(slug = slug, status = 0)):
        products = Product.objects.filter(category__slug = slug)
        category = Category.objects.filter(slug = slug).first()
        context = {'products': products, 'category': category}
        return render(request, 'products/products.html', context)
    else:
        messages.warning(request, 'No such category found')
        return redirect('collections')
    
def productview(request, cate_slug, prod_slug):
    if Category.objects.filter(slug = cate_slug, status=0):
        if Product.objects.filter(slug = prod_slug, status=0):
            product = Product.objects.filter(slug = prod_slug, status=0).first()
            context = {'product': product}

        else:
            messages.error(request, "No such product found")
            return redirect('collections')
    else:
        messages.error(request, "No such category found")
        return redirect('collections')
    
    return render(request, 'products/product_view.html', context)

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered Successfully! Login to Continue...')
            return redirect('/login')
    context = {'form': form}
    return render(request, 'products/auth/register.html', context)

def loginview(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect('/')
    
    else:
        if request.method == "POST":
            name = request.POST.get('username')
            pwd = request.POST.get('password')

            user = authenticate(request, username=name, password=pwd)

            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect('/')
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect('/login')
            
        return render(request, 'products/auth/login.html')

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out Successfully")
    
    return redirect('/')
    
    
