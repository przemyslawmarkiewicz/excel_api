from django.core.validators import FileExtensionValidator
from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    file = serializers.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['xlsx', 'xls'])]
    )
    columns = serializers.ListField(child=serializers.CharField())
