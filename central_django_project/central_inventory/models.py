from django.db import models
from django.contrib.auth.models import User

class base_model(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(
        User,
        related_name="%(class)s_createdby",
        on_delete=models.CASCADE,
        null=True,
    )
    updated_by = models.ForeignKey(
        User,
        related_name="%(class)s_updatedby",
        on_delete=models.CASCADE,
        null=True,
    )
    

class site(base_model):
    site_id  = models.IntegerField(primary_key=True)
    site_name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=False)
    zipcode = models.IntegerField(null=True)

    def __str__(self):
        return self.site_name

class order(base_model):
    order_id = models.IntegerField(primary_key=True)
    purchase_id = models.IntegerField(max_length=100, null=False)
    quantity = models.IntegerField(null=False)
    dev_type = models.CharField(max_length=100, null=False)
    order_status = (
        ('Pending','Pending'),
        ('In-Transit','In-Transit'),
        ('Delivered','Delivered')
    )
    order_status = models.CharField(max_length=100, choices=order_status)

class iap(base_model):
    serial_no  = models.IntegerField(primary_key=True)
    ip_address = models.CharField(max_length=100, null=False)
    mac_address = models.CharField(max_length=100, null=False)
    model = models.CharField(max_length=100, null=False)
    status = models.BooleanField()
    is_vc = models.BooleanField()
    site_id = models.ForeignKey(site, related_name='iappersite', on_delete=models.CASCADE)
    order_id = models.ForeignKey(order, related_name='iaporder', on_delete=models.CASCADE)

    def __str__(self):
        return self.serial_no

class switch(base_model):
    serial_no  = models.CharField(max_length=100, primary_key=True)
    ip_address = models.CharField(max_length=100, null=False)
    mac_address = models.CharField(max_length=100, null=False)
    model = models.CharField(max_length=100, null=False)
    status = models.BooleanField()
    site_id = models.ForeignKey(site, related_name='switchpersite', on_delete=models.CASCADE)
    order_id = models.ForeignKey(order, related_name='switchorder', on_delete=models.CASCADE)

    def __str__(self):
        return self.serial_no

   




