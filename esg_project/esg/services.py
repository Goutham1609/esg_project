from .models import Company, BusinessUnit, Metric, MetricValue

def get_company_metrics_summary(company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist:
        return None

    units = BusinessUnit.objects.filter(company_id=company_id)
    metrics = Metric.objects.filter(business_unit__in=units)

    metric_values = MetricValue.objects.filter(metric__in=metrics).select_related('metric')

    summary = {
        "company_id": company_id,
        "company_name": company.name,
        "metric_count": metrics.count(),
        "metric_total_value": sum([mv.value or 0 for mv in metric_values]),
        "metrics": []
    }

    for mv in metric_values:
        summary["metrics"].append({
            "metric_id": mv.metric.id,
            "metric_name": mv.metric.name,
            "category": mv.metric.get_category_display() if hasattr(mv.metric, "get_category_display") else str(mv.metric.category),
            "year": mv.year,
            "value": mv.value,
            "unit": mv.unit
        })

    return summary
