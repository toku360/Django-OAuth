from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,AbstractBaseUser,PermissionsMixin
)
from django.urls import reverse_lazy

# Create your models here.

# BaseUserManager/ユーザーを生成する際のヘルパー(Helper)クラス

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Enter Email')
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        # DBに保存
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
# カスタムユーザーの定義クラス

class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # emailを一意としログインIDとする
    USERNAME_FIELD = 'email'
    # スーパーユーザーを作成する際に必要なフィールド
    REQUIRED_FIELDS = ['username']

    object = UserManager()

    # 処理後にhome画面へ遷移
    def get_absolute_url(self):
        return reverse_lazy('accounts:home')