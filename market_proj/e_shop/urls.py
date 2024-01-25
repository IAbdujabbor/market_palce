from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path

from mysite import settings
from . import views
from .form import LoginForm

urlpatterns = [
    path('', views.main, name='main'),
    path('2/', views.product_list),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('create-product/', views.create_product, name='create_product'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm), name='login'),
    path('dashbord/', views.user_products, name='dashbord'),
    path('delete_item/<int:item_id>/', views.delete_items, name='delete_item'),
    path('item/<int:item_id>/edit/', views.edit_item, name='edit_item'),
    path('search/<str:q>',views.test_search, name='test_search'),
    path('items/', views.item_list, name='item_list'),
    #path('#',views.log_out, name='logout' )
    path("logout/", LogoutView.as_view(), name="logout"),
    path("chat_message/<int:item_pk>/" ,views.chatMessage,name='chatMessage'),
    path("inbox/", views.inbox, name='inbox'),
    path("detail/<int:pk>/", views.detail, name='detail'),
    path('category/<int:category_id>/', views.category_items, name='category_items'),



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
