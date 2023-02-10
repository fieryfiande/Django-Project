from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from central_inventory.models import *
from .models import *
from rest_framework.views import APIView
from django.http import Http404
# def index(request):
# #     return HttpResponse("Here I am at views")

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def site_list(request):
#     if request.method == 'GET':
#         sites = site.objects.all()
#         serializer = SiteSerializer(sites, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         sites = request.data
#         serializer = SiteSerializer(data=sites)
#         if serializer.is_valid():
#             serializer.save()
#             return Response('sites successfully added')
#     elif request.method == 'PUT':
#         primary = request.query_params.get('site_id', None)
#         if primary:
#             site1 = site.objects.get(pk=primary)
#             serializer = SiteSerializer(data=request.data,instance=site1)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response('sites Updated')
#     elif request.method == 'DELETE':
#         pk = request.query_params.get('site_id', None)
#         site1 = site.objects.get(pk=pk).delete()
#         return Response('sites Deleted')

class site_list(APIView):
    # def site_list(self, pk):
    #     try:
    #         return NewAPI.objects.get(pk=pk)
    #     except NewAPI.DoesNotExist:
    #         raise Http404
  
    def get(self, request, format=None):
        sites = site.objects.all()
        serializer = SiteSerializer(sites, many=True)
        return Response(serializer.data)

    def post(self, request,  format=None):
        sites = request.data
        serializer = SiteSerializer(data=sites)
        if serializer.is_valid():
            serializer.save()
            return Response('sites successfully added')

    def put(self, request, format=None):
        primary = request.query_params.get('site_id', None)
        if primary:
            site1 = site.objects.get(pk=primary)
            serializer = SiteSerializer(data=request.data,instance=site1)
            if serializer.is_valid():
                serializer.save()
                return Response('sites Updated')
        
    def delete(self, request, format=None):
        pk = request.query_params.get('site_id', None)
        site1 = site.objects.get(pk=pk).delete()
        return Response('sites Deleted')