import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


class Log:
    def debug(self, *a, **kw):
        return print(*a, **kw)

    def error(self, *a, **kw):
        return print(*a, **kw)


logger = Log()


class LogMiddleware:

    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request):

        logger.debug(
            f" LogMiddleware request:  {request.path} and id {id(request)}")
        # logger.debug(f" LogMiddleware request:  {request.META}")

        response = self.get_response(request)

        logger.debug(f" LogMiddleware response:  {response.status_code}")
        
        return response
