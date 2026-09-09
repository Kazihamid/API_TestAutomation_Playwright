class BaseAPI:
    def __init__(self, request):
        self.request = request

    def get(self, endpoint, headers=None, params=None):
        return self.request.get(endpoint, headers=headers, params=params)

    def post(self, endpoint, headers=None, data=None, form=None):
        """
        data: use for raw/JSON bodies (Playwright auto-serializes dicts to JSON
              and sets Content-Type: application/json if not already set)
        form: use for x-www-form-urlencoded bodies (dict of key/value pairs)
        """
        return self.request.post(endpoint, headers=headers, data=data, form=form)
