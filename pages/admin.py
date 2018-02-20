from django.contrib import admin

from . import models


admin.site.register(models.Post)
admin.site.register(models.DifficultyLevel)
admin.site.register(models.PostType)
admin.site.register(models.Category)