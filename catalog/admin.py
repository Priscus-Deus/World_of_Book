from django.contrib import admin
from .models import Book, Author, BookInstance, Status, Genre, Language
# Register your models here.


#admin.site.register(Book)
#admin.site.register(BookInstance)
#admin.site.register(Author)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    ist_filter = ('book', 'status')




admin.site.register(Author, AuthorAdmin)
admin.site.register(Status)
admin.site.register(Genre)
admin.site.register(Language)
