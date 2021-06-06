# from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.schemas import get_schema_view

API_TITLE = "Event App "
API_DESCRIPTION = "A Web API for project 'API for event app'."

schema_view = get_schema_view(
    title=API_TITLE + "API",
    description=API_DESCRIPTION,
    version="0.1.0",
    permission_classes=[IsAuthenticated],
    authentication_classes=[BasicAuthentication],
)

api_urls = [
    path("events/", include("events.urls")),
    path("users/", include("users.urls")),
    # docs
    path("openapi/", schema_view, name="openapi-schema"),
    path(
        "docs/",
        TemplateView.as_view(
            template_name="swagger.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger",
    ),
]

urlpatterns = [
    path("api/", include(api_urls)),
    #    path('admin/', admin.site.urls),
]
