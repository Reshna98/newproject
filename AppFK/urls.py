from django.urls import path
from AppFK import views
from django.contrib import admin

# from AppEmail.views import stdform
urlpatterns = [
    path("",views.Home,name="Home"),
    path("CategoryPage",views.CategoryPage,name="CategoryPage"),
    path("Productpage",views.Productpage,name="Productpage"),
    path("AddCategory",views.AddCategory,name="AddCategory"),
    path("AddProduct",views.AddProduct,name="AddProduct"),
    path("ProductDetails",views.ProductDetails,name="ProductDetails"),
    path("delete/<int:pk>",views.delete,name="delete"),
    path("Tables",views.Tables,name='Tables')
    

]