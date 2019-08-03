import pytest
from rest_framework import serializers, viewsets
from drf_multiple_serializer import ActionBaseSerializerMixin, ReadWriteSerializerMixin


# serializers

class DummyWriteSerializer(serializers.Serializer):
    pass


class DummyListSerializer(serializers.Serializer):
    pass


class DummyReadSerializer(serializers.Serializer):
    pass

# viewsets

class ActionBaseViewSet(ActionBaseSerializerMixin,
                        viewsets.ModelViewSet):
    pass

class ReadWriteViewSet(ReadWriteSerializerMixin,
                       viewsets.ModelViewSet):
    pass

# tests

def test_action_base_serializer_mixin():
    actions = {
        'list': DummyListSerializer,
        'create': DummyWriteSerializer,
        'retrieve': DummyReadSerializer,
        'update': DummyWriteSerializer,
        'delete': DummyWriteSerializer,
    }
    viewset = ActionBaseViewSet()
    viewset.serializer_classes = {
        'default': DummyWriteSerializer,
        'list': DummyListSerializer,
        'retrieve': DummyReadSerializer,
    }
    
    for action, expected_serializer in actions.items():
        viewset.action = action
        serializer = viewset.get_serializer_class()
        assert serializer == expected_serializer




def test_read_write_serializer_mixin():
    actions = {
        'list': DummyReadSerializer,
        'create': DummyWriteSerializer,
        'retrieve': DummyReadSerializer,
        'update': DummyWriteSerializer,
        'delete': DummyWriteSerializer,
    }
    viewset = ReadWriteViewSet()
    viewset.serializer_classes = {
        'read': DummyReadSerializer,
        'write': DummyWriteSerializer,
    }

    for action, expected_serializer in actions.items():
        viewset.action = action
        serializer = viewset.get_serializer_class()
        assert serializer == expected_serializer



def test_using_read_write_mixin_with_action_base_usage():
    viewset = ReadWriteViewSet()
    viewset.serializer_classes = {
        'default': DummyWriteSerializer,
        'list': DummyListSerializer,
        'retrieve': DummyReadSerializer,
    }

    for action in ('list', 'create', 'retrieve', 'update', 'delete'):
        viewset.action = action
        with pytest.raises(AssertionError):
            serializer = viewset.get_serializer_class()

def test_using_action_base_mixin_with_read_write_usage():
    viewset = ActionBaseViewSet()
    viewset.serializer_classes = {
        'read': DummyReadSerializer,
        'write': DummyWriteSerializer,
    }

    for action in ('list', 'create', 'retrieve', 'update', 'delete'):
        viewset.action = action
        with pytest.raises(AssertionError):
            serializer = viewset.get_serializer_class()
