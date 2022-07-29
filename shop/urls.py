from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path('',views.index,name='ShopHome'),
    path('cart/',views.cart,name='cart'),
    path('about/',views.about,name='aboutus'),
    path('tracker/',views.track,name='tracker'),
    path('contact/',views.contact,name='contactus'),
    path('productview/',views.productView,name='productview'),
    path('checkout/',views.checkout,name='checkout'),
    path('pay/',views.pay,name='pay')
]