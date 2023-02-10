from rest_framework import serializers
from .models import *

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = site
        fields = ['site_id','site_name','address','city','state','country','zipcode']
    
class IAPSerializer(serializers.ModelSerializer):
    class Meta:
        model = iap
        fields = '__all__'

class SwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = switch
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = '__all__'

