from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self,username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have a valid email address.')
        if not username:
            raise ValueError('Users must have a valid username.')

        print("extra_fields",extra_fields)
        account = self.model(
            email=self.normalize_email(email), username=username, **extra_fields
        )
        account.set_password(password)
        account.save()

        return account

    def create_superuser(self,username, email, password, **extra_fields):
        account = self.create_user(username,email, password, **extra_fields)
        account.is_admin = True
        account.save()
        return account


class Account(AbstractBaseUser):
    """ Model: account
    """
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    designation = models.CharField(max_length=40, blank=True)
    team = models.CharField(max_length=40, blank=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name]).strip()

    def get_short_name(self):
        return self.first_name
