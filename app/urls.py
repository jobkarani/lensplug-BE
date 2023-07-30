from django.urls import path
from app import views

urlpatterns = [
    path('blogs/', views.get_blogs, name='blogs'),
    path('blogcategories/', views.api_blogscategories, name='apiBlogCategories' ),
    path('getBlogDetails/<int:blog_id>/', views.getBlogDetails, name='Blog Details' ),
    path('categoryblogs/<int:blogcategory_id>/', views.getBlogByCategory, name='apiCategoryblogs' ),

    path('weddingcakes/', views.weddingCakes, name='weddingcakes' ),
    path('weddingcakedetails/<int:product_id>/', views.weddingCakeDetails, name='weddingCakeDetails' ),

    path('birthdaycakes/', views.birthdayCakes, name='birthdayCakes' ),
    path('birthdaycakedetails/<int:product_id>/', views.birthdayCakesDetails, name='birthdayCakesDetails' ),

    path('babyShowerCakes/', views.babyShowerCakes, name='babyShowerCakes' ),
    path('babyShowerCakesDetails/<int:product_id>/', views.babyShowerCakesDetails, name='babyShowerCakesDetails' ),

    path('bridalShowerCakes/', views.bridalShowerCakes, name='bridalShowerCakes' ),
    path('bridalShowerCakesDetails/<int:product_id>/', views.bridalShowerCakesDetails, name='bridalShowerCakesDetails' ),

    path('christmasCakes/', views.christmasCakes, name='christmasCakes' ),
    path('christmasCakesDetails/<int:product_id>/', views.christmasCakesDetails, name='christmasCakesDetails' ),



    path('easterCakes/', views.easterCakes, name='easterCakes' ),
    path('easterCakesDetails/<int:product_id>/', views.easterCakesDetails, name='easterCakesDetails' ),

    path('fathersDayCakes/', views.fathersDayCakes, name='fathersDayCakes' ),
    path('fathersDayCakesDetails/<int:product_id>/', views.fathersDayCakesDetails, name='fathersDayCakesDetails' ),

    path('mothersDayCakes/', views.mothersDayCakes, name='mothersDayCakes' ),
    path('mothersDayCakesDetails/<int:product_id>/', views.mothersDayCakesDetails, name='mothersDayCakesDetails' ),

    path('graduationCakes/', views.graduationCakes, name='graduationCakes' ),
    path('graduationCakesDetails/<int:product_id>/', views.graduationCakesDetails, name='graduationCakesDetails' ),

    path('valentinesCakes/', views.valentinesCakes, name='valentinesCakes' ),
    path('valentinesCakesDetails/<int:product_id>/', views.valentinesCakesDetails, name='valentinesCakesDetails' ),

    path('ruracioCakes/', views.ruracioCakes, name='ruracioCakes' ),
    path('ruracioCakesDetails/<int:product_id>/', views.ruracioCakesDetails, name='ruracioCakesDetails' ),

    path('engagementCakes/', views.engagementCakes, name='engagementCakes' ),
    path('engagementCakesDetails/<int:product_id>/', views.engagementCakesDetails, name='engagementCakesDetails' ),

    path('coporateCakes/', views.coporateCakes, name='coporateCakes' ),
    path('coporateCakesDetails/<int:product_id>/', views.coporateCakesDetails, name='coporateCakesDetails' ),

    path('anniversaryCakes/', views.anniversaryCakes, name='anniversaryCakes' ),
    path('anniversaryCakesDetails/<int:product_id>/', views.anniversaryCakesDetails, name='anniversaryCakesDetails' ),

    path('baptismalCakes/', views.baptismalCakes, name='baptismalCakes' ),
    path('baptismalCakesDetails/<int:product_id>/', views.baptismalCakesDetails, name='baptismalCakesDetails' ),

    path('christeningCakes/', views.christeningCakes, name='christeningCakes' ),
    path('christeningCakesDetails/<int:product_id>/', views.christeningCakesDetails, name='christeningCakesDetails' ),

]
