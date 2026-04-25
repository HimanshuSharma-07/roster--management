import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roster_system.settings')
django.setup()

from core.models import Employee
for e in Employee.objects.all():
    print(f"ID: {e.emp_id}, Role: {e.role_type}")
