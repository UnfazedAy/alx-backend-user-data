#!/usr/bin/python3
# import logging

# logging.info("This is an info level")

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]

# c = zip(a, b)
# res = "".join([f"{k}={v}" for k, v in c])
# print(res)

import bcrypt

password = "donthavetimetothink"
bytes = password.encode('UTF-8')
salt = bcrypt.gensalt()
hash = bcrypt.hashpw(bytes, salt)
print(hash)