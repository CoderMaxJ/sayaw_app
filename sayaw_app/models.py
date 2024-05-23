
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin,Group,Permission
from django.utils import timezone
from django.db import models

# models.py
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models

class UserInfoManager(BaseUserManager):
    def create_user(self, username, password=None, staff=False, superadmin=False):
        if not username:
            raise ValueError('Username must be required!')

        user = self.model(
            username=username,
            is_staff=staff,
            is_superuser=superadmin,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, staff=True, superadmin=True):
        user = self.create_user(username, password, staff, superadmin)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserInfoManager()

    USERNAME_FIELD = 'username'

    # Add related_name for groups and user_permissions
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_permissions')


class rooms(models.Model):
    is_availlable=models.BooleanField(default=True)
    gate_number=models.CharField(max_length=10,null=True)
    room_number=models.IntegerField(null=True)
    room_price=models.IntegerField(null=True)
    front_view=models.ImageField(upload_to='room_image/',null=True)
    inside_view1=models.ImageField(upload_to='room_image/',null=True)
    inside_view2=models.ImageField(upload_to='room_image/',null=True)
    inside_view3=models.ImageField(upload_to='room_image/',null=True)
    room_description=models.TextField(max_length=2000)
    
   
    

    
class cottages(models.Model):
    is_availlable=models.BooleanField(default=False)
    gate_number=models.CharField(max_length=10,null=True)
    cottage_number=models.IntegerField(null=True)
    cottage_price=models.IntegerField(null=True)
    front_view=models.ImageField(upload_to='cottage_image/',null=True)
    inside_view1=models.ImageField(upload_to='cottage_image/',null=True)
    inside_view2=models.ImageField(upload_to='cottage_image/',null=True)
    inside_view3=models.ImageField(upload_to='cottage_image/',null=True)
    cottage_description=models.TextField(max_length=2000)
   
   
    
class booking(models.Model):
    payment_method=models.CharField(max_length=20,null=True)
    is_fully_paid=models.BooleanField(null=True,default=False)
    is_paid=models.BooleanField(default=False,null=True)
    changeschedule_approve=models.BooleanField(default=False,null=True)
    change_schedule=models.BooleanField(default=False, null=True)
    transaction_Code=models.CharField(max_length=10,null=True)
    date_Reserved=models.DateField(null=True)
    time_Reserved=models.TimeField(null=True)
    guest_Name=models.CharField(max_length=30,null=True)
    guest_Lastname=models.CharField(max_length=30,null=True)
    guest_Address=models.CharField(max_length=50,null=True)
    guest_Number=models.IntegerField(null=True)
    cottage_number=models.IntegerField(null=True)
    cottage_price=models.IntegerField(null=True)
    room_number=models.IntegerField(null=True)
    gate_Number=models.CharField(max_length=50,null=True)
    room_Price=models.IntegerField(null=True)
    date_In=models.DateField(null=True)
    date_Out=models.DateField(null=True)
    stay_Duration=models.IntegerField(null=True)
    time_In=models.TimeField(null=True)
    time_Out=models.TimeField(null=True)
    feedback=models.TextField(max_length=200, null=True)
    partial_paid=models.IntegerField(default=0)
    total_bill=models.IntegerField(default=0)
    balance_bill=models.IntegerField(default=0)
    changeschedule_reason=models.TextField(null=True)
    
    def __str__(self):
        return self.guest_Name
    
# duplicates = booking.objects.values('field_name').annotate(max_id=models.Max('id'), count=models.Count('id')).filter(count__gt=1)

# for duplicate in duplicates:
#     # Keep the record with the highest ID (latest record)
#     booking.objects.filter(field_name=duplicate['name']).exclude(id=duplicate['max_id']).delete()
    
    
    
    
class paid(models.Model):
    guest_name=models.CharField(max_length=100)
    guest_lastname=models.CharField(max_length=100,null=True)
    payment_proof=models.ImageField(upload_to='payment_proof/')
    transaction_code=models.CharField(max_length=10)
    date_paid=models.DateField(null=True)
    time_paid=models.TimeField(null=True)
    total_bill=models.IntegerField(null=True)
        
    def __str__(self):
      return self.guest_name
    
    
class Guest_list(models.Model):
    guest_name=models.CharField(max_length=100,null=True)
    guest_lastname=models.CharField(max_length=100,null=True)
    guest_address=models.CharField(max_length=100,null=True)
    room=models.CharField(max_length=100,null=True)
    cottage=models.CharField(max_length=100,null=True)
    program=models.CharField(max_length=100)
    nationality=models.CharField(max_length=100,null=True)
    total_bill=models.IntegerField(null=True)
    def __str__(self):
        return self.guest_name
    
    
class nationality(models.Model):
    guest_nationality=models.CharField(max_length=50)
    
    def __str__(self):
        return self.guest_nationality


class information(models.Model):
    data=models.TextField(max_length=2000)
    def __str__(self):
        return self.data
    
class message_storage_1(models.Model):
    message=models.TextField(max_length=500)
    def __str__(self):
        return self.message
class message_storage_2(models.Model):
    message=models.TextField(max_length=500)
    def __str__(self):
        return self.message
    
class message_storage_3(models.Model):
    message=models.TextField(max_length=500)
    def __str__(self):
        return self.message
    
class gcash(models.Model):
    number=models.CharField(max_length=11)
class paymaya(models.Model):
    number=models.CharField(max_length=11)


class change_schedule(models.Model):
    code=models.TextField(max_length=7,null=True)
    reason=models.TextField(max_length=500,null=True)
    date=models.DateField(null=True)
    time=models.TimeField(null=True)

   