from django.contrib import admin
from .models import Agent,Client
# Register your models here.
@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    pass
@admin.register(Client)
class AgentAdmin(admin.ModelAdmin):
    pass