from django.urls import path
from AdminModule import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('index',views.index,name='index'),
    path('login', auth_views.LoginView.as_view(template_name="AdminModule/login.html"), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name="AdminModule/logout.html"), name='logout'),

    #path('update_profile',views.update_profile,name='update_profile'),
    #path('admin_password_reset',views.admin_password_reset,name='admin_password_reset'),
    path('add_category',views.add_category,name='add_category'),
    path('edit_category/<int:id>',views.edit_category,name='edit_category'),
    path('view_category',views.view_category,name='view_category'),
    path('delete_category/<int:id>',views.delete_category,name='delete_category'),
    path('add_area',views.add_area,name='add_area'),
    path('edit_area/<int:id>',views.edit_area,name='edit_area'),
    path('delete_area/<int:id>',views.delete_area,name='delete_area'),
    path('view_area',views.view_area,name='view_area'),
    path('add_partner',views.add_partner,name='add_partner'),
    path('partner_add_more',views.partner_add_more,name='partner_add_more'),
    path('view_partner',views.view_partner,name='view_partner'),

    path('delete_partner/<int:id>',views.delete_partner,name='delete_partner'),
    path('validity_extension/<int:id>',views.validity_extension,name='validity_extension'),
    path('view_received_bookings',views.view_received_bookings,name='view_received_bookings'),
    path('view_confirmed_bookings',views.view_confirmed_bookings,name='view_confirmed_bookings'),
    path('view_completed_bookings',views.view_completed_bookings,name='view_completed_bookings'),
    path('reviews',views.reviews,name='reviews'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)