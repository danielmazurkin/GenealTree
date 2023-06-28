from django.contrib import admin
from pdf_reports.models import TaskPDFReport
from peoples.models import People
from pdf_reports.broker_logic.sender import SenderToServicePDF


@admin.register(TaskPDFReport)
class TaskPDFReportAdmin(admin.ModelAdmin):
    """Регистрация задачи с PDF задачей."""
    list_display = ('people', )
    exclude = ('owner_user', )
    readonly_fields = ('status', )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Переопределяем данные в выпадающем списке внешнего ключа."""
        if db_field.name == "people":
            kwargs["queryset"] = People.objects.filter(owner_user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        """Переопределяем метод чтобы администратору отображались только его данные."""
        qs = super().get_queryset(request)
        return qs.filter(owner_user=request.user)

    def save_model(self, request, obj, form, change):
        """Переопределяем save_model чтобы сохранить в rabbit mq."""
        obj.owner_user = request.user
        obj.save()

        with SenderToServicePDF(priority=10) as conn:
            conn.send_data('test sending..')
