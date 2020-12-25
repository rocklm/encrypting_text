''' 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Script Name: 
text encryption module

Purpose:
functions to encrypt and decrypt text

Script Dependencies:
N/A

Parent Script(s):
N/A

Child Scripts(s):
N/A

Notes:
(1) built on Python Version 3.9.1 64bit
(2) useful for encrypting API keys and passwords/passphrases

Name            Date            Version         Change
Lee Rock        25/12/2020      v1.0.0          initial version

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
'''

''' 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                    start of script
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
'''

''' 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
install required non standard external modules if missing
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
'''

import sys
import subprocess
import pkg_resources

required = {'cryptography'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)


''' 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
required modules
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
'''

from cryptography.fernet import Fernet #install (build version: 3.3.1)


class encrypt:

    #initialisation function
    def __init__(self):
        pass

    #function to encrypt text
    #sends the encrypted text and cipher key to seperate text files in the same directory
    def encrypt_text(text, file_loc):
    
        #convert passed text into a string - if unable retrun error message
        try:
            text = str(text)
            file_loc = str(file_loc)
        except:
            raise TypeError('inputs must be a string or coercable into a string data type')


        cipher_key = Fernet.generate_key() #generate an encrytion key
        cipher = Fernet(cipher_key) #initialise encryption key
        encrypted_text = cipher.encrypt(bytes(text, encoding='utf-8')) #encrypt the text
    
        #write the encrypted password to a text file
        with open(file_loc + '\\encrypted_text.txt', 'w') as text_file:  text_file.write(encrypted_text.decode("utf-8"))
        text_file.close()
    
        #wirte the cipher key to a text file
        with open(file_loc + '\\cipher.txt', 'w') as key_file:  key_file.write(cipher_key.decode("utf-8"))
        key_file.close()

        print('Created encrypted text and cipher text file in {}'.format(file_loc))

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    #decrypt text
    #needs the encrypted text string
    #and the corresponding cipher key to decrypt the text
    def decrypt_text(text, cipher):
        
        #encode the encrypted text and corresponding cipher key to utf-8
        #otherwise raise an exception error
        try:
            encoded_text = bytes(text, encoding='utf-8')
            encoded_cipher = Fernet(bytes(cipher, encoding='utf-8'))
        except:
            raise TypeError('inputs must be encodable to utf-8')

        #return decrypted text
        return encoded_cipher.decrypt(encoded_text).decode("utf-8")

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -       

#code below will only run if this is the main script ie not being called
#from another script as a module
#below are examples of how to encrypt and decrypt using this module
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == '__main__':

    #encrypt a password and send the encrypted text and cipher key 
    #in seperate text files to the same declared directory
    encrypt.encrypt_text('my_pass', 'd:\\') 

    #open and read in encrypted text
    text_file = open('d:\\encrypted_text.txt', 'r')
    text = text_file.readline()
    text_file.close()

    #open and read in the corresponding cipher
    cipher_file = open('d:\\cipher.txt', 'r')
    cipher = cipher_file.readline()
    cipher_file.close()

    print(encrypt.decrypt_text(text, cipher))
  
''' 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                    end of script
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
'''
    


