from django.contrib import admin
from .models import Category, Question, Answer



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)



class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug', 'author', 'category')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'question')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
