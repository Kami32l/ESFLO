import hashlib

def hash_password(pswrd):
    """
    Hashes password using sha256.
    :param pswrd: password to hash
    :return: password hash
    """
    pswrd = pswrd.encode()
    pswrd = hashlib.sha256(pswrd).hexdigest()
    return pswrd