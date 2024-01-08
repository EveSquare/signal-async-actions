from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "content",
        "thumbnail",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "updated_at",
        "created_at",
    )
    search_fields = (
        "title",
        "content",
    )
    date_hierarchy = "created_at"
    ordering = ("created_at",)
    fields = (
        "title",
        "content",
        "thumbnail",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    filter_horizontal = ()
    list_select_related = ()
    raw_id_fields = ()
    save_on_top = False
    save_as = False
    autocomplete_fields = ()
    inlines = ()
    exclude = ()
    actions = ()
    view_on_site = False
