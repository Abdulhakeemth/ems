from __future__ import unicode_literals
from django.db import models
from main.models import BaseModel
from django.utils.translation import ugettext_lazy as _
from versatileimagefield.fields import VersatileImageField
from account.models import Account,District

class Event(BaseModel):    
    event_name = models.CharField(max_length=128,null=True,blank=True)
    venue = models.CharField(max_length=128,null=True,blank=True)
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()
    end_time = models.DateTimeField()
    reg_end_time = models.DateTimeField()
    reg_fee = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'Event'
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
        ordering = ('-pk',)

    def __str__(self):
        return str(self.title)

class Banner(BaseModel):
    title = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    description = models.TextField()
    small_image = VersatileImageField(
        'Image',
        upload_to='images/event/banner/small/',
        # width_field='width',
        # height_field='height'
    )
    large_image = VersatileImageField(
        'Image',
        upload_to='images/event/banner/large/',
        # width_field='width',
        # height_field='height'
    )
    order= models.IntegerField(default=0)

    class Meta:
        db_table = 'Banner'
        verbose_name = _('Banner')
        verbose_name_plural = _('Banners')
        ordering = ('-pk',)

    def __str__(self):
        return str(self.title)    

class EventTicket(BaseModel):    
    event = models.ForeignKey(Event, on_delete=models.CASCADE,blank=True,null=True)
    PAYMENT_STATUS =(
        ('Paid', 'Paid'),
        ('Cancel', 'Cancel'),
        ('Pending', 'Pending')
        )
    payment_status = models.CharField(max_length=14,null=False,blank=False)
    attandance = models.CharField(max_length=14)
    email = models.EmailField(verbose_name="email", max_length=60,)
    phone = models.PositiveIntegerField()
    full_name = models.CharField(max_length=140)
    phone_code = models.CharField(max_length=30,default="91")
    address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        db_table = 'Event_Ticket'
        verbose_name = _('Event Ticket')
        verbose_name_plural = _('Event Tickets')
        ordering = ('-pk',)

    def __str__(self):
        return str(self.full_name)