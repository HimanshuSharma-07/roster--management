import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roster_system.settings')
django.setup()

from core.models import Employee, Roster

print(f"Total Employees: {Employee.objects.count()}")
print(f"Total Roster Entries: {Roster.objects.count()}")
print(f"Unique Dates: {Roster.objects.values('date').distinct().count()}")

# Show a few dates to see range
dates = list(Roster.objects.values_list('date', flat=True).distinct().order_by('date'))
if dates:
    print(f"Date Range: {dates[0]} to {dates[-1]}")
