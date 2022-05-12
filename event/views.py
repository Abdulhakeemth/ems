
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *
from main.functions import get_auto_id
import json
from django.core.paginator import Paginator


@login_required(login_url='account:login')
def create_event(request):     
    user = request.user
    if user.is_admin:
        if request.method == "POST":
            form = EventForm(request.POST,request.FILES)
            if form.is_valid():
                form_data = form.save(commit=False)
                form_data.auto_id = get_auto_id(Event)
                form_data.save()
                response_data = {
                    "status" : "true",
                    "title" : "Success",
                    "reLoad" : "true",
                }
            else:
                response_data = {
                    "status" : "false",
                    "title" : "Form validation error",
                    "reLoad" : "false",
                }
            return HttpResponse(json.dumps(response_data),content_type='application/javascript')
        else:
            form = EventForm(request.POST)
            context = {
                "form" : form,
                "page_name":"create_event",     
            }
            return render(request, 'dashboard/event/create_event.html',context)
    else:
        context = {}
        return render(request, '403.html',context)



# # @login_required(login_url='account:login')
# # def class_list(request):     
# #     user = request.user
# #     if user.is_admin or user.is_teacher:
# #         class_detiles = ClassDetail.objects.filter(is_deleted=False).order_by('semester')
# #         paginator = Paginator(class_detiles, 25)
# #         page_number = request.GET.get('page')
# #         page_obj = paginator.get_page(page_number)
# #         context = {
# #             "page_obj" : page_obj,
# #             "page_name":"class_list",
# #         }
# #         return render(request, 'dashboard/class/list_class.html',context)
# #     else:
# #         context = {}
# #         return render(request, '403.html',context)

# # @login_required(login_url='account:login')
# # def view_class(request,pk):     
# #     user = request.user
# #     if user.is_admin or user.is_teacher:
# #         class_detail = ClassDetail.objects.get(pk=pk)
# #         students = Student.objects.filter(class_detail=class_detail).order_by("roll_no")
# #         context = {
# #             "class_detail" : class_detail,   
# #             "page_name": "view_class",
# #             "students":students
# #         }
# #         return render(request, 'dashboard/class/view_class.html',context)
# #     else:
# #         context = {}
# #         return render(request, '403.html', context)
    

# # @login_required(login_url='account:login')
# # def update_class(request,pk):     
# #     user = request.user
# #     if user.is_admin:
# #         if request.method == "POST":
# #             instance = ClassDetail.objects.get(pk=pk)
# #             form = ClassDetailForm(request.POST,request.FILES,instance=instance)
            
# #             if (form.is_valid()):
# #                 form.save()
# #                 response_data = {
# #                 "status" : "true",
# #                 "title" : "Success",
# #                 "reLoad" : "true",
# #                 }
# #             return HttpResponse(json.dumps(response_data),content_type='application/javascript')
# #         else:
# #             instance = ClassDetail.objects.get(pk=pk)
# #             form = ClassDetailForm(instance = instance)
# #             context = {
# #                 "form" : form,
# #                 "instance" :instance,
# #                 "page_name": "update_class",
 
# #             }
# #             return render(request, 'dashboard/class/update_class.html',context)
# #     else:
# #         context = {}
# #         return render(request, '403.html',context)


# # @login_required(login_url='account:login')
# # def delete_class(request,pk):     
# #     user = request.user
# #     if user.is_admin:
# #         ClassDetail.objects.get(pk=pk).delete()
# #         return redirect("class_detail:list")
# #     else:
# #         context = {}
# #         return render(request, '403.html',context)



