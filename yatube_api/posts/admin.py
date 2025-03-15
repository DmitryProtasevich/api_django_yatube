from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.safestring import mark_safe

from .models import Post, Group, Comment, Follow, User

admin.site.unregister(User)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    @admin.display(description='Кол-во постов у пользователя')
    def posts_count(self, obj):
        return obj.posts.count()

    @admin.display(description='Кол-во подписчиков у пользователя')
    def followers_count(self, obj):
        return obj.follower.count()

    @admin.display(description='Кол-во подписок у пользователя')
    def following_count(self, obj):
        return obj.following.count()
    list_display = BaseUserAdmin.list_display + (
        'posts_count', 'followers_count', 'following_count'
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'text', 'pub_date', 'author', 'image_preview', 'group'
    )
    search_fields = ('text', 'author__username', 'group__title')
    list_filter = ('pub_date', 'group', 'author')

    @admin.display(description='Изображение')
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="80" height="60">'
            )
        return ''


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'description')
    list_display_links = ('title',)
    search_fields = ('title', 'slug')
    list_filter = ('description',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'post', 'created')
    list_display_links = ('text',)
    search_fields = ('author', 'text')
    list_filter = ('created', 'author')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'following')
    list_display_links = ('user',)
    search_fields = ('user', 'following')
    list_filter = ('user', 'following')
