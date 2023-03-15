# DJANGO Rest Framework API_KEY
- @permission.py
```python
from django.conf import settings
from rest_framework.permissions import BasePermission

class CheckApiKey(BasePermission):
    def has_permission(self, request, view):
        api_key_secret = request.META.get('HTTP_API_KEY')
        return api_key_secret == settings.API_KEY_SECRET
```
- @settings.py
```python
API_KEY_SECRET = 'secret_key'

add application
'rest_framework'
```
- @views.py
```python
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
```
- @urls.py
```python
from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.example_view, name="home")
]
```



