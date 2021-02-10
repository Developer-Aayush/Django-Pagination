from django.db import models


class paginationData(models.Model):
    data_serial_number = models.CharField(max_length=200, null=True)
    data_name = models.CharField(max_length=200, null=True)
