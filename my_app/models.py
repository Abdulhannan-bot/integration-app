from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
# Create your models here.

SIGNAL_TYPE = (
    ("01", "Stakeholders Being Hired In Customer Accounts"),
    ("02", "Stakeholders Leaving Customer Accounts"),
    ("03", "Customers Moving Into Prospect Accounts"),
    ("04", "Customers Moving Into Greenfield Accounts"),
    ("05", "Stakeholders Being Hired In Prospect Accounts"),
    # ("06", "Competitors Being Hired In Customer Accounts"),
)

class Client(models.Model):
    user = models.ForeignKey(User, null = True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null = True)
    email = models.EmailField(max_length=255, null = True, blank = True)
    password = models.CharField(max_length=100, null = True)

    def __str__(self):
        return str(self.name)
    
class Signal(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    signal_type = models.CharField(max_length=2, choices=SIGNAL_TYPE)
    stakeholder_current_company = models.CharField(max_length=255) 
    stakeholder_first_name = models.CharField(max_length=128) 
    stakeholder_last_name = models.CharField(max_length=128)
    stakeholder_current_title = models.CharField(max_length=255) 
    stakeholder_time_in_current_role = models.CharField(max_length=255) 
    stakeholder_current_email = models.CharField(max_length=255) 
    stakeholder_phone_number = models.CharField(max_length=100, null = True)


@receiver(post_save, sender = User)
def user_generator(sender, created, instance, **kwargs):
  if created:
    Client.objects.create(
      user = instance,
      email = instance.email,
      name = instance.first_name+" "+instance.last_name,
      password = instance.password)