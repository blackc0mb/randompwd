import random
## powered by raspberry.org
class pwd():
    def __init__(self):
        self.numpass = None
        self.passlenght = None
    
    def set_numpasswords(self, numpass):
        self.numpass = int(numpass)

    def set_length(self, passlenght):
        self.passlenght = int(passlenght)
    
    def get_passwords(self):
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTVWXYZ0123456789._?#$%&=),!-;*+'
        retPassword = []
        for p in range(self.numpass):
            password = ''
            for c in range(self.passlenght):
                password += random.choice(chars)
            retPassword.append(password)
        return retPassword
        
