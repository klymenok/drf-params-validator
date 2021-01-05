from django.utils.functional import wraps

from rest_framework.response import Response
from rest_framework import status


def validate_request_params(params=None, data=None):
    """
    The decorator for view actions to validate request parameters presence
    :param params: list of GET params names to validate
    :param params: list of POST data items to validate
    :return:
    """
    def deco(f):
        @wraps(f)
        def wrapper(self, request, *args, **kwargs):
            if data:
                for item in data:
                    if not request.data.get(item):
                        return Response(f'`{item}` parameter is missing', status=status.HTTP_400_BAD_REQUEST)
            if params:
                for param in params:
                    if not request.query_params.get(param):
                        return Response(f'`{param}` parameter is missing', status=status.HTTP_400_BAD_REQUEST)
            return f(self, request, *args, **kwargs)
        return wrapper
    return deco
