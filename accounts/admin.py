from django.contrib import admin

from .models import books,bookissue

class booksAdmin(admin.ModelAdmin):
    list_display=['bookid','bookname','book_author','publish_date','book_description','book_image']

class bookissueAdmin(admin.ModelAdmin):
    list_display=['issuedate','returndate','user','book']

#class bookissueAdmin(admin.ModelAdmin):
#    list_display=['bookid','bookname','book_author','issuedate','returndate','user']


# Register your models here.
admin.site.register(books,booksAdmin)
admin.site.register(bookissue,bookissueAdmin)
