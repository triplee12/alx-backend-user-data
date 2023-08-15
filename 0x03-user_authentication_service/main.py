#!/usr/bin/env python3
"""Main file."""

# from db import DB
# from user import User
# from sqlalchemy.exc import InvalidRequestError
# from sqlalchemy.orm.exc import NoResultFound
# from auth import _hash_password
from auth import Auth

email = 'me@me.com'
password = 'mySecuredPwd'

auth = Auth()

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))

# print(_hash_password("Hello Holberton"))

# my_db = DB()

# user = my_db.add_user("test@test.com", "PwdHashed")
# print(user.id)

# user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
# print(user_2.id)

# find_user = my_db.find_user_by(email="test@test.com")
# print(find_user.id)

# try:
#     find_user = my_db.find_user_by(email="test2@test.com")
#     print(find_user.id)
# except NoResultFound:
#     print("Not found")

# try:
#     find_user = my_db.find_user_by(no_email="test@test.com")
#     print(find_user.id)
# except InvalidRequestError:
#     print("Invalid")

# try:
#     my_db.update_user(user.id, hashed_password='NewPwd')
#     print("Password updated")
# except ValueError:
#     print("Error")
