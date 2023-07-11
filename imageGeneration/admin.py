from django.contrib import admin

from .models import Prompt, Image

admin.site.register(Prompt)

admin.site.register(Image)