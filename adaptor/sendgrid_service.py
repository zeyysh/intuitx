import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
from sendgrid.helpers.mail import Mail

import adaptor


class sendGrid(adaptor.Client):
    """
    This class inherited of Client and override create, send_with_service, send_with_template and create_template
    SendGrid class used Send Grid SDK for sending email in to way. First send a same content to one or
    multiple email address, second send a dynamic content with given parameters to one or multiple email address.
    ....

    Attributes:
        -------
        same as Client class

    Methods:
        create(self):
        set the same content to email object of send grid
            Returns:
                A send grid object for sending email with it's API

    """

    def __init__(self, service, from_sender, to_receivers, subject, content, templates, name):
        super().__init__(service, from_sender, to_receivers, subject, content, templates, name)

    def create(self):
        """
        set content from a list or string and then create a mail Object

        @return:
        email
        @rtype: SendGrid Object
        """

        if type(self.content) == list:
            if self.content[1] != None:
                if self.content[0] != self.content[1]:
                    self.content = "-content-"
                else:
                    self.content = self.content[0]
            else:
                self.content = self.content[0]

        # create a Mail and assign sender, object, receivers and content
        mail = Mail()
        mail.from_email = self.from_sender
        mail.subject = self.subject
        mail.to = self.to_receivers
        mail.content = Content("text/plain", self.content)
        return mail

    def send_with_service(self):
        """
        send emails with same content to multiple receivers from send grid API
        @rtype: object
        """
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            sg.send(sendGrid.create(self))
        except Exception as e:
            print(e.to_dict)

    def create_template(self):
        """
        create emails with different content to send to multiple receivers
        """
        self.content = self.content.replace('{', '-')
        self.content = self.content.replace('}', '-')
        tokennames = []  # used for storing tokens name
        tokenvalues = []  # used for storing tokens values
        for i in range(1):
            tokennames.append(list(self.tokens_list[i]))
        for i in range(len(self.tokens_list)):
            tokenvalues.append(list(self.tokens_list[i].values()))
        # change the format of phone number in files to Appropriate format for sending email
        for i in range(len(tokenvalues)):
            for j in range(len(tokenvalues[i])):
                if type(tokenvalues[i][j]) == str and tokenvalues[i][j][0] == '[':
                    tokenvalues[i][j] = tokenvalues[i][j].replace("['", '')
                    tokenvalues[i][j] = tokenvalues[i][j].replace("']", '')
        to_emails = []
        # create a To object for each receiver
        for i in range(len(self.tokens_list)):
            to = To()
            to.email = self.to_receivers[i]
            to.subject = self.subject
            # change the format off tokens to a appropriate format for seng grid
            sub_dic = {'-' + str(tokennames[0][j]) + '-': str(tokenvalues[i][j]) for j in
                       range(len(tokennames[0]))}
            to.substitutions = sub_dic
            to_emails.append(to)
        # create a Mail object for sending all emails
        message = Mail(
            from_email=self.from_sender,
            to_emails=to_emails,
            subject='Hello from SendGrid!',
            html_content=self.content,
            is_multiple=True)
        return message

    def send_with_template(self):
        """
        send emails with dynamic content and assigned tokens to multiple receivers from send grid API
        """

        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            sg.send(sendGrid.create_template(self))
        except Exception as e:
            print(e.to_dict)
