class DynamicFieldsSerializer(ModelSerializer):
    """Takes an additional `fields` argument """

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        super().__init__(*args, **kwargs)

        if fields is not None: # Leave only specified `fields`
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class DynamicFieldsSerializer(ModelSerializer):
    """Takes an additional `fields` argument"""

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None) or self.Meta.fields
        self.Meta = type('Meta', (self.Meta,) {'fields' : fields})
        super().__init__(*args, **kwargs)

