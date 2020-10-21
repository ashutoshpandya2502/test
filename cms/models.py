from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Agent(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email =  models.EmailField(max_length = 254) 
@receiver(post_save, sender=User)
def update_agent(sender, instance, created, **kwargs):
	if created:
		Agent.objects.create(user=instance)
	instance.agent.save()
class Client(models.Model):
	first_name = models.CharField(max_length=200)
	last_name =  models.CharField(max_length=200)
	address =	models.CharField(max_length=200)
	agent = models.ForeignKey(Agent, on_delete=models.CASCADE)