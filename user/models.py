"""
This is the custom user model which will overwirtes default user model of django
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields import AutoField


class MyUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        # if not username:
        #     raise ValueError("Users must have an username")

        user = self.model(
                email = self.normalize_email(email),
                # username=username
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            # username = username
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    # this fileds are assigned by our self
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    # username = models.CharField(max_length=30, unique=True)
    # this are the fields that is required for the creation of user
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # some optional field that is possible
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)


    USERNAME_FIELD = "email" # name of field required to login
    # REQUIRED_FIELDS = ['username'] # if optional fields are assinged then that should be added too.
     
    objects = MyUserManager()

    # def __str__(self):
    #     return self.username

    # this is required to create custom user
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        abstract = True
        

# we need to add this to settings file to tell django where our custom user model lies

class Admin(MyUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
