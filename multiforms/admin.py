from django.contrib import admin

from .models import Question, Comment, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "date_posted", "upvotes")
    search_fields = ("title", "description", "posted_by")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment", "upvotes")


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("answer_to_question", "upvotes")


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Answer, AnswerAdmin)
