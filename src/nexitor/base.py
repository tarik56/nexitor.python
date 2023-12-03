import requests
import threading


class NexitorBase:

    def __init__(self, url, application, instance, api_key):
        self.url = url
        self.application = application
        self.instance = instance
        self.api_key = api_key

    def log(self, status, title, user_name, user_identifier, user_ip, message, payload, stacktrace):
        def send_log():
            requests.post(
                url=self.url + "log",
                json=dict(
                    status=status,
                    title=title,
                    user_name=user_name,
                    user_identifier=user_identifier,
                    user_ip=user_ip,
                    message=message,
                    payload=payload,
                    stacktrace=stacktrace,
                    application=self.application,
                    instance=self.instance),
                headers={"Authorization": f"Bearer {self.api_key}"})

        threading.Thread(target=send_log).start()
