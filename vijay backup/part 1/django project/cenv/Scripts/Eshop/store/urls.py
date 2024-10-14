from django.contrib import admin
from django.urls import path
# from .views.home import Index, store
# from .views.signup import Signup
# from .views.login import Login, logout
# from .views.cart import cart
# from .views.checkout import CheckOut
# from .views.order import OrderView
from .middlewares.auth import auth_middleware

# Create your views here.
urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store, name='store'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='order'),

]
