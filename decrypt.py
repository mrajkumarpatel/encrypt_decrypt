import traceback
from cryptography.fernet import Fernet
import settings
import base64
import sys


# noinspection PyBroadException
def decrypt(txt):
    try:
        # base64 decode
        txt = base64.b64decode(txt)
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        decoded_text = cipher_suite.decrypt(txt).decode("ascii")
        return decoded_text
    except Exception as e:
        # log the error
        print(traceback.format_exc())
        return None


if __name__ == '__main__':
	if len(sys.argv) == 2:
		print(decrypt(sys.argv[1]))
	else:
		print("Pass One Argument, the Encrypted String - Which you want to be Decrypted")