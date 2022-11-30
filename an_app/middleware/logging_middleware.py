import logging

logger = logging.getLogger(__name__)


def loggingMiddlewareFactory(get_response):
    
    def loggingMiddleWare(request):
        logger.debug("Just Got an Incoming request with Path {request.path}")
        response  = get_response(request)
        logger.debug("Finished the request with response {response.data}")
        logger.debug("Finished the request with response code {response.status_code}")
        return response
        
    return loggingMiddleWare

