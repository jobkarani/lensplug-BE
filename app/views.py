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
def vehicleLights(request):
    if request.method == "GET":
        products = VehicleLights.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = VehicleLightsSerializer(result_page, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def getVehicleLightsByCategory(request, vehicle_category_id):
    if request.method == "GET":
        vehicle_lights_category = get_object_or_404(VehicleLightsCategory, id=vehicle_category_id)
        vehiclelights = VehicleLights.objects.filter(category=vehicle_lights_category)
        serializer =VehicleLightsCategorySerializer(vehiclelights, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def accessories(request):
    if request.method == "GET":
        products = Accessories.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = AccessoriesSerializer(result_page, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def getAccessoriesByCategory(request, accessories_category_id):
    if request.method == "GET":
        accessories_category = get_object_or_404(AccessoriesCategory, id=accessories_category_id)
        accessories = Accessories.objects.filter(category=accessories_category)
        serializer =AccessoriesCategorySerializer(accessories, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def bulbs(request):
    if request.method == "GET":
        products = Bulbs.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = BulbsSerializer(result_page, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def getBulbsByCategory(request, bulbs_category_id):
    if request.method == "GET":
        bulbs_category = get_object_or_404(BulbsCategory, id=bulbs_category_id)
        bulbs = Bulbs.objects.filter(category=bulbs_category)
        serializer =BulbsCategorySerializer(bulbs, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def grilles(request):
    if request.method == "GET":
        products = Grilles.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = GrillesSerializer(result_page, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def getGrillesByCategory(request, grilles_category_id):
    if request.method == "GET":
        grilles_category = get_object_or_404(GrillesCategory, id=grilles_category_id)
        grilles = Grilles.objects.filter(category=grilles_category)
        serializer =GrillesCategorySerializer(grilles, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def bumperAndParts(request):
    if request.method == "GET":
        products = BumperAndParts.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = BumperAndPartsSerializer(result_page, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def getBumperAndPartsByCategory(request, bumper_category_id):
    if request.method == "GET":
        bumper_category = get_object_or_404(BumperAndPartsCategory, id=bumper_category_id)
        bumper = BumperAndParts.objects.filter(category=bumper_category)
        serializer =BumperAndPartsCategorySerializer(bumper, many=True)
        return Response(serializer.data)