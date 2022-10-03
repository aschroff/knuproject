from django.db import models

# Create your models here.


class Area(models.Model):
    area_text = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.area_text


class Fact(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    fact_text = models.CharField(max_length=40)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.area.area_text + '--' + self.fact_text


class Dimension(models.Model):
    dimension_text = models.CharField(max_length=20)

    def __str__(self):
        return self.dimension_text


class Unit(models.Model):
    unit_text = models.CharField(max_length=5)

    def __str__(self):
        return self.unit_text


class Value(models.Model):
    fact = models.ForeignKey(Fact, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True, null=True)
    value = models.CharField(max_length=20)
    source = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.fact.fact_text + ' (' + self.source + ')'


class Select(models.Model):
    select_txt = models.CharField(max_length=20)
    value = models.ForeignKey(Value, on_delete=models.CASCADE)
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)

    def __str__(self):
        return self.dimension.dimension_text + ' = ' + self.select_txt




