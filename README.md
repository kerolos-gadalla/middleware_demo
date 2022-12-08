
### Middleware life cycle

![Life cycle](assets/lifecycle.png)

### Middleware in settings

![Life cycle](assets/MW_in_settings.png)

# Use cases

## Filtering Requests

- Regional
- Authority/Role
  - some paths can get guarded
- Cross site request forgery CSRF
  - can automatically implement and check for
- 404
- caching

## Injecting data

- Authentication - Inject user principle
- parse json to dict when it is the content type
- injecting headers allow-origion: www.our.trusted.co

## Collecting data

- Analytics
  - can help other components operate
    - a user blocking for the rest of the day for high traffic

```python
class ExampleMiddleware:

    def _init_(self, get_response):
        self.get_response = get_response

    def _call_(self, request):

        # Code that is executed in each request before the view is called

        response = self.get_response(request)

        # Code that is executed in each request after the view is called
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # This code is executed just before the view is called

    def process_exception(self, request, exception):
        # This code is executed if an exception is raised

    def process_template_response(self, request, response):
        # This code is executed if the response contains a render() method
        return response
```

# Examples

- SecurityMiddleware
- UpdateCacheMiddleware

- CommonMiddleware
    - This is curious

    ```ruby
    If APPEND_SLASH is True and the initial URL doesn’t end with a slash, and it is not found in the URLconf, then a new URL is formed by appending a slash at the end. If this new URL is found in the URLconf, then Django redirects the request to this new URL. Otherwise, the initial URL is processed as usual.
    ```
