from django.db import models
from Utils.model_abstacs import Model
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
    TitleDescriptionModel
)
from django.contrib.auth import get_user_model

class Contact(Model):
    
    class Meta:
        verbose_name_plural = "Contacts"

    user = models.ForeignKey(get_user_model(),verbose_name="USER", on_delete=models.CASCADE)
    name = models.CharField("Name",max_length=50)
    email = models.EmailField("EMAIL", max_length=254)
    image = models.ImageField("IMAGE",upload_to="contact/")
    message = models.TextField()
    
    def __str__(self):
        return self.name
    