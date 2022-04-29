from tkinter.messagebox import RETRY
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# from rest_framework import viewsets
from .serializers import MasterSerializer
from .models import Master
# from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status


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


@api_view(['GET', 'POST'])
def golf(request):
    if request.method == 'GET':
        golf_actions = Master.objects.filter(industry='Golf')
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
        golf_open = Master.objects.filter(compDate=None)
        golf_open_serializer = MasterSerializer(golf_open, many=True)
        return JsonResponse(golf_open_serializer.data, safe=False)


# not used based on site functionality, but works as an endpoint
# @api_view(['GET', 'PUT', 'DELETE'])
# def golf_action(request, pk):
#     try:
#         golf_action = Master.objects.filter(industry='Golf').get(pk=pk)
#     except Master.DoesNotExist:
#         return JsonResponse({'message': 'This job does not exist.'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         golf_action_serializer = MasterSerializer(golf_action)
#         return JsonResponse(golf_action_serializer.data)

#     elif request.method == 'PUT':
#         golf_action_data = JSONParser().parse(request)
#         golf_action_serializer = MasterSerializer(golf_action, data=golf_action_data)
#         if golf_action_serializer.is_valid():
#             golf_action_serializer.save()
#             return JsonResponse(golf_action_serializer.data)
#         return JsonResponse(golf_action_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         golf_action.delete()
#         return JsonResponse({'message': 'Job was deleted successfully '})

@api_view(['GET', 'PUT'])
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