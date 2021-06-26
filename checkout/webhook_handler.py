from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handle Stripe weebhooks
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown unexpected webhook event
        """
        return HttpResponse(
            content=f'Weebhook received: {event["type"]}',
            status=200)
