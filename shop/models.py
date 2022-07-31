from django.db import models
import datetime

class Product(models.Model):
    product_id=models.BigAutoField(primary_key=True)
    product_name=models.CharField(max_length=300)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField("Date",default=datetime.date.today)

    def __str__(self) -> str:
        return self.product_name
