from django.contrib.auth.hashers import mask_hash, BasePasswordHasher
from django.test import TestCase

# Create your tests here.
import base64
import hashlib
import secrets
from django.utils.crypto import (
    constant_time_compare, get_random_string, pbkdf2,
)
class PBKDF2PasswordHasher(BasePasswordHasher):
    """
    Secure password hashing using the PBKDF2 algorithm (recommended)
    Configured to use PBKDF2 + HMAC + SHA256.
    The result is a 64 byte binary string.  Iterations may be changed
    safely but you must rename the algorithm if you change SHA256.
    """
    algorithm = "pbkdf2_sha256"
    iterations = 260000
    digest = hashlib.sha256

    def encode(self, password, salt, iterations=None):
        assert password is not None
        assert salt and '$' not in salt
        iterations = iterations or self.iterations
        hash = pbkdf2(password, salt, iterations, digest=self.digest)
        hash = base64.b64encode(hash).decode('ascii').strip()
        return "%s$%d$%s$%s" % (self.algorithm, iterations, salt, hash)

    def decode(self, encoded):
        algorithm, iterations, salt, hash = encoded.split('$', 3)
        assert algorithm == self.algorithm
        return {
            'algorithm': algorithm,
            'hash': hash,
            'iterations': int(iterations),
            'salt': salt,
        }

    def verify(self, password, encoded):
        decoded = self.decode(encoded)
        encoded_2 = self.encode(password, decoded['salt'], decoded['iterations'])
        return constant_time_compare(encoded, encoded_2)

    def safe_summary(self, encoded):
        decoded = self.decode(encoded)
        return {
            _('algorithm'): decoded['algorithm'],
            _('iterations'): decoded['iterations'],
            _('salt'): mask_hash(decoded['salt']),
            _('hash'): mask_hash(decoded['hash']),
        }

    def must_update(self, encoded):
        decoded = self.decode(encoded)
        return decoded['iterations'] != self.iterations

    def harden_runtime(self, password, encoded):
        decoded = self.decode(encoded)
        extra_iterations = self.iterations - decoded['iterations']
        if extra_iterations > 0:
            self.encode(password, decoded['salt'], extra_iterations)


PBKDF2PasswordHasher.encode("123456","1iIuGXvAwr/kXmqQ=",None)



