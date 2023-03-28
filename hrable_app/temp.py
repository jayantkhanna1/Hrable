
from passlib.hash import sha512_crypt as sha512
pwd = "dummyhr"
pwd = sha512.hash(pwd, rounds=5000, salt="hrablehr")
print(pwd)