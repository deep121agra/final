from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save

class UserManager(BaseUserManager):
    def create_user(self, firstname, lastname, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            firstname=firstname,
            lastname=lastname,
        )
        user.set_password(password)# it can used to set a pswwword in database
        user.save(using=self._db)
        return user

    def create_superuser(self, firstname, lastname, username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            firstname=firstname,
            lastname=lastname,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    VENDOR = 1
    CUSTOMER = 2
    ROLE_CHOICES = (
        (VENDOR, 'VENDOR'),
        (CUSTOMER, 'Customer'),
    )

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, null=True, blank=True)

    # Required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # Fixed typo
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    def get_role(self):
        if self.role==1:
            user_role='Vendor'
        elif self.role==2:
            user_role='Customer'
        return user_role       



class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='media/profile_picture', blank=True, null=True)
    cover_photo = models.ImageField(
        upload_to='media/cover_photo', blank=True, null=True)
    adress_line1 = models.CharField(max_length=50, blank=True, null=True)
    adress_line2 = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=14, blank=True, null=True)
    pin_code = models.CharField(max_length=6, blank=True, null=True)
    latitute = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email