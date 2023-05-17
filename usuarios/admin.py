from django.contrib import admin
from .forms import UserChangeForm, UserCreationForm
from .models import Users
from django.contrib.auth import admin as adm

@admin.register(Users)
class Users_admin(adm.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    fieldsets = adm.UserAdmin.fieldsets + (('Cargo', {'fields': ('cargo',)}),)