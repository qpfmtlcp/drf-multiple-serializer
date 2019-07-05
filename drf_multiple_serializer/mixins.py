class MultipleSerializerMixin(object):
    serializer_classes = {
        'default': None
    }

    def get_serializer_class(self):
        default = self.serializer_class or self.serializer_classes.get('default')
        assert default is not None, (
            "'%s' should either include a `serializer_class` attribute, "
            "or override the `get_serializer_class()` method."
            % self.__class__.__name__
        )

        serializer = self.serializer_classes.get(self.action)
        if not serializer:
            serializer = default

        return serializer
