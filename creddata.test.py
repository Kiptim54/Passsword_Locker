import unittest
from creddata import Credentials

class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        setup before a test is run
        '''
        self.new_cred = Credentials("Facebook", "Kiptim54", "Author7")
    def test_init(self):
        '''
        check if instances initialize as expected
        '''
        self.assertEqual(self.new_cred.account, "Facebook")
        self.assertEqual(self.new_cred.username, "Kiptim54")
        self.assertEqual(self.new_cred.password, "Author7")
    def test_save_credentials(self):
        '''
        check if credentials can be saved
        '''  
        self.new_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list),1)
        
    

if __name__ == '__main__':
    unittest.main()