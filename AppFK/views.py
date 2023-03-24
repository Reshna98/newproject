from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def Home(request):
    return render(request,'home.html')


def CategoryPage(request):
    return render(request,'addcategory.html')


def AddCategory(request):
    if request.method == 'POST':
        categoryname=request.POST['categoryname']
        categorynumber=request.POST['categorynumber']
        data = CategoryModel(Category_Name=categoryname,Category_Number=categorynumber)
        data.save()
        # messages.info(request, 'New User Added')
        return redirect('Home')


def Productpage(request):
    category=CategoryModel.objects.all()
    context={'category':category}
    return render(request,'addproduct.html',context)


def AddProduct(request):
    if request.method=='POST':
        pdtname=request.POST['pdtname']
        pdtbrand=request.POST['pdtbrand']
        pdtprice=request.POST['pdtprice']
        # mfd=request.POST['mfd']
        select=request.POST['select']
        category=CategoryModel.objects.get(id=select)
        data = ProductModel(Product_Name=pdtname,Product_Brand=pdtbrand,Price=pdtprice,Category=category)
        data.save()
        return redirect('Home')


def ProductDetails(request):
    product_detail = ProductModel.objects.all()
    return render(request,'productdetail.html',{'product':product_detail})

def delete(request,pk):
    p=ProductModel.objects.get(id=pk)
    p.delete()
    return redirect('ProductDetails')

def Tables(request):
        category=CategoryModel.objects.all()
        product=ProductModel.objects.all()
        return render(request,'table.html',{'cdata':category,'pdata':product})
