from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('person',views.person,name='person'),
    path('index',views.index,name='index'),
    path('about',views.about,name='about'),
    path('services',views.services, name='services'),
    path('find_professionals',views.find_professionls,name='find_professionals'),
    path('feedback',views.feedback,name='feedback'),
    path('login', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('user_registration',views.user_registration,name='user_registration'),
    path('contact',views.contact,name='contact'),
    path('user_add_more',views.user_add_more,name='user_add_more'),
    path('book/<int:id>',views.book,name="book"),
    path('cancel/<int:id>',views.cancel,name="cancel"),
    path('feedback/<int:id>',views.feedback,name="feedback"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)