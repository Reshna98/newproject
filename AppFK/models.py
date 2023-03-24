from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    Category_Name=models.CharField(max_length=70)
    Category_Number=models.IntegerField()

    # def __str__(self):
    #     return self.Course_Name

class ProductModel(models.Model):
    Category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
    Product_Name=models.CharField(max_length=100)
    Product_Brand=models.CharField(max_length=200)
    Price=models.IntegerField()
    MFD=models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return self.Std_Name