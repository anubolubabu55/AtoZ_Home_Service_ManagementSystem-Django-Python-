from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('index',views.index,name='index'),
    path('login', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    #path('update_profile',views.update_profile,name='update_profile'),
    #path('admin_password_reset',views.admin_password_reset,name='admin_password_reset'),
    #path('add_category',views.add_category,name='add_category'),
    #path('edit_category',views.edit_category,name='edit_category'),
    #path('delete_category',views.delete_category,name='delete_category'),
    #path('add_area',views.add_area,name='add_area'),
    #path('edit_area',views.edit_area,name='edit_area'),
    #path('delete_area',views.delete_area,name='delete_area'),
    #path('add_partner',views.add_partner,name='add_partner'),
    #path('delete_partner',views.delete_partner,name='delete_partner'),
    #path('validity_extension',views.validity_extension,name='validity_extension'),
    #path('view_received_bookings',views.view_received_bookings,name='view_received_bookings'),
    #path('view_confirmed_bookings',views.view_confirmed_bookings,name='view_confirmed_bookings'),
    #path('view_completed_bookings',views.view_completed_bookings,name='view_completed_bookings'),
    #path('reviews',views.reviews,name='reviews'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)