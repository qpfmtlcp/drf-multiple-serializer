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

### Action Base

Set the serializer to serializer_classes with the viewset action.  
The rest of the actions use the default serializer.

```
from rest_framework import viewsets
from drf_multiple_serializer import MultipleSerializerMixin


class CategoryViewSet(ActionBaseSerializerMixin,
                      viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_classes = {
        'default': CategorySerializer,
        'list': CategoryListSerializer,
        'retrieve': CategoryReadSerializer,
    }

```

### Read & Write

Set the read & write serializer to serializer_classes.  
List, Retrieve actions use a read serializer,  
and the other actions (include delete) use a write serializer.

```
from rest_framework import viewsets
from drf_multiple_serializer import ReadWriteSerializerMixin


class ItemViewSet(ReadWriteSerializerMixin,
                  viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_classes = {
        'read': ItemReadSerializer,
        'write': ItemWriteSerializer,
    }
```

## Test

```
> python3 -m venv venv
> source venv/bin/activate
(venv) > pytest
```
