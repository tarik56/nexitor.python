import time

from .base import NexitorBase
from flask import request


class NexitorFlask(NexitorBase):

    def __init__(self, url, application, instance, api_key, handler):
        super(NexitorFlask, self).__init__(url, application, instance, api_key)
        self.handler = handler

        @self.handler.before_request
        def before():
            request.start_time = time.time()

        @self.handler.after_request
        def after(response):
            elapsed_time = time.time() - request.start_time
            print(f"Time taken for the request: {elapsed_time} seconds")
            return response



