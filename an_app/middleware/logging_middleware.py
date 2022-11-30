import logging

logger = logging.getLogger(__name__)
class Log:
    def debug(self, *a, **kw):
        return print(*a, **kw) 

logger = Log()


def loggingMiddlewareFactory(get_response):
    
    def loggingMiddleWare(request):
        logger.debug(f"Just Got an Incoming request with Path {request.path} and id {id(request)}")
        response  = get_response(request)
        logger.debug(f"Finished the request with response {response}")
        logger.debug(f"Finished the request with response code {response.status_code}")
        return response
        
    return loggingMiddleWare

