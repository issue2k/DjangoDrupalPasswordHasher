import os, sys
import collections
from hashlib import sha512
from django.contrib.auth.hashers import BasePasswordHasher

class DrupalPasswordHasher(BasePasswordHasher):
    '''
    Hashes a Drupal 7 password with the prefix 'drupal'
    Used for legacy passwords from VCP 2.0.

    snippet from https://djangosnippets.org/snippets/2729/#c4520
    modified for compatibility with Django 1.6
    '''

    algorithm = "drupal"
    iter_code = 'C'
    salt_length = 8

    def encode(self, password, salt, iter_code=None):
        """The Drupal 7 method of encoding passwords"""

        _ITOA64 = './0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

        if iter_code == None:
            iterations = 2 ** _ITOA64.index(self.iter_code)
        else:
            iterations = 2 ** _ITOA64.index(iter_code)

        # convert these to bytestrings to get rid of dumb decoding errors:
        salt = str(salt)
        password = str(password)

        hashed_string = sha512(salt + password).digest()

        for i in range(iterations):    
            hashed_string = sha512(hashed_string + password).digest()


        l = len(hashed_string)

        output = ''
        i = 0

        while i < l:
            value = ord(hashed_string[i])
            i = i + 1

            output += _ITOA64[value & 0x3f]
            if i < l:
                value |= ord(hashed_string[i]) << 8

            output += _ITOA64[(value >> 6) & 0x3f]
            if i >= l:
                break
            i += 1

            if i < l:
                value |= ord(hashed_string[i]) << 16

            output += _ITOA64[(value >> 12) & 0x3f]
            if i >= l:
                break
            i += 1

            output += _ITOA64[(value >> 18) & 0x3f]

        long_hashed = "%s$%s%s%s" % (self.algorithm, iter_code,
                salt, output)
        return long_hashed[:59]


    def verify(self, password, encoded):
        hash = encoded.split("$")[1]
        iter_code = hash[0]
        salt = hash[1:1 + self.salt_length]        
        test_encoded = self.encode(password, salt, iter_code)
        return encoded == test_encoded
