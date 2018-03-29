class Credentials:
    '''
    class that creates instaces of user accounts
    '''
    cred_list = []

    def __init__(self, account , username , password):

        self.account = account
        self.username = username
        self.password = password

