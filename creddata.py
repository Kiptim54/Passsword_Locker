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

    def delete_cred(self):
        '''
        delete credentials 
        '''
        Credentials.cred_list.remove(self)
    
    @classmethod
    def find_account(cls, account):
        '''
        search for accounts
        '''
        for cred in cls.cred_list:
            if cred.account == account:
                return cred
    @classmethod
    def cred_exists(cls, account):
        '''
        confirm a class actually exists
        '''
        for cred in cls.cred_list:
            if cred.account == account:
                return True
        return False
    @classmethod
    def display_cred(cls):
        '''
        method that returns all credentials
        '''
        return cls.cred_list

    def __init__(self, account , username , password):

        self.account = account
        self.username = username
        self.password = password

