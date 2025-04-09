from django.contrib import admin
from .models import Course, Lesson
from django.urls import reverse
from django.utils.html import format_html
from urllib.parse import urlencode


class LessonInline(admin.StackedInline):
    model = Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # Define fieldsets for form layout
    fieldsets = (
        ("Basic Information", {
            "fields": [('title', 'description'), "price"],
            "classes": ["wide"],
        }),
        ("Optional Info", {
            "fields": ['status'],
            "classes": ["collapse"],
            "description": "This section contains optional fields for the user.",
        }),
    )

    list_display = ('title', 'description', 'price', 'author', 'status')
    list_display_link = ('title')
    list_editable = ('status', 'price')
    list_filter = ('author', 'status')
    inlines = [
        LessonInline,
    ]

    def get_form(self,request,obj,**kwargs):
        form = super().get_form(request,obj, **kwargs)
        form.base_fields['title'].label = ('Custom Title Label')
        return form

    def get_list_display(self, request):
        if request.user.is_superuser:
            return ('title', 'description', 'price', 'author', 'status')
        else:
            return ('title', 'description', 'author', 'status')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('course', 'title','view_lessons_count')

    def view_lessons_count(self, obj):
            count = obj.course.lessons.count()
            url = reverse("admin:admin_customise_course_changelist") + "?" + urlencode({'course': obj.course.id})
            return format_html("<a href='{}'>{} lesson</a>", url, count)

    view_lessons_count.short_description = "Lessons Count"
admin.site.site_title = 'Custom Admin'
admin.site.site_header = 'Custom Admin Project'
