from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from .serializers import FileSerializer
from rest_framework import status, parsers, renderers
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView


class FileUploadView(GenericAPIView):
    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.FileUploadParser,
    )
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = FileSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            resume = data['file']
            columns = data['columns'][0].split(',')
            return Response({
                'file': str(resume),
                'columns': columns
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
