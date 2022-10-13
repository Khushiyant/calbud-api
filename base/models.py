from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils import timezone


class UserAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name,password=None, phone=None, profile_image=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            profile_image=profile_image,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, first_name, last_name, password=None, phone=None, profile_image=None
    ):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            profile_image=profile_image,
        )

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    weight = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    profile_image = models.URLField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    premium_at = models.DateTimeField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    # audit fields
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_staff(self):
        return self.is_admin

    def get_name(self):
        return self.first_name

    def __str__(self) -> str:
        return self.email


class FoodProfile(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField(max_length=300, null=True, blank=True)
    kcal = models.IntegerField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()
    fiber = models.FloatField()

    # audit fields
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    def get_name(self):
        return self.name

class PerDayProfile(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    food = models.ForeignKey(FoodProfile, on_delete=models.CASCADE)
    date = models.DateField()

    # audit fields
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user} {self.food} {self.date}"

    def get_name(self):
        return f"{self.user} {self.food} {self.date}"


    