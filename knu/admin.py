from django.contrib import admin

# Register your models here.

from .models import Area
from .models import Select
from django.contrib import admin
from .models import Fact, Value, Unit, Dimension, Scenario, Impact, Calculation, Eval, SelectEval, Task
admin.site.register(Dimension)
admin.site.register(Fact)
admin.site.register(Unit)



class ImpactInline(admin.TabularInline):
    model = Impact
    extra = 3

class ScenarioMother(admin.TabularInline):
    model = Scenario.inheritance.through
    fk_name = 'to_scenario'


class ScenarioAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['scenario_text', 'description']}),
    ]
    inlines = [ScenarioMother, ImpactInline]


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


class SelectEvalInline(admin.TabularInline):
    model = SelectEval
    extra = 3

class EvalAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['eval_text', 'description', 'scenario', 'task']}),
    ]
    inlines = [SelectEvalInline]

class CalculationInline(admin.TabularInline):
    model = Calculation
    extra = 3

class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['task_text', 'description']}),
    ]
    inlines = [CalculationInline]


admin.site.register(Task, TaskAdmin)
admin.site.register(Eval, EvalAdmin)
admin.site.register(Scenario, ScenarioAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Value, ValueAdmin)
