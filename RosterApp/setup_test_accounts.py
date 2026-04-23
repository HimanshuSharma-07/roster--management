import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roster_system.settings')
django.setup()

from django.contrib.auth.models import User
from core.models import Employee

def setup_accounts():
    print("--- Setting up Test Accounts ---")
    
    # 1. Superuser
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Created Superuser: admin / admin123")
    else:
        u = User.objects.get(username='admin')
        u.set_password('admin123')
        u.save()
        print("Updated Superuser: admin / admin123")

    # 2. WFM
    wfm_user, _ = User.objects.get_or_create(username='wfm')
    wfm_user.set_password('admin123')
    wfm_user.save()
    Employee.objects.update_or_create(
        user=wfm_user,
        defaults={
            'emp_id': 'WFM001',
            'name': 'Main WFM Admin',
            'role_type': 'WFM',
            'pms': 'PMS-Main',
            'manager': 'System'
        }
    )
    print("Created WFM: wfm / admin123")

    # 3. Supervisor
    sup_user, _ = User.objects.get_or_create(username='sup')
    sup_user.set_password('sup123')
    sup_user.save()
    Employee.objects.update_or_create(
        user=sup_user,
        defaults={
            'emp_id': 'SUP001',
            'name': 'John Supervisor',
            'role_type': 'Supervisor',
            'pms': 'PMS-Sup',
            'manager': 'Main WFM Admin'
        }
    )
    print("Created Supervisor: sup / sup123")

    # 4. Agent (Guest)
    agent_user, _ = User.objects.get_or_create(username='agent_guest')
    agent_user.set_password('pass123')
    agent_user.save()
    Employee.objects.update_or_create(
        user=agent_user,
        defaults={
            'emp_id': 'GUEST',
            'name': 'Guest Agent',
            'role_type': 'Agent',
            'pms': 'PMS-Guest',
            'manager': 'John Supervisor'
        }
    )
    print("Created Agent: agent_guest / pass123")
    print("--------------------------------")

if __name__ == "__main__":
    setup_accounts()
