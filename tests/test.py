from rest_framework import serializers, viewsets
from drf_multiple_serializer import MultipleSerializerMixin


# serializers

class DummyWriteSerializer(serializers.Serializer):
    pass


class DummyListSerializer(serializers.Serializer):
    pass


class DummyReadSerializer(serializers.Serializer):
    pass


# views

class DummyViewSet(MultipleSerializerMixin,
                   viewsets.ModelViewSet):
    serializer_classes = {
        'default': DummyWriteSerializer,
        'list': DummyListSerializer,
        'retrieve': DummyReadSerializer,
    }


# tests

def test_get_serializer_class_by_action():
    viewset = DummyViewSet()

    viewset.action = 'list'
    serializer = viewset.get_serializer_class()
    assert serializer == DummyListSerializer

    viewset.action = 'create'
    serializer = viewset.get_serializer_class()
    assert serializer == DummyWriteSerializer

    viewset.action = 'update'
    serializer = viewset.get_serializer_class()
    assert serializer == DummyWriteSerializer

    viewset.action = 'retrieve'
    serializer = viewset.get_serializer_class()
    assert serializer == DummyReadSerializer
