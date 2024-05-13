from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

class HomePage(viewsets.ViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home/index.html'

    def list(self, request):
        username = request.query_params.get('username')
        return Response({'username': username})
