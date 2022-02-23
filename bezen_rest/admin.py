from django.contrib import admin

# Register your models here.
from .models import Fish
from .models import ProcessedFish

admin.site.register(Fish)
admin.site.register(ProcessedFish)