from django.db import models

class Records(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Record'
        ordering = ('id',)

    def __str__(self):
        return f"{self.last_name},{self.first_name} "
