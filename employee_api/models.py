from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=10)


# Create / Insert / Add - GET
# Retrieve / Fetch - POST
# Update / Edit - PUT
# Delete / Remove - DELETE
