class User:
    '''
    Class that generates new instances of user
    '''
    user_list = [] #list of users to be stored here

    def save_user(self):
        '''
        saving user credentials into user_list for login
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete a user account
        '''
        User.user_list.remove(self)
    @classmethod
    def find_user(cls, username):
        '''
        find username using search terms
        '''
        for user in cls.user_list:
            if user.username == username:
                return  user



    def __init__(self, username,password):
        '''
        These are the properties of the class User
        '''
        self.username = username
        self.password = password