# admin.py

from django.contrib import admin
from .models import CourseClass, ClassContent,JoinedClass
from .models import ContentInteraction

@admin.register(ContentInteraction)
class ContentInteractionAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'is_marked_as_read', 'start_time', 'end_time', 'duration_in_minutes')
    list_filter = ('is_marked_as_read', 'user', 'content')  # Filter options in admin
    search_fields = ('user__username', 'content__title')  # Enable search by user and content title

    def duration_in_minutes(self, obj):
        """Calculate and display duration in minutes."""
        return obj.duration() if obj.duration() is not None else "Not completed"
    duration_in_minutes.short_description = 'Duration (minutes)'  # Label for the admin list display

    # Optionally, make read-only fields for records
    readonly_fields = ('start_time', 'end_time', 'duration_in_minutes')


class ClassContentInline(admin.TabularInline):
    model = ClassContent
    extra = 1  # Number of extra empty forms to display

@admin.register(CourseClass)
class CourseClassAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'teacher', 'unique_id', 'passkey')
    search_fields = ('course_name', 'teacher__username', 'unique_id')
    inlines = [ClassContentInline]  # Allows adding ClassContent directly in the CourseClass admin page

@admin.register(ClassContent)
class ClassContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'course_class', 'created_at')
    search_fields = ('title', 'course_class__course_name')
    list_filter = ('course_class', 'created_at')

class JoinedClassAdmin(admin.ModelAdmin):
    list_display = ('user', 'course_class')
    list_filter = ('course_class',)
    search_fields = ('user__username', 'course_class__course_name')

admin.site.register(JoinedClass, JoinedClassAdmin)