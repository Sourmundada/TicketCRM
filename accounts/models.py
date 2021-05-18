from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Custom Manager For Custom User Model.
class MyAccountManager(BaseUserManager):

    # Creating Normal Users.
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # Creating SuperUsers or Admin.
    def create_superuser(self, email, first_name, last_name, password):

        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            password = password,
        )

        # permissions for making the superuser, the admin of the website.
        user.is_admin = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


# Custom User Model For Admin Login.
class Account(AbstractBaseUser):

    # our fields
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    # required fields
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_superadmin   = models.BooleanField(default=False)

    # For Admin to login with email.
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    # User Model Manager
    objects = MyAccountManager()

    def __str__(self):
        return self.email

    # For admin to have all permissions.
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class Staff(Account):

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'        

    def __str__(self):
        return f'{self.first_name} {self.last_name}'