from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from django import views
from .models import *
from .serializer import *
from rest_framework.decorators import detail_route
from django.shortcuts import render
from .forms import *


# Create your views here.


'''class aview(viewsets.ModelViewSet):
    queryset = A.objects.all()
    serializer_class = aserializer

    @detail_route(methods=['get'])
    def set_age(self):

        def get_queryset(self):
            return A.objects.filter(id <= 5)

        def get_context_data(self, **kwargs):
            return get_queryset()

        return Response(self.serializer_class(get_queryset()).data)'''


def hello(request):
    return render(request, 'A.html', {'form': Aform()})
