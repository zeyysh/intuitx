import json

from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client as TwilioClient

import adaptor


class Twilio(adaptor.Client):
    def __init__(self, service, from_sender, to_receivers, subject, content, templates, name):
        super().__init__(service, from_sender, to_receivers, subject, content, templates, name)
        """
        Twilio class(defined for twilio sms service) can be used for giving required parameters
        ---------
        Constructs all the necessary attributes for the client object.
        """
    def create(self):
        """
        Twilio accessing api for client
        accessibility:
        just enrolled phone number
        """
        # self.client = TwilioClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        # self.from_sender = settings.TWILIO_NUMBER
        account_sid = 'AC65a9c31d92aff32d8ec2f613c0b5e237'
        auth_token = "ca2642802db20cbab875b926f4b1c411"
        self.notify_service_sid = 'ISab30811b824a0254585c7f41b66daf3d'
        self.client = TwilioClient(account_sid, auth_token)
        self.to_receivers = self.to_receivers
        self.content = self.content
        if not self.templates:
            self.receivers_content = []
            self.receivers_content.append(self.content)


    def create_template(self):
        """
        receivers contact: list
        getting tokens(dynamic content) from tokens list and put them in content
        """
        self.receivers_content = []
        for tokens in self.tokens_list:
            content = self.content
            for key in tokens:
                content = content.replace("{" + f"{key}" + "}", f"{tokens[key]}")
            self.receivers_content.append(content)


    def send_with_service(self):
        """
        send service for twilio message provider
        receivers content => file format: zip
        creat message from client message
        and if it works correctly it will print (successfully send)
        """
        try:
            for content, receiver in zip(self.receivers_content, self.to_receivers):
                message = self.client.messages.create(to=receiver,
                                                      from_=self.from_sender
                                                      , body=content)
                print(self.receivers_content)
                print("message send successfully, message.sid")
        except TwilioRestException as e:
            print("Error handeled => code:%s" % e.code)

    def send_with_template(self):
        """
        # as template for Twilio sms service is not submitted this template is manual
        it can be set on bulk sms
        template: boolean
        get information from send_with_service and normalize_phone_number and send it by api
        """
        print(self.to_receivers)

        bindings = list(map(lambda number: json.dumps({'binding_type': 'sms', 'address': number}), self.to_receivers))
        print("=====> To Bindings :>", bindings, "<: =====")
        try:
            notification = self.client.notify.services(self.notify_service_sid).notifications.create(
            to_binding=bindings,
            body=self.receivers_content[0]
            )
            print(notification.body)
            print("message send successfully, message.sid")
        except TwilioRestException as e:
            print("Error handeled => code:%s" % e.code)

def normalize_phone_number(receiver):
    """
    normalize your phonen umber so it can be read without error
    """
    if receiver[0] != '+':
         if receiver[0] == '0':
             if receiver[1] == '0':
                 receiver = '+' + receiver[2:]
             else:
                 receiver = '+' + receiver[1:]
         else:
             receiver = '+' + receiver
    return receiver