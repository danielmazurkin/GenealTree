from django.contrib import admin, messages
from users.models import AllowedUser
from django.contrib.auth.models import User
from users.models import FriendLinkedTree
from django.conf import settings
from django.utils.html import format_html


@admin.register(AllowedUser)
class AllowedUserAdmin(admin.ModelAdmin):
    """Разрешенный пользователь."""
    fields = ('login_user', )

    def save_model(self, request, obj, form, change):
        """Переопределение сохранения модели для создания многопользовательского режима."""
        if user := User.objects.filter(username=obj.login_user).first():

            obj.user_linked = user
            obj.owner_user = request.user
            obj.save()

            FriendLinkedTree(
                user=request.user,
                user_linked=user,
            ).save()

        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, "Вы пытаетесь добавить пользователя, которого не существует.")

    def get_queryset(self, request):
        """Переопределяем метод чтобы администратору отображались только его данные."""
        qs = super().get_queryset(request)
        return qs.filter(owner_user=request.user)


@admin.register(FriendLinkedTree)
class FriendLinkedTreeAdmin(admin.ModelAdmin):
    """Дружественные ссылки."""

    readonly_fields = ('user', 'link_photos', 'link_bio', 'link_tree')
    exclude = 'user_linked',

    def has_add_permission(self, request):
        return False

    def link_photos(self, obj):
        return format_html(f"<a href='{settings.SITE_URL}/photo/{obj.user.pk}/'>"
                           f"Фотографии человека"
                           f"</a>")

    link_photos.short_description = 'Фотографии'

    def link_bio(self, obj):
        return format_html(f"<a href='{settings.SITE_URL}/bio/{obj.user.pk}/'>"
                           f"Биографии человека"
                           f"</a>")

    link_bio.short_description = 'Биографии'

    def link_tree(self, obj):
        return format_html(f"<a href='{settings.SITE_URL}/tree/{obj.user.pk}/'>"
                           f"Древо человека"
                           f"</a>")

    link_tree.short_description = 'Дерево'

    def get_queryset(self, request):
        """Переопределяем метод чтобы администратору отображались только его данные."""
        qs = super().get_queryset(request)
        return qs.filter(user_linked=request.user)
