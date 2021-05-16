import mailchimp_transactional as MailchimpTransactional
from mailchimp_transactional.api_client import ApiClientError

import adaptor


class MailChimp(adaptor.Client):
    """ 
    Use sdk of mailchimp service 

    Attributes 
    ----------
    from_sender: str
        email of sender
    to_receivers: list
        list of receivers's emails
    subject: str
        subject of email
    content: list or str
        list ==> list of difference contents for receivers
        str ==> str of dynamic content
    

    methods
    -------
    create(): @abstractmethod
        create, set and change Attributes that service needs
    create_template(): @abstractmethod
        create Attributes that service needs for send email with template
    send_with_service(): @abstractmethod
        send email without template (only simple content)
    send_with_template(): @abstractmethod
        send email with template (dynamic content)

    """

    def __init__(self, from_sender, to_receivers, subject, content):
        super().__init__(from_sender, to_receivers, subject, content)

    def create(self):
        """
        set MailChimp_API_KEY
        change tokens list to dictionary's that service needs for tokens space in content
        if token phone_number have [] or '' delete that
        change signs of tokens space to signs's service needs
        if want send difference contents to receivers so it set settings for it 
        create message parameter for send email

        Parameter
        ---------
            to: list
                list of {"email": receiver, "type": 'to'}
            API_KEY: str
                MailChimp Api Key
            mailchimp:
                mailchimp client parameter
            message: dict
                {
                "from_email": email of sender,
                "subject": subject,
                "text": content,
                "to": to list,
                "merge_vars": self.tokens,
                }
            template_content: list
                [{"name":name of template's block, "content": content}]

        """


        self.to = []
        self.vars = []
        self.tokens = []
        self.API_KEY = 'EWV8qx2JRA6JcdYwEAEQ8g'
        self.mailchimp = MailchimpTransactional.Client(self.API_KEY)

        i = 0
        for tokens in self.tokens_list:
            for key in tokens:
                if key == "phone_number":
                    try:
                        if (tokens[key].count("[") and tokens[key].count("]")) == 1:
                            if tokens[key].count("'") == 2:
                                tokens[key] = tokens[key][2:-2]
                            else:    
                                tokens[key] = tokens[key][1:-1]
                    except:
                        pass
                self.vars.append({"name":key,"content":tokens[key]})
            self.tokens.append({'rcpt':self.to_receivers[i],'vars':self.vars})
            i =+ 1
            self.vars = []

        
        if type(self.to_receivers) != list:
            x = [self.to_receivers]
            self.to_receivers = x
            
#--------------------------------------------------------
        if self.tokens != []:
            try:
                temp_content = self.content.replace('{',"{{")
                self.content= temp_content.replace('}',"}}")
            except:
                pass
        
        if type(self.content) == list:
            if self.content[1] != None:
                if self.content[0] != self.content[1]:
                    self.content = "{{content}}"
                else:
                    self.content = self.content[0]
            else:
                self.content = self.content[0]


                    
        self.template_content =[{"name":"main","content": self.content}]
        for receiver in self.to_receivers:
            self.to.append({
                "email": receiver,
                "type": 'to'
            })

        self.message = {
            "from_email": self.from_sender,
            "subject": self.subject,
            "text": self.content,
            "to": self.to,
            "merge_vars": self.tokens,
        }


    def create_template(self):
        """
        set template name
        create template parameter
        add new template code (is comment)
        
        Parameter
        ---------
            template_name: str
                template name
            template: dict
                {"template_name": template_name, "template_content": template_content, "message": message}

        """

    # ==================== add new template ==================

        # self.add_template = False    # test
        # if self.add_template:
        #     self.template_name = self.template_name  # test
        #     html = codecs.open("adaptor\html_code_mailchimp.html")  # test
        #     code = html.read()  # test

        #     try:
        #         self.response = self.mailchimp.templates.add({"name": self.template_name,"code":code})
        #         print(self.response)
        #     except ApiClientError as error:
        #         print("An exception occurred: {}".format(error.text))
        # else:
        #     self.template_name = "simple Text"

    # ========================================================

        self.template = {"template_name": "simple Text", "template_content": self.template_content, "message": self.message}

    def send_with_service(self):
        """
        try to send email without template and print response
        if except print Error
        """

        try:
            self.response = self.mailchimp.messages.send({"message": self.message})
            print('API called successfully: {}'.format(self.response))
        except ApiClientError as error:
            print('An exception occurred: {}'.format(error.text))

    def send_with_template(self):
        """
        try to send email with template and print response
        if except print Error
        """

        try:
            self.response = self.mailchimp.messages.send_template(self.template)
            print('API called successfully: {}'.format(self.response))
        except ApiClientError as error:
            print('An exception occurred: {}'.format(error.text))