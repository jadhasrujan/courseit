# admin.py

from django.contrib import admin
from .models import Courses, Sections, Chapter

# Inline for Chapter in Section
class ChapterInline(admin.TabularInline):  # Or use StackedInline for a vertical layout
    model = Chapter
    extra = 1  # Number of empty rows to show
    fields = ('title', 'description', 'video_url')  # Customizable fields to display

# Inline for Section in Course
class SectionInline(admin.TabularInline):
    model = Sections
    extra = 1  # Number of empty rows to show
    inlines = [ChapterInline]  # Nested inline for Chapters within Sections
    fields = ('section_name', 'description')  # Customize the fields for Section

# Custom Admin for Courses
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'duration', 'created_at', 'instructor_name', 'short_description', 'requirements')
    search_fields = ('course_name', 'instructor_name', 'instructor_name')
    inlines = [SectionInline]  # Display Sections within Course

# Custom Admin for Sections
class SectionsAdmin(admin.ModelAdmin):
    list_display = ('section_name', 'course', 'description')
    search_fields = ('section_name', 'course__course_name')  # Search Sections by Course name
    inlines = [ChapterInline]  # Display Chapters within Sections

# Register models in the admin
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Sections, SectionsAdmin)
admin.site.register(Chapter)
