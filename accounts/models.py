from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from accounts.managers import CustomUserManager


class User(AbstractBaseUser):
    display_name = models.CharField(verbose_name="Name", max_length=100,
                                    blank=True)
    email = models.EmailField(verbose_name="email", max_length=60,
                              unique=True)
    username = models.CharField(max_length=30, unique=True)
    mobile_number = models.CharField(max_length=10, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined',
                                       auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "mobile_number"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissions
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True
