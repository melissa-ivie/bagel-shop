from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

# Create your models here.


class CustomUser(models.Model): 
    user_base = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    cashier = models.BooleanField(default=False)
    chef = models.BooleanField(default=False)
    owner = models.BooleanField(default=False)
    bagel_bucks = models.FloatField(default=100)
    phone_number= models.CharField(max_length=11, default="00000000000")

    def is_cashier(self): 
        return self.cashier      

    def is_chef(self): 
        return self.chef      

    def is_owner(self): 
        return self.owner      

    def __str__(self): 
        return "CustomUser: " + str(self.user_base.email)


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=len("preparation-cashier"), default="ordered")
    pickup_time = models.DateTimeField(default=timezone.now, editable=True)
    order_total = models.FloatField(default=0)
 
    def set_status(self, new_status): 
       self.status = new_status

    def __str__(self): 
        return "Order owned by " + str(self.owner)


class MenuItem(models.Model):
    description = models.CharField(max_length=40, default="")
    item_type = models.IntegerField(default=-1)
    primary_item = models.BooleanField(default=True) # essentially the opposite of being a topping item
    available = models.IntegerField(default=100)
    max_available = models.IntegerField(default=100) # magic number 100 is max inventory quantity
    price = models.FloatField(default=0)
    
    def fill_qty(self): 
        """ 
        Sets the amount in the inventory to maximum 
        """
        self.available = self.max_available


    def change_qty(self, amt):
        """
        Change the quantity available by amt  
        """
        self.available += amt

    def __str__(self): 
        return self.description


class LineItem(models.Model):
    containing_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    associated_line_item = models.ForeignKey('self', blank=True, on_delete=models.CASCADE, null=True, related_name="lineitem") # null, blank options allow the field to be nullable`
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    qty = models.IntegerField(default=0) 
    
    def __str__(self):
        return self.menu_item.description + " linked to: " + str(self.associated_line_item)

