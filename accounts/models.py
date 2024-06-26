from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class usersManager(BaseUserManager):
    def create_user(self, email, username, first_name, phone_number,last_name = None, password=None):
        if not email:
            raise ValueError("User must have email address")
        
        if not username:
            raise ValueError("User must have username")
        
        user = self.model(
            email= self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name =last_name,
            phone_number = phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        
        return user 
    
    def create_superuser(self, email, username, first_name, phone_number,last_name=None, password=None):
        user = self.create_user(
            email= self.normalize_email(email),
            username = username,
            first_name = first_name,
            phone_number = phone_number,
            password = password,
            last_name =last_name
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True

        user.save(using = self._db)
        return user

class user(AbstractBaseUser):
    Vendor = 1
    Customer = 2
    ROLE_CHOICE = (
        (Vendor, "Vendor"),
        (Customer, "Customer")
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=13, unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_super_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username","first_name","phone_number"]
    objects = usersManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

class userProfile(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="media/user/profile_picture/", blank=True, null=True)
    cover_profile = models.ImageField(upload_to="media/user/cover_profile_picture/", blank=True, null=True)
    address_line = models.CharField(max_length=50, blank=True, null=True)
    # address_line_2 = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    pin_code = models.CharField(max_length=6, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
    
@receiver(post_save, sender=user)
def createUserProfile(sender, instance, created, **kwargs):
    if created:
        userProfile.objects.create(user=instance)
