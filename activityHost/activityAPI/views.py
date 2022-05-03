from calendar import weekday
from tkinter.messagebox import RETRY
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from psycopg2 import Date
# from rest_framework import viewsets
from .serializers import MasterSerializer
from .models import Master
# from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from datetime import date, datetime, timedelta

today = datetime.now().date()

if date.today().weekday() == 0:
    this_week = datetime.now() + timedelta(days=5)

if date.today().weekday() == 1:
    this_week = datetime.now() + timedelta(days=4)

if date.today().weekday() == 2:
    this_week = datetime.now() + timedelta(days=3)

if date.today().weekday() == 3:
    this_week = datetime.now() + timedelta(days=2)

if date.today().weekday() == 4:
    this_week = datetime.now() + timedelta(days=1)

if date.today().weekday() == 5 | 6:
    this_week = datetime.now() + timedelta(days=6)


# class MasterViewSet(viewsets.ModelViewSet):
#     queryset = Master.objects.all().order_by('industry')
#     serializer_class = MasterSerializer
#     permission_classes = (AllowAny,)

# # Create your views here.

# class GolfViewSet(viewsets.ModelViewSet):
#     # queryset = Master.objects.filter(industry='Golf')
#     queryset = Master.objects.filter(industry='Golf')
#     serializer_class = MasterSerializer
#     permission_classes = (AllowAny,)


@api_view(['GET'])
def dashboard(request):
    if request.method == 'GET':
        all_actions = Master.objects.all()
        dashboard_serializer = MasterSerializer(all_actions, many=True)
        return JsonResponse(dashboard_serializer.data, safe=False)

@api_view(['GET'])
def dashboard_filter(request, industry=None, action=None):
    # try:
    #     get_filter = Master.objects.all().filter(industry=industry, request=action)
    # except Master.DoesNotExist:
    #     return JsonResponse({'message': 'This job does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        get_filter = Master.objects.filter(industry=industry, request=action.replace('-', ' '))
        get_filter_serializer = MasterSerializer(get_filter, many=True)
        return JsonResponse(get_filter_serializer.data, safe=False)

@api_view(['GET'])
def dashboard_table(request, year=None, month=None, industry=None, action=None):
    # try:
    #     get_filter = Master.objects.all().filter(industry=industry, request=action)
    # except Master.DoesNotExist:
    #     return JsonResponse({'message': 'This job does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        get_table = Master.objects.filter(dueDate__year=year, dueDate__month=month, industry=industry, request=action.replace('-', ' '))
        get_table_serializer = MasterSerializer(get_table, many=True)
        return JsonResponse(get_table_serializer.data, safe=False)
        

@api_view(['GET'])
def golf_book_order(request):
    if request.method == 'GET':
        golf_booked_orders = Master.objects.filter(industry='Golf', request='Book Order').order_by("name", "oppNumber")
        golf_booked_order_serializer = MasterSerializer(golf_booked_orders, many=True)
        return JsonResponse(golf_booked_order_serializer.data, safe=False)

@api_view(['GET'])
def golf_drawing(request):
    if request.method == 'GET':
        golf_booked_orders = Master.objects.filter(industry='Golf', request='Book Order').order_by("name", "oppNumber")
        golf_booked_order_serializer = MasterSerializer(golf_booked_orders, many=True)
        return JsonResponse(golf_booked_order_serializer.data, safe=False)


@api_view(['GET', 'POST'])
def golf(request):
    if request.method == 'GET':
        golf_actions = Master.objects.filter(industry='Golf').order_by("name", "oppNumber")
        golf_serializer = MasterSerializer(golf_actions, many=True)
        return JsonResponse(golf_serializer.data, safe=False)

    if request.method == 'POST':
        golf_data = JSONParser().parse(request)
        golf_serializer = MasterSerializer(data=golf_data)
        if golf_serializer.is_valid():
            golf_serializer.save()
            return JsonResponse(golf_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(golf_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view((['GET']))
def golf_open(request):
    if request.method == 'GET':
        golf_open = Master.objects.filter(compDate=None).order_by("name", "oppNumber")
        golf_open_serializer = MasterSerializer(golf_open, many=True)
        return JsonResponse(golf_open_serializer.data, safe=False)

@api_view((['GET']))
def golf_today(request):
    if request.method == 'GET':
        golf_today = Master.objects.filter(dueDate__lte=today, compDate=None, industry='Golf').order_by("name", "oppNumber")
        golf_today_serializer = MasterSerializer(golf_today, many=True)
        return JsonResponse(golf_today_serializer.data, safe=False)

@api_view((['GET']))
def golf_this_week(request):
    if request.method == 'GET':
        golf_this_week = Master.objects.filter(dueDate__lt=this_week, dueDate__gte=today, industry="Golf").order_by("name", "oppNumber")
        golf_this_week_serializer = MasterSerializer(golf_this_week, many=True)
        return JsonResponse(golf_this_week_serializer.data, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def edit_action(request, pk):
    try:
        edit_action = Master.objects.get(pk=pk)
    except Master.DoesNotExist:
        return JsonResponse({'message': 'This job does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        edit_action_serializer = MasterSerializer(edit_action)
        return JsonResponse(edit_action_serializer.data)

    elif request.method == 'PUT':
        edit_action_data = JSONParser().parse(request)
        edit_action_serializer = MasterSerializer(edit_action, data=edit_action_data)
        if edit_action_serializer.is_valid():
            edit_action_serializer.save()
            return JsonResponse(edit_action_serializer.data)
        return JsonResponse(edit_action_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        edit_action.delete()
        return JsonResponse({'message': 'Job was deleted successfully '})