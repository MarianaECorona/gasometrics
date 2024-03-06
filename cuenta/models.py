from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class MyAccountManager (BaseUserManager):

    def create_user (self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address.")
        if not username:
            raise ValueError("Users must have an username.")
        user = self.model(
            email=self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Cuenta(AbstractBaseUser, PermissionsMixin):
    
    email               = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username            = models.CharField(max_length=20, unique=True)
    is_admin            = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    hide_email          = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True)  # Add this line

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def _str_(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_Label):
        return True