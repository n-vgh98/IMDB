import logging
import time




class TimeMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        duration = time.time() - start_time

        response["X-Page-Generation-Duration-ms"] = int(duration * 1000)

        logger = logging.getLogger('response_time')
        logger.error(f'{response}')
        print(response)
        return response










    # def process_request(self, request):
    #     request.start_time = time.time()
    #
    # def process_response(self, request, response):
    #     total = time.time() - request.start_time
    #
    #     response["X-total-time"] = int(total * 1000)
    #
    #
    #     return response
