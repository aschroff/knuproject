from django.db import models

# Create your models here.


class Area(models.Model):
    area_text = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.area_text

class Keyfigure(models.Model):
    description = models.CharField(max_length=200)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    class Meta:
        abstract = True


class Fact(Keyfigure):
    fact_text = models.CharField(max_length=40)

    def __str__(self):
        return self.area.area_text + '--' + self.fact_text

class Task(models.Model):
    task_text = models.CharField(max_length=40)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.task_text

class Calculation(Keyfigure):
    calculation_text = models.CharField(max_length=40)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    def __str__(self):
        return self.area.area_text + '--' + self.calculation_text

class Dimension(models.Model):
    dimension_text = models.CharField(max_length=20)

    def __str__(self):
        return self.dimension_text


class Unit(models.Model):
    unit_text = models.CharField(max_length=5)

    def __str__(self):
        return self.unit_text

class Number(models.Model):
    fact = models.ForeignKey(Fact, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    value = models.CharField(max_length=20)
    class Meta:
        abstract = True


class Value(Number):
    source = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.fact.fact_text + ' (' + self.source + ')'

class Result(Number):
    method = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.fact.fact_text + ' (' + self.method + ')'

class Select(models.Model):
    select_txt = models.CharField(max_length=20)
    value = models.ForeignKey(Value, on_delete=models.CASCADE)
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)

    def __str__(self):
        return self.dimension.dimension_text + ' = ' + self.select_txt

class SelectResult(models.Model):
    select_txt = models.CharField(max_length=20)
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)

    def __str__(self):
        return self.dimension.dimension_text + ' = ' + self.select_txt

class Scenario(models.Model):
    scenario_text = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    inheritance = models.ManyToManyField('self', related_name='mothers', symmetrical=False)
    prio = models.CharField(max_length=1)
    def __str__(self):
        return self.scenario_text


class Impact(models.Model):
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='impacts')
    impact_text = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    value = models.ForeignKey(Value, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.impact_text


class Eval(models.Model):
    eval_text = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.eval_text

class SelectEval(models.Model):
    select_txt = models.CharField(max_length=20)
    eval = models.ForeignKey(Eval, on_delete=models.CASCADE)
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)
    def __str__(self):
        return self.dimension.dimension_text + ' = ' + self.select_txt

