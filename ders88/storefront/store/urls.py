from django.urls import path, include
from rest_framework_nested import routers
from . import views
from pprint import pprint

router = routers.DefaultRouter()
router.register('products',views.ProductViewSet,basename='products')
router.register('collections',views.CollectionViewSet)

products_router = routers.NestedDefaultRouter(router,'products',lookup='product')
products_router.register('reviews',views.ReviewViewSet,basename='product-reviews') # product-list-reviews , product-detail-reveiws

urlpatterns = router.urls + products_router.urls

# urlpatterns = [
#     path('',include(router.urls))
#     # path('products/',views.ProductList.as_view()),
#     # path('products/<int:pk>/',views.ProductDetail.as_view()),
#     # path('collections/',views.CollectionList.as_view()),
#     # path('collections/<int:pk>/',views.CollectionDetail.as_view(),name='collection-detail'),
# ]
