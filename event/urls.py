
from django.urls import path
from . import views

app_name = 'event'

urlpatterns = [

    path('event/', views.create_event, name="create"),
#     path('class-list/', views.class_list, name="list"),
#     path('view-class/<pk>/', views.view_class, name="view"),
#     path('update-class/<pk>/', views.update_class, name="update"),
#     path('delete-class/<pk>/', views.delete_class, name="delete"),

# #     path('create-ajax/', views.create_ajax, name="create_ajax"),

# #     path('user-autocomplete',views.user_autocomplete.as_view(),name='user_autocomplete',),
# #     path('investor-autocomplete',views.investor_autocomplete.as_view(),name='investor_autocomplete',),
# #     path('investor-group-autocomplete',views.investor_group_autocomplete.as_view(),name='investor_group_autocomplete',),
# #     path('saved-list-autocomplete',views.saved_list_autocomplete.as_view(),name='saved_list_autocomplete',),

# #     path('investor-list/', views.investor_list, name="investor_list"),
# #     path('investor-groups/', views.investor_groups, name="investor_groups"),

# #     path('investor-request-list/', views.investor_request_list, name="investor_request_list"),
    
# #     path('view-group/<pk>/', views.view_group, name="view_group"),
# #     path('update-group/<pk>/', views.update_group, name="update_group"),
# #     path('update-group-ajax/<pk>/', views.update_group_ajax, name="update_group_ajax"),

# #     path('view-investor/<pk>/', views.view_investor, name="view_investor"),
# #     path('update-investor/<pk>/', views.update_investor, name="update_investor"),
# #     path('update-investor-ajax/<pk>/', views.update_investor_ajax, name="update_investor_ajax"),
# #     path('add-director/', views.add_director, name="add_director"),
# #     path('remove-director/<pk>/', views.remove_director, name="remove_director"),
# #     path('add-director-autocomplete',views.add_director_autocomplete.as_view(),name='add_director_autocomplete',),
    
# #     path('add-investor/', views.add_to_saved_list, name="add_to_saved_list"),
# #     path('update-saved-list/<pk>/', views.update_saved_list, name="update_saved_list"),
# #     path('delete-investor/<pk>/', views.delete_saved_list, name="delete_saved_list"),
# #     path('investor-saved-list/', views.investor_saved_list, name="investor_saved_list"),

# #     path('test/', views.auto_investor_account, name="auto_investor_account"),
# #     path('reg/', views.register_with_id, name="register_with_id"),
# #     path('reg-data/', views.register_with_id_data, name="register_with_id_data"),
# #     path('otp-verification/', views.otp_verification, name="otp_verification"),

]

