from django.db import models
import re
import bcrypt
from datetime import datetime

# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def validator(self,postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First Name must be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name must be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid Email Address'
        email_check = self.filter(email=postData['email'])
        if email_check:
            errors['email'] = "Email already in use"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if postData['password'] != postData['password2']:
            errors['password'] = 'Passwords do not match'
        return errors

    def authenticate(self, email, password):
        errors = {}
        if not EMAIL_REGEX.match(email):
            return False
        if len(password) < 1:
            return False
        users = self.filter(email=email)
        if not users:
            return False
        user = users[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())

    def register(self, postData):
        pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name = postData['first_name'],
            last_name = postData['last_name'],
            email = postData['email'],
            password = pw,
        )
  
class InquiryManager(models.Manager):
    def validatornew(self,postData):
        errors = {}
        if len(postData['companyName']) < 5:
            errors['companyName'] = "Company Name must be at least 5 characters"
        if len(postData['projectName']) < 2:
            errors['projectName'] = "Project Name must be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid Email Address'
        if len(postData['description']) < 5:
            errors['description'] = "Description Name must be at least 5 characters"
        return errors

    def add(self, postData):
        return self.create(
            company_name = postData['companyName'],
            project_name = postData['projectName'],
            email = postData['email'],
            start_date = postData['date'],
            project_length = postData['projectLength'],
            project_desc =  postData['description'],

        )


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()


class Inquiry(models.Model):
    company_name = models.CharField(max_length=45)
    project_name = models.CharField(max_length=45)
    email = models.EmailField()
    start_date = models.DateTimeField()
    project_length = models.IntegerField()
    project_desc =  models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = InquiryManager()

class Product(models.Model):
    description = models.CharField(max_length=45)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    hours =  models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    quantity_ordered = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class cart(models.Model):
    user = models.OneToOneField(User, related_name="user_uploaded_cart",on_delete=models.CASCADE)
    product = models.ManyToManyField(Product,related_name="products_added_carts")
    quantity = models.IntegerField(default=0)
    total_price = models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    Cart = models.ForeignKey(cart, related_name="order_items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    item_cost =  models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


  