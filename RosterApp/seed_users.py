import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roster_system.settings')
django.setup()

from django.contrib.auth.models import User
from core.models import Employee

def create_user_and_employee(username, password, emp_id, name, role, pms=None, manager=None):
    if not User.objects.filter(username=username).exists():
        user = User.objects.create_user(username=username, password=password)
        Employee.objects.create(
            user=user,
            emp_id=emp_id,
            name=name,
            role_type=role,
            pms=pms,
            manager=manager
        )
        print(f"Created {role}: {username}")
    else:
        print(f"User {username} already exists.")

if __name__ == "__main__":
    # Create WFM
    create_user_and_employee('wfm', 'admin123', 'WFM001', 'Admin WFM', 'WFM', 'PMS-01', 'Senior Mgr')
    
    # Create Supervisor
    create_user_and_employee('sup', 'sup123', 'SUP001', 'John Supervisor', 'Supervisor', 'PMS-02', 'Admin WFM')
    
    # Create some Agents
    create_user_and_employee('agent1', 'agent123', 'AGT001', 'Alice Agent', 'Agent', 'PMS-03', 'John Supervisor')
    create_user_and_employee('agent2', 'agent123', 'AGT002', 'Bob Agent', 'Agent', 'PMS-03', 'John Supervisor')

    # Create a Superuser for Django Admin
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Created Superuser: admin")
