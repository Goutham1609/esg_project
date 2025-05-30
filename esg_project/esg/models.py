from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    sector = models.CharField(max_length=100)
    reporting_period = models.CharField(max_length=20)  # e.g., "2024"

    def __str__(self):
        return self.name

class BusinessUnit(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    company = models.ForeignKey(Company, related_name='business_units', on_delete=models.CASCADE)
    function = models.CharField(max_length=255, help_text="What this unit does (e.g., Manufacturing, Sales)")

    def __str__(self):
        return f"{self.name} - {self.company.name}"

class Metric(models.Model):
    CATEGORY_CHOICES = [
        ('environmental', 'Environmental'),
        ('social', 'Social'),
        ('governance', 'Governance'),
    ]
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    year = models.IntegerField()
    value = models.FloatField()
    unit = models.CharField(max_length=50)
    business_unit = models.ForeignKey(BusinessUnit, related_name='metrics', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.year}"


class MetricValue(models.Model):
    business_unit = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE, related_name='metric_values')
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE, related_name='values')
    reporting_period = models.CharField(max_length=100)  # e.g., "2023", "Q1 2024"
    value = models.FloatField()
    unit = models.CharField(max_length=50, help_text="e.g., kWh, %, incidents")
    year = models.IntegerField()

    def __str__(self):
        return f"{self.metric.name} - {self.business_unit.name} ({self.reporting_period})"
    
