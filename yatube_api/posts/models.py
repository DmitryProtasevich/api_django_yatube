from django.contrib.auth import get_user_model
from django.db import models

from posts.constants import Constants

User = get_user_model()


class AbstractText(models.Model):
    text = models.TextField('Текст')

    class Meta:
        abstract = True

    def __str__(self):
        return (
            (self.text[:Constants.MAX_TITLE_LENGTH] + '...')
            if len(self.text) > Constants.MAX_TITLE_LENGTH else self.text
        )


class Group(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('Слаг', unique=True)
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return (
            (self.title[:Constants.MAX_TITLE_LENGTH] + '...')
            if len(self.title) > Constants.MAX_TITLE_LENGTH else self.title
        )


class Post(AbstractText):
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts',
        verbose_name='Автор поста'
    )
    image = models.ImageField(
        'Изображение', upload_to='posts/', null=True, blank=True
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True,
        verbose_name='Группа'
    )

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'
        ordering = ['-pub_date']


class Comment(AbstractText):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Автор комментария'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Пост'
    )
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created']


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following',
        verbose_name='Подписки'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.CheckConstraint(
                name='prevent_self_follow',
                check=~models.Q(user=models.F('following')),
            ),
            models.UniqueConstraint(
                name='unique_user_following',
                fields=['user', 'following']
            )
        ]

    def __str__(self):
        return f'{self.user} подписан на {self.following}'
