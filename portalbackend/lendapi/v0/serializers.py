from rest_framework import serializers


class GenericSerializer(serializers.Serializer):

    def update(self, instance, validated_data):
        pass

    def save(self, **kwargs):
        pass

    def create(self, validated_data):
        pass

    pass
