from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Position, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _



User = get_user_model()



class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)



class ProfileAdmin(admin.ModelAdmin):
    list_display = ('position', 'user', 'image')



class UserAdmin(BaseUserAdmin):
	ordering = ['id']
	list_display = ['email', 'name']
	fieldsets = (
	(None, {'fields': ('email', 'password')}),
	(_('Personal Info'), {'fields': ('name',)}),
	(
		_('Permissions'),
		{
			'fields': (
				'is_active',
				'is_staff',
				'is_superuser',
                'groups',
                'user_permissions',
			)
		}
	),
	(_('Important dates'), {'fields': ('last_login',)}),
)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2')
		}),
	)





admin.site.register(Position, PositionAdmin) 
admin.site.register(Profile, ProfileAdmin) 
admin.site.register(User, UserAdmin)