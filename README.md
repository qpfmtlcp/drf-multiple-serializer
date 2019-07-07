# DRF multiple serializer

[![Build Status](https://travis-ci.org/qpfmtlcp/drf-multiple-serializer.svg?branch=master)](https://travis-ci.org/qpfmtlcp/drf-multiple-serializer)

Extension for using multiple serializer in Django REST Framework.


## Installation

Install from [PyPI](https://pypi.org/project/drf-multiple-serializer/)

```
pip install drf-multiple-serializer
```

There is no need to modify your INSTALLED_APPS setting.


## Usage

Set the serializer to serializer_classes with the viewset action.  
The rest of the actions use the default serializer.

```
from rest_framework import viewsets
from drf_multiple_serializer import MultipleSerializerMixin

from .models import Category, Item


class CategoryViewSet(MultipleSerializerMixin,
                      viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_classes = {
        'default': CategorySerializer,
        'list': CategoryListSerializer,
        'retrieve': CategoryReadSerializer,
    }


class ItemViewSet(MultipleSerializerMixin,
                  viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_classes = {
        'default': ItemSerializer,
        'create': ItemWriteSerializer,
    }
```
