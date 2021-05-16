from ippanel import Client as FarazClient
from ippanel import Error

import adaptor


class FarazSMS(adaptor.Client):
    def __init__(self, excel_or_list, service, from_sender, to_receivers, subject, content,
                 templates, name):
        super().__init__(self, excel_or_list, service, from_sender, to_receivers, subject, content,
                         templates, name)

    def create(self):
        # self.sms = FarazClient(os.environ.get('FARAZ_API_KEY'))
        # self.from_sender = os.environ.get('FARAZ_NUMBER')
        # print(os.environ.get('FARAZ_API_KEY'))
        # print(os.environ.get('FARAZ_NUMBER'))
        self.sms = FarazClient("lE4WSCxzQlexOHiNj7Cdr1piDhpPE8vKFhUuSIeUSyM=")
        self.name = self.name
        self.content = self.content
        if type(self.to_receivers) is list:
            self.to_receivers = self.to_receivers
        else:
            self.to_receivers = [self.to_receivers]

    def send_with_service(self):
        print(self.to_receivers)
        print(self.content)
        try:
            bulk_id = self.sms.send(originator=self.from_sender,
                                    recipients=self.to_receivers,
                                    message=self.content)
            print('messages send successfully', bulk_id)
        except Error as e:
            print("Error handled => code: %s" % e.code)

    def create_template(self):
        self.template_for_all_services = self.template_for_all_services

    def send_with_template(self):
        print(self.to_receivers)
        print(self.name)

        for receiver, content, name in zip(self.to_receivers, self.template_for_all_services, self.name):
            try:
                bulk_id = self.sms.send(originator=self.from_sender,
                                        recipients=[receiver],
                                        message=content)
                print(f'messages send successfully to {name} -->bulk_id :{bulk_id}')
            except Error as e:
                print("Error handled => code: %s" % e.code)
