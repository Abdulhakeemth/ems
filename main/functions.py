import string
import random
from django.http import HttpResponse
from decimal import Decimal
import urllib.request
import urllib.parse


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def generate_unique_id(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_form_errors(args,formset=False):
    message = ''
    if not formset:
        for field in args:
            if field.errors:
                message += field.errors  + "|"
        for err in args.non_field_errors():
            message += str(err) + "|"

    elif formset:
        for form in args:
            for field in form:
                if field.errors:
                    message +=field.errors + "|"
            for err in form.non_field_errors():
                message += str(err) + "|"
    return message[:-1]


def get_auto_id(model):
    auto_id = 1
    latest_auto_id =  model.objects.all().order_by("-auto_id")[:1]
    if latest_auto_id:
        for auto in latest_auto_id:
            auto_id = auto.auto_id + 1
    return auto_id

def get_ref_id(model):
    ref_id = 1
    latest_ref_id = model.objects.all().order_by("-ref_id")[:1]
    
    if latest_ref_id:
        for ref in latest_ref_id:
            ref_id = ref.ref_id + 1       
    return ref_id


def get_pk_id(model):
    pk_id = 1
    latest_pk_id =  model.objects.all().order_by("-date_joined")[:1]
    if latest_pk_id:
        for auto in latest_pk_id:
            pk_id = auto.pk + 1
    return pk_id



def get_timezone(request):
    if "set_user_timezone" in request.session:
        user_time_zone = request.session['set_user_timezone']
    else:
        user_time_zone = "Asia/Kolkata"
    return user_time_zone
 
