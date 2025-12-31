import random
from typing import Optional
from dotenv import load_dotenv
import os


# NOTE: .env file should be ignored in .gitignore, but it's not for demonestration purposes only
load_dotenv()

username = os.getenv("ADMIN_USERNAME")
password = os.getenv("ADMIN_PASSWORD")


class LoginValidator:
    """A class used to validate logins"""

    def __init__(self, uname: Optional[str], pswd: Optional[str]) -> None:
        self.__uname = uname
        self.__pswd = pswd
        self.ver_code = None
        print("** Welcome To Store App **")
        print("--------------------------")

    def is_valid_uname(self, username: str) -> bool:
        return username == self.__uname

    def is_valid_pswd(self, password: str) -> bool:
        return password == self.__pswd

    def generate_verification_code(self) -> int:
        self.ver_code = random.randint(10_000, 99_999)
        return self.ver_code

    def validate_verification_code(self, ver_input: int) -> bool:
        return ver_input == self.ver_code


def initiate_login(validator: LoginValidator):
    while True:
        uname = input("Enter your username:>> ")
        if not validator.is_valid_uname(uname):
            print("Incorrect Username, Try Again...")
            continue
        else:
            break

    while True:
        password = input("Enter your password:>> ")
        if not validator.is_valid_pswd(password):
            print("Incorrect Password, Try Again...")
            continue
        else:
            break

    ver_code = validator.generate_verification_code()

    while True:
        print(f"Your Verification Code is: {ver_code}")

        try:
            ver_input = int(input("Enter the verification code:>> "))
        except ValueError:
            print("Verification code must be numeric...")
            continue

        if validator.validate_verification_code(ver_input):
            print("Hooray, Login Successful!")
            break
        else:
            print("Incorrect Verification Code, Try Again...")
            continue


lv = LoginValidator(uname=username, pswd=password)

initiate_login(validator=lv)
