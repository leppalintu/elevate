from django.contrib import admin
from import_export.resources import ModelResource

from .models import Country
from import_export.admin import ImportExportModelAdmin
from .models import Country


# username: student
# password: student123

# https://www.youtube.com/watch?v=hmgYDbBZGiw
# https://stackoverflow.com/questions/68164249/how-to-combine-django-import-export-with-list-display-in-admin-py
class CountryModelResource(ModelResource):
    class Meta:
        model = Country


class CountryModelAdmin(ImportExportModelAdmin):
    list_display = ('name', 'region', 'capital', 'timezone', )
    resource_class = CountryModelResource
    list_filter = ('region', 'timezone', )
    ordering = ('name', )


# Register your models here.
admin.site.register(Country, CountryModelAdmin)
