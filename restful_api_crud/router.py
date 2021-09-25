from employee_api.viewsets import EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', EmployeeViewSet)

# localhost:port_number/api/employee/5
# GET, POST, PUT, DELETE
# list, retrieve
