from celery import Celery
from app.config import settings

celery_app = Celery("finity", broker=settings.REDIS_URL, backend=settings.REDIS_URL)
celery_app.conf.timezone = "Asia/Kolkata"

# Import tasks
from app.task.compliance_scan import weekly_compliance_scan

celery_app.conf.beat_schedule = {
    "weekly-compliance-scan": {
        "task": "app.task.compliance_scan.weekly_compliance_scan",
        "schedule": 604800.0,  # every Sunday (7 days in seconds)
    }
}