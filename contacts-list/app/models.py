from django.db import models
from typing import Optional


# Create your models here.
class Contact(models.Model):
    name = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    is_favorite = models.BooleanField()


def create(name, email, phone, favorite) -> Contact:
    contact = Contact(name=name, email=email, phone=phone, is_favorite=favorite)
    contact.save()
    return contact


def favorite() -> Contact:
    contacts = Contact.objects.filter(is_favorite=True)
    return contacts


def all() -> Contact:
    contacts = Contact.objects.all()
    return contacts


def update_email(name, email_new) -> Contact:
    contact = Contact.objects.get(name=name)
    contact.email = email_new
    contact.save()
    return contact

def find_by_name(name) -> Optional[Contact]:
    try:
        contacts = Contact.objects.get(name=name)
        return contacts
    except:
        return None

def delete(name):
    contact = Contact.objects.get(name=name)
    contact.delete()
    return contact