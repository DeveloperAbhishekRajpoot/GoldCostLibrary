from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email_id = models.EmailField()
    seat_number = models.CharField(max_length=10)
    joining_date = models.DateField()
    monthly_fee = models.DecimalField(max_digits=10, decimal_places=2)
    profile_image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name