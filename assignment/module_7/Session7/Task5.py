#Use ChatGPT to generate a Python example where a base class Notification has a send() method, and two subclasses (EmailNotification, SMSNotification) override send() to print different messages. Paste the generated code, run it, and write one line explaining how method overriding works in your example.

class Notification:
    def send(self):
        print("Sending Notification")

class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification")

n=Notification()
e=EmailNotification()
s=SMSNotification()
n.send()
e.send()
s.send()