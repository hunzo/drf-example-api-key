from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


from .permission import CheckApiKey

@api_view(['GET'])
@permission_classes((CheckApiKey,))
def example_view(request, format=None):
    content = {
        'stutus': 'ok'
    }

    return Response(content)