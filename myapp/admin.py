# myapp/admin.py
from django.contrib import admin
from myapp.models import UserProfile

class UserLocationAdmin(admin.ModelAdmin):
    list_display = ('username', 'latitude', 'longitude', 'timestamp')  # Columns to display in the admin panel
    search_fields = ('username',)  # Enable search by username
    list_filter = ('timestamp',)  # Filter by timestamp for easier navigation
    ordering = ('-timestamp',)  # Order by timestamp in descending order (newest first)

# Register the model and the admin class
admin.site.register(UserProfile, UserLocationAdmin)
