from django.contrib import admin
from .models import Category,Book,Review
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Book,BookAdmin)
admin.site.register(Review)
admin.site.register(Category,CategoryAdmin)
# admin.site.register(BookSearch)