from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company_name = models.CharField(max_length=255)
    website = models.URLField()
    industry = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name