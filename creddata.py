class Credentials:
    '''
    class that creates instaces of user accounts
    '''
    cred_list = []

    def save_cred(self):
        '''
        self credentials in cred_list
        '''
        Credentials.cred_list.append(self)


    def __init__(self, account , username , password):

        self.account = account
        self.username = username
        self.password = password

