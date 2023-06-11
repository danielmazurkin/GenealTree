from peoples.models import People


class PeopleAdminMixin:
    """Миксин для внешнего ключа на человека."""
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Переопределяем данные в выпадающем списке внешнего ключа."""
        if db_field.name == "people":
            kwargs["queryset"] = People.objects.filter(owner_user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
