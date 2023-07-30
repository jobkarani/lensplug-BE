from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
# from simple_mail.mail import send_mail

from app.models import *
from .serializer import *
from .pagination import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


# Create your views here

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


@api_view(['GET',])
def weddingCakes(request):
    if request.method == "GET":
        products = WeddingCakes.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = WeddingCakesSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def weddingCakeDetails(request, product_id):
    if request.method == "GET":
        product= WeddingCakes.objects.filter(id = product_id)
        serializer = WeddingCakesSerializer(product, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def babyShowerCakes(request):
    if request.method == "GET":
        products = BabyShowerCakes.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = BabyShowerCakesSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def babyShowerCakesDetails(request, product_id):
    if request.method == "GET":
        product= BabyShowerCakes.objects.filter(id = product_id)
        serializer = BabyShowerCakesSerializer(product, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def bridalShowerCakes(request):
    if request.method == "GET":
        products = BridalShowerCakes.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = BridalShowerCakesSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def bridalShowerCakesDetails(request, product_id):
    if request.method == "GET":
        product= BridalShowerCakes.objects.filter(id = product_id)
        serializer = BridalShowerCakesSerializer(product, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def christmasCakes(request):
    if request.method == "GET":
        products = ChristmasCakes.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = ChristmasCakesSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def christmasCakesDetails(request, product_id):
    if request.method == "GET":
        product= ChristmasCakes.objects.filter(id = product_id)
        serializer = ChristmasCakesSerializer(product, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def easterCakes(request):
    if request.method == "GET":
        products = EasterCakes.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = EasterCakesSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def easterCakesDetails(request, product_id):
    if request.method == "GET":
        product= EasterCakes.objects.filter(id = product_id)
        serializer = EasterCakesSerializer(product, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def fathersDayCakes(request):
    if request.method == "GET":
        products = FathersDayCakes.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = FathersDayCakesSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def fathersDayCakesDetails(request, product_id):
    if request.method == "GET":
        product= FathersDayCakes.objects.filter(id = product_id)
        serializer = FathersDayCakesSerializer(product, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def mothersDayCakes(request):
    if request.method == "GET":
        products = MothersDayCakes.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = MothersDayCakesSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def mothersDayCakesDetails(request, product_id):
    if request.method == "GET":
        product= MothersDayCakes.objects.filter(id = product_id)
        serializer = MothersDayCakesSerializer(product, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def graduationCakes(request):
    if request.method == "GET":
        products = GraduationCakes.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = GraduationCakesSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def graduationCakesDetails(request, product_id):
    if request.method == "GET":
        product= GraduationCakes.objects.filter(id = product_id)
        serializer = GraduationCakesSerializer(product, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def valentinesCakes(request):
    if request.method == "GET":
        products = ValentinesCakes.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = ValentinesCakesSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def valentinesCakesDetails(request, product_id):
    if request.method == "GET":
        product= ValentinesCakes.objects.filter(id = product_id)
        serializer = ValentinesCakesSerializer(product, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def ruracioCakes(request):
    if request.method == "GET":
        products = RuracioCakes.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = RuracioCakesSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def ruracioCakesDetails(request, product_id):
    if request.method == "GET":
        product= RuracioCakes.objects.filter(id = product_id)
        serializer = RuracioCakesSerializer(product, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def engagementCakes(request):
    if request.method == "GET":
        products = EngagementCakes.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = EngagementCakesSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def engagementCakesDetails(request, product_id):
    if request.method == "GET":
        product= EngagementCakes.objects.filter(id = product_id)
        serializer = EngagementCakesSerializer(product, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def coporateCakes(request):
    if request.method == "GET":
        products = CoporateCakes.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = CoporateCakesSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def coporateCakesDetails(request, product_id):
    if request.method == "GET":
        product= CoporateCakes.objects.filter(id = product_id)
        serializer = CoporateCakesSerializer(product, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def anniversaryCakes(request):
    if request.method == "GET":
        products = AnniversaryCakes.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = AnniversaryCakesSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def anniversaryCakesDetails(request, product_id):
    if request.method == "GET":
        product= AnniversaryCakes.objects.filter(id = product_id)
        serializer = AnniversaryCakesSerializer(product, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def baptismalCakes(request):
    if request.method == "GET":
        products = BaptismalCakes.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = BaptismalCakesSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def baptismalCakesDetails(request, product_id):
    if request.method == "GET":
        product= BaptismalCakes.objects.filter(id = product_id)
        serializer = BaptismalCakesSerializer(product, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def christeningCakes(request):
    if request.method == "GET":
        products = ChristeningCakes.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = ChristeningCakesSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def christeningCakesDetails(request, product_id):
    if request.method == "GET":
        product= ChristeningCakes.objects.filter(id = product_id)
        serializer = ChristeningCakesSerializer(product, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def birthdayCakes(request):
    if request.method == "GET":
        products = BirthdayCakes.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = BirthdayCakesSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def birthdayCakesDetails(request, product_id):
    if request.method == "GET":
        product= BirthdayCakes.objects.filter(id = product_id)
        serializer = BirthdayCakesSerializer(product, many=True)
        return Response(serializer.data)



@api_view(['GET'])
def get_blogs(request):
    if request.method == "GET":
        blogs = Blogs.objects.all()
        serializer = BlogsSerializer(blogs, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def api_blogscategories(request):
    if request.method == "GET":
        blogcategories = BlogCategory.objects.all()
        serializer = BlogCategorySerializer(blogcategories, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getBlogDetails(request, blog_id):
    if request.method == "GET":
        blogs= Blogs.objects.filter(id = blog_id)
        serializer = BlogsSerializer(blogs, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def getBlogByCategory(request, blogcategory_id):
    if request.method == "GET":
        blogcategory = get_object_or_404(BlogCategory, id=blogcategory_id)
        blogs = Blogs.objects.filter(blog_category=blogcategory)
        serializer =BlogsSerializer(blogs, many=True)
        return Response(serializer.data)