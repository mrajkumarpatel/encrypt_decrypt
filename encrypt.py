import traceback
from cryptography.fernet import Fernet
import settings
import base64
import sys


# noinspection PyBroadException
def encrypt(txt):
    try:
        # convert integer etc to string first
        txt = str(txt)
        # get the key from settings
        cipher_suite = Fernet(settings.ENCRYPT_KEY) # key should be byte
        # #input should be text, so convert the text to byte
        encrypted_text = cipher_suite.encrypt(txt.encode('ascii'))
        # encode to urlsafe base64 format
        encrypted_text = base64.b64encode(encrypted_text).decode("ascii")
        return encrypted_text
    except Exception as e:
        print(traceback.format_exc())
        return None


if __name__ == '__main__':
	if len(sys.argv) == 2:
		print(encrypt(sys.argv[1]))
	else:
		print("Pass One Argument, the Text Which you want to be Encrypted")
