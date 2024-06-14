""" Microservice API endpoints """

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


# Create your views here.
class MicroserviceViewSet(ViewSet):
    """API endpoints for microservice"""

    @action(["post"], detail=False)
    def summarize(self, request: Request) -> Response:
        """Summarize given text"""

        return Response(status=status.HTTP_200_OK)
