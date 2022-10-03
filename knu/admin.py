from django.contrib import admin

# Register your models here.

from .models import Area
from .models import Select
from django.contrib import admin
from .models import Fact, Value, Unit, Dimension
admin.site.register(Dimension)
admin.site.register(Fact)
admin.site.register(Unit)




class FactInline(admin.TabularInline):
    model = Fact
    extra = 3

class SelectInline(admin.TabularInline):
    model = Select
    extra = 3


class AreaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['area_text', 'description']}),
    ]
    inlines = [FactInline]

class ValueAdmin(admin.ModelAdmin):
        fieldsets = [
            (None, {'fields': ['fact', 'value', 'unit', 'source']}),
        ]
        inlines = [SelectInline]


admin.site.register(Area, AreaAdmin)
admin.site.register(Value, ValueAdmin)
