from django.urls import path
from . import views

urlpatterns = [
    path('', views.home.as_view(), name="home"),
    path('livre/<int:idp>/detail', views.detail.as_view(), name="detail"),
    path('cart/add/<int:livre_id>/', views.cart_add, name='cart_add'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/remove/<int:livre_id>/', views.cart_remove, name='cart_remove'),
    path('connexion/', views.signin, name="signin"),
    path('inscription/', views.signup, name="signup"),
    path('deconnexion', views.signout, name="signout"),
    path('profil/', views.profil, name="profil"),
    path('rechercher/', views.rechercher, name="rechercher"),
    path('emprunter/', views.emprunt, name='emprunt'),
    path('emprunts/', views.Emprunts, name="emprunts"),
]

