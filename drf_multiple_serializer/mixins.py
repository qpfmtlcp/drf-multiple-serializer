class MultipleSerializerMixin(object):
    serializer_classes = {}
    
    def get_serializer_class(self):
        serializer_class = self.get_serializer_class_by_action() or self.serializer_class
        
        assert serializer_class is not None, (
            "'%s' should either include one of `serializer_class` and `serializer_classes` attribute, "
            "or override the `get_serializer_class()` method."
            % self.__class__.__name__
        )
        
        return serializer_class
    
    def get_serializer_class_by_action(self):
        pass


class ActionBaseSerializerMixin(MultipleSerializerMixin):
    serializer_classes = {
        'default': None,
    }
    
    def get_serializer_class_by_action(self):
        default = self.serializer_classes.get('default')
        serializer_class = self.serializer_classes.get(self.action)
        return serializer_class or default


class ReadWriteSerializerMixin(MultipleSerializerMixin):
    serializer_classes = {
        'read': None,
        'write': None,
    }
    
    def get_serializer_class_by_action(self):
        if self.action in self.get_read_actions():
            return self.serializer_classes.get('read')
        
        if self.action in self.get_write_actions():
            return self.serializer_classes.get('write')
    
    def get_read_actions(self):
        actions = ('list', 'retrieve')
        return actions
    
    def get_write_actions(self):
        actions = ('create', 'update', 'partial_update', 'delete')
        return actions
