from alert.signals import alert_sent

def do_something_after_welcome_alert_is_sent(sender, alert, **kwargs):
    pass

alert_sent.connect(do_something_after_welcome_alert_is_sent,
                      sender=WelcomeAlert)
