from django.db import models

    
class OTPsave(models.Model):
    OTP = models.CharField(max_length = 5)
    
    
    class Meta:
        db_table = "OTPsave"