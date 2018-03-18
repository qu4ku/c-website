from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'user_info', 'city', 'website', 'phone')

	def user_info(self, obj):
		return obj.description

	# You can use this to change displayed field name
	# user_info.short_description = 'Info'


admin.site.register(UserProfile, UserProfileAdmin)
