from rest_framework import serializers
from .models import Camera, Characteristic, ShortDefenition, ShortDefenitionImage, Category, Filter


class CameraListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Camera
        fields = '__all__'

class CategoryListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Category
        fields = '__all__'

class CharacteristicListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Characteristic
        fields = [
            'key',
            'value',
        ]

class CameraDetailSerializer(serializers.ModelSerializer):    
    characteristics = CharacteristicListSerializer(many=True)
    class Meta:
        model = Camera
        fields = [
            "id",
            "camera_name",
            "camera_def",
            "camera_cost",
            "camera_image",
            "characteristics"
        ]

class ShortDefenitionListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = ShortDefenition
        fields = '__all__'

class ShortDefenitionImageListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = ShortDefenitionImage
        fields = '__all__'
        

class CategoryDetailSerializer(serializers.ModelSerializer):    
    camera = CameraListSerializer(many=True)
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "camera",
        ]


class FilterListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Filter
        fields = '__all__'


class FilterDetailListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Filter
        fields = [
            "BRAND_CHOICES",
            "CAMERA_TYPE_CHOICES",
            "FRAME_TYPE_CHOICES",
            "POS_CHOICES",
            "USE_CHOICES",
            "ZOOM_CHOICES",
            "SENS_CHOICES",
            "MP_CHOICES",
            "IK_CHOICES",
            "PROT_CHOICES",
            "SUP_CHOICES",
            "WDR_CHOICES",
            "VAR_CHOICES",
        ]