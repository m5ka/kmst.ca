from django.http import HttpRequest, HttpResponse
from django_minify_html.middleware import MinifyHtmlMiddleware


class WebsiteMinifyHtmlMiddleware(MinifyHtmlMiddleware):
    def should_minify(self, request: HttpRequest, response: HttpResponse) -> bool:
        return super().should_minify(request, response) and not request.path.startswith(
            "/admin/"
        )
