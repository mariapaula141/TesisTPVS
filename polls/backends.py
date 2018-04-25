from alert.utils import BaseAlertBackend

class MyAlertBackend(BaseAlertBackend):
    
    def send(self, alert):
        # send the alert here