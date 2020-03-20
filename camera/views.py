from django.shortcuts import render, redirect
from rest_framework import generics
from .serializers import CameraListSerializer, CharacteristicListSerializer, ShortDefenitionListSerializer,ShortDefenitionImageListSerializer, CameraDetailSerializer, CategoryListSerializer, CategoryDetailSerializer, FilterListSerializer, FilterDetailListSerializer
from . models import Camera, Characteristic, ShortDefenition, ShortDefenitionImage, Category, Filter, User
from rest_framework.decorators import action
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

############ TEMPLATES #############################

def index(request, Context={}):
    camera = Camera.objects.all()
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'camera': camera,
    }
    context.update(Context)
    return render(request, 'site/pages/home.html', context)

def category(request, pk):
    camera = Camera.objects.filter(category=pk)
    categories = Category.objects.all()
    category = Category.objects.get(id=pk)
    context = {
        'camera': camera,
        'category': category,
        'categories': categories,
    }
    return render(request, 'site/pages/category.html', context)

def camera_detail(request, pk):
    camera = Camera.objects.get(id=pk)
    categories = Category.objects.all()
    short_def = ShortDefenition.objects.filter(camera=pk)
    short_img = ShortDefenitionImage.objects.filter(camera=pk)
    characteristic = Characteristic.objects.filter(camera=pk)
    context = {
        'camera': camera, 
        'categories': categories,
        'short_def': short_def, 
        'short_img': short_img, 
        'characteristic': characteristic
    }
    return render(request, 'site/pages/camera-model.html', context)




def shops(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'site/pages/shops.html', context)
def delivery(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'site/pages/delivery.html', context)
def payment(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'site/pages/payment.html', context)
def contact(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'site/pages/contact.html', context)
def services(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'site/pages/services.html', context)
def feedback(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'site/pages/feedback.html', context)

# Authentication View

def singin(request):
    

def signup(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('camera:index')
    else:
        form = SignUpForm()
    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'site/pages/signup.html', context)

####### API #######################################

class CameraListView(generics.ListAPIView):
    serializer_class = CameraListSerializer
    queryset = Camera.objects.all()

    @action(detail=True, methods=["GET"])
    def camera(self, request, id=None):
        category = self.get_object()
        camera = Camera.objects.filter(category=category)
        serializer = CameraListSerializer(camera, many=True)
        return Response(serializer.data, status=200)

class CharacteristicListView(generics.ListAPIView):
    serializer_class = CharacteristicListSerializer
    queryset = Camera.objects.all()

    @action(detail=True, methods=["GET"])
    def characteristic(self, request, id=None):
        camera = self.get_object()
        characteristic = Characteristic.objects.filter(camera=camera)
        serializer = CharacteristicListSerializer(characteristic, many=True)
        return Response(serializer.data, status=200)

class ShortDefenitionListView(generics.ListAPIView):
    serializer_class = ShortDefenitionListSerializer
    queryset = ShortDefenition.objects.all()

class ShortDefenitionImageListView(generics.ListAPIView):
    serializer_class = ShortDefenitionImageListSerializer
    queryset = ShortDefenitionImage.objects.all()

class DetailListView(generics.ListAPIView):
    serializer_class = CameraDetailSerializer
    def get_queryset(self):
        
        if self.kwargs['id']:
            return Camera.objects.filter(id=self.kwargs['id'])
        else:
            return Camera.objects.all().order_by('id')

class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

class CategoryDetailListView(generics.ListAPIView):
    serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        if self.kwargs['id']:
            return Category.objects.filter(id=self.kwargs['id'])
        else:
            return Category.objects.all().order_by('id')


class FilterListView(generics.ListAPIView):
    serializer_class = FilterListSerializer
    queryset = Filter.objects.all()

class FilterDetailListView(generics.ListAPIView):
    queryset = Filter.objects.all()
    serializer_class = FilterDetailListSerializer
