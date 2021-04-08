# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


# from django.contrib.auth import get_user_model
# UserModel = get_user_model()


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    category_image = models.ImageField(upload_to='imgs/')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='imgs/')
    content = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        # user = UserModel(email=email, **extra_fields)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    object = CustomUserManager()

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    # object = UserManager()
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    comment = models.TextField()

    # for replies
    parent_field = models.ForeignKey("self", null=True, blank=True, related_name='parents', on_delete=models.CASCADE)

    # class Meta:
    #     ordering = ['-timestamp']

    def __str__(self):
        return self.comment

    def children(self):
        return Comment.objects.filter(parent=self)

    def is_parent(self):
        if self.parent_field is not None:
            return False
        return True
