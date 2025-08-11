from django.db import models
from django.utils import timezone

class User(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=20)
    profile = models.ImageField(default="",upload_to="profile/")
    usertype = models.CharField(default="buyer",max_length=40)

    def __str__(self):
        return f"{self.fname}"
    
class Product(models.Model):
    seller = models.ForeignKey(User,on_delete=models.CASCADE)
    
    gender = (
        ("Male","Male"),
        ("Female","Female"),
        ("Kids","Kids")
    )
    category = (
        ("Casual","Casual"),
        ("Sports","Sports"),
        ("Sneakers","Sneakers"),
        ("Flip-Flops","Flip-Flops"),
        ("Party","Party"),
        ("Crocs","Crocs"),
        ("Sandals","Sandals")
    )
    size = (
        ("S","S"),
        ("M","M"),
        ("L","L"),
        ("XL","XL"),
        ("XXL","XXL")
    )


    gen = models.CharField(max_length=40,choices=gender)
    cat = models.CharField(max_length=40,choices=category)
    sz = models.CharField(max_length=40,choices=size)
    bname = models.CharField(max_length=40)
    pname = models.CharField(max_length=40)
    price = models.IntegerField()
    desc = models.TextField()
    pimage = models.ImageField(default="",upload_to="products/")

    def __str__(self):
        return f"{self.pname}"
    

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    ttime = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.product}"
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    time_date = models.DateTimeField(default=timezone.now())
    payment = models.BooleanField(default=False)
    qty = models.IntegerField(default=1)
    total = models.IntegerField()
    roundtotal = models.IntegerField()

    def __str__(self):
      return f"{self.product}"    