from celery_worker import celery_app

@celery_app.task
def weekly_compliance_scan():
    """Proactive Sunday compliance check for all users."""
    # TODO: query all active businesses, run compliance checks, send alerts
    print("Running weekly compliance scan...")