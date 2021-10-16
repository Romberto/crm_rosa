from django.contrib import admin

from manager.models import CaseModel, CommentModel, StatusModel


@admin.register(CaseModel)
class AdminCase(admin.ModelAdmin):
    list_display = ('farmerName', 'companyName', 'phone')


admin.site.register(CommentModel)
admin.site.register(StatusModel)
