from django.utils.functional import wraps

from rest_framework.response import Response
from rest_framework import status

def validate_request_params(params: list):
    """
    The decorator for view actions to validate request parameters presence
    :param params: list of params names to validate
    :return:
    """
    def deco(f):
        @wraps(f)
        def wrapper(self, request, *args, **kwargs):
            for param in params:
                if not request.data.get(param):
                    return Response(f'`{param}` parameter is missing', status=status.HTTP_400_BAD_REQUEST)
            return f(self, request, *args, **kwargs)
        return wrapper
    return deco
