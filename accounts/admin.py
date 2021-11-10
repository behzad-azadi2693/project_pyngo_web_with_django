from django.contrib import admin

# Register your models here.
from django.contrib.admin.decorators import action
from django.contrib.auth import get_user_model
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(get_user_model())
class AdminUser(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('username', 'is_admin', 'is_active')
    list_filter = ('is_admin','username', 'phone_check')

    fieldsets = ( #this is for form
            ('اطلاعات شخصی',{'fields':('username','password', )}),
            ('دسترسی',{'fields':('is_active','is_admin','phone_check')}),
            ('محدودیت  ها',{'fields':('groups', 'user_permissions')}),
        )
    add_fieldsets = (#this is for add_form 
        (' اطلاعات شخصی',{'fields':('username','password')}),
        ('دسترسی',{'fields':('is_active','is_admin', 'groups', 'user_permissions')})
    )

    search_field = ('username',)
    ordering = ('username',)
