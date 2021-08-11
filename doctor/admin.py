from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Doctor
from .forms import DoctortCreationForm

# this is to customise the user view at admin page
class MyDoctor(UserAdmin):
    add_form = DoctortCreationForm
    list_display = ('email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'first_name')
    readonly_fields = ('id', 'date_joined', 'last_login')
    ordering = ('first_name',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    add_fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')}),
    )

admin.site.register(Doctor, MyDoctor)