
class ExampleMiddleware:

    def __init__(self, get_response):
        print("called ExampleMiddleware.__init__")

        self.get_response = get_response

    def __call__(self, request):
        print("called ExampleMiddleware")

        # Code that is executed in each request before the view is called
        self.process_request(request)
        response = self.get_response(request)
        response = self.process_response(request, response)

        # Code that is executed in each request after the view is called
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # This code is executed just before the view is called
        print("called process_view")

    def process_exception(self, request, exception):
        # This code is executed if an exception is raised
        print("called process_exception")

    def process_template_response(self, request, response):
        # This code is executed if the response contains a render() method
        print("called process_template_response")
        return response

    def process_request(self, request):
        print("called process_request")

    def process_response(self, request, response):
        print("called process_response")

        return response
