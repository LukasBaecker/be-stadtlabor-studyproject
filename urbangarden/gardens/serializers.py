from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import Garden,Resource, ResourceBorrowing

#Garden
class GardenSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Garden
        geo_field = 'geom_point'
        fields = '__all__'
        

# Resource
class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['resource_id', 'resource_status', 'resource_name', 
                'category', 'date_created', 'return_date', 'garden'
            ]

# ResourceBorrowing
class ResourceBorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceBorrowing
        fields = '__all__'
