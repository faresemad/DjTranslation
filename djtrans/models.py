from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, verbose_name=_("Created by"), on_delete=models.CASCADE, related_name="books")
    updated_by = models.ForeignKey(User, verbose_name=_("Updated by"), on_delete=models.CASCADE, related_name="updated_books")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")
        ordering = ["-created_at"]
