from django.contrib import admin
from .models import Activity, Task


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish',   
                       'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'activity', 'publish',   
                       'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author', 'activity',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')