# from django.urls import path

# from cats.views import cat_list

# urlpatterns = [
#    path('cats/', cat_list),
# ]

# from cats.views import APICat

# urlpatterns = [
#     path('cats/', APICat.as_view()),
# ] 

# from cats.views import CatList, CatDetail

# urlpatterns = [
#     path('cats/', CatList.as_view()),
#     path('cats/<int:pk>/', CatDetail.as_view()),
# ] 

# from cats.views import CatViewSet

# urlpatterns = [
#     path('cats/', CatViewSet.as_view({'get': 'list'})),
# ] 
# from rest_framework.routers import SimpleRouter

# from django.urls import include, path

# from cats.views import CatViewSet

# # Создаётся роутер
# router = SimpleRouter()
# # Вызываем метод .register с нужными параметрами
# router.register('cats', CatViewSet)
# # В роутере можно зарегистрировать любое количество пар "URL, viewset":
# # например
# # router.register('owners', OwnerViewSet)
# # Но нам это пока не нужно

# urlpatterns = [
#     # Все зарегистрированные в router пути доступны в router.urls
#     # Включим их в головной urls.py
#     path('', include(router.urls)),
# ] 

from django.urls import include, path

from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, OwnerViewSet, LightCatViewSet
from rest_framework.authtoken import views


router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)
router.register(r'mycats', LightCatViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('api-token-auth/', views.obtain_auth_token),
    # Djoser создаст набор необходимых эндпоинтов.
    # базовые, для управления пользователями в Django:
    path('auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('auth/', include('djoser.urls.jwt')),
]