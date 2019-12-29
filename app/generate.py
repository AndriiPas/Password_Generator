import secrets
import string
from math import pow, log


class Generate:

    def __init__(self, count_of_symbol=None):
        self.pul = 26
        self.count_of_symbol = count_of_symbol

    def generate(self, up_and_lw=None, digit=None, special_symbol=None):
        alphabet = string.ascii_lowercase
        if up_and_lw:
            self.pul += 26
            alphabet += string.ascii_uppercase
        if digit:
            self.pul += 10
            alphabet += string.digits
        if special_symbol:
            self.pul += 33
            alphabet += string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(int(self.count_of_symbol)))
        return password

    def password_entropy(self):
        entropy = log(pow(self.pul, int(self.count_of_symbol)), 2)
        if entropy < 28:
            result = 'Very Weak; might keep out family members'
            return result
        elif 28 <= entropy < 35:
            result = 'Weak; should keep out most people, often good for desktop login passwords'
            return result
        elif 35 <= entropy < 59:
            result = 'Reasonable; fairly secure passwords for network and company passwords'
            return result
        elif 59 <= entropy < 127:
            result = 'Strong; can be good for guarding financial information'
            return result
        elif 127 <= entropy:
            result = 'Very Strong; often overkill'
            return result
