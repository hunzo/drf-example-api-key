from django.conf import settings
from rest_framework.permissions import BasePermission

class CheckApiKey(BasePermission):
    def has_permission(self, request, view):
        api_key_secret = request.META.get('HTTP_API_KEY')
        return api_key_secret == settings.API_KEY_SECRET