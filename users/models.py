from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # add this to avoid reverse accessor name clashes
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="user_set_custom",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions "
        "granted to each of their groups.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="user_set_custom",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
