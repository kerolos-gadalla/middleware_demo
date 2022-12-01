import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


class Log:
    def debug(self, *a, **kw):
        return print(*a, **kw)

    def error(self, *a, **kw):
        return print(*a, **kw)


logger = Log()


def loggingMiddlewareFactory(get_response):

    def loggingMiddleWare(request):
        logger.debug(
            f"Just Got an Incoming request with Path {request.path} and id {id(request)}")
        response = get_response(request)
        logger.debug(f"Finished the request with response {response}")
        logger.debug(
            f"Finished the request with response code {response.status_code}")
        return response

    return loggingMiddleWare


# def loggingMiddlewareFactoryREORDERED(get_response):

#     def loggingMiddleWare(request):
#         logger.debug(
#             f"Just Got an Incoming request with Path (REORDERED) {request.path} and id {id(request)}")
#         response = get_response(request)
#         logger.debug(
#             f"Finished the request with response (REORDERED) {response}")
#         logger.debug(
#             f"Finished the request with response code (REORDERED) {response.status_code}")
#         return response

#     return loggingMiddleWare


class MiddleWare1:

    def __init__(self, get_response) -> None:
        self.get_response = get_response
        self.count_exceptions = 0

    def __call__(self, request):

        logger.debug(
            f"L2 {request.path} and id {id(request)}")

        if (('posts' in request.path and request.method == 'POST') or
                ('create' in request.path)):
            if not request.user.is_authenticated:
                # or whatever data you want to return
                return render(request, 'posts/not_authorized.html', {}, status=401)
        response = self.get_response(request)
        logger.debug(f"L2 {response}")
        logger.debug(
            f"L2 {response.status_code}")
        return response



class MiddleWareExceptionCount:

    def __init__(self, get_response) -> None:
        self.get_response = get_response
        self.count_exceptions = 0

    def __call__(self, request):
        # add all exceptions to each request
        request.total_exception_count = self.count_exceptions
        response = self.get_response(request)
        return response

    # def process_template

    def process_exception(self, request, exception):
        self.count_exceptions += 1
        logger.error(f"Encountered {self.count_exceptions} exceptions so far")

