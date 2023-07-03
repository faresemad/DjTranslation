from django.utils import translation


class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if "lang" in request.GET:
            lang = request.GET["lang"]
            translation.activate(lang)

        response = self.get_response(request)

        return response
