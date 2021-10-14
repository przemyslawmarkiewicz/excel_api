from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from .serializers import FileSerializer
from rest_framework import status, parsers, renderers
from rest_framework.generics import GenericAPIView
from openpyxl import load_workbook
from api_service.views_helpers import set_summary


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
            file = data['file']
            wb = load_workbook(file)
            columns = set(data['columns'][0].split(','))
            columns_found = {column: False for column in columns}
            summary = []
            for sheet in wb:
                set_summary(sheet, columns_found, summary)
            for key, val in columns_found.items():
                if val and key not in [key["column"] for key in summary]:
                    summary.append({"column": key, "info": "column doesn't have numeric values"})
                if not val:
                    summary.append({"column": key, "info": "column not found"})
            return Response({
                'file': str(file),
                'summary': summary
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)