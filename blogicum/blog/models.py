from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


class BaseBlogModel(models.Model):
    is_published = models.BooleanField(
        verbose_name='Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию',
    )
    created_at = models.BooleanField(
        verbose_name= 'Добавлено',
        auto_now_add = True,
    )

    class Meta:
        abstract = True
        ordering = ('created_at',)



class Post(BaseBlogModel):
    text = models.TextField()
    title = models.CharField(max_length = settings.MAXLENGTH, blank = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_namee_plural = 'Посты'

class Comment(BaseBlogModel):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_namee_plural = 'Комментарии'
