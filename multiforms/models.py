from django.db import models
from accounts.models import User


class Comment(models.Model):
    comment = models.CharField(max_length=512)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)


class Question(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    comment = models.ForeignKey(Comment, null=True, on_delete=models.SET_NULL)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
    
    
class Answer(models.Model):
    answer_to_question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    answer_detail = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
