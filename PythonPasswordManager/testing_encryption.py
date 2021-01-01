from Security import Encryptor, PasswordTools

password = "my Password"

# this file exists
unencrypted_file = r"C:\Users\James\source\repos\PythonPasswordManager\encrypt_me.txt"
# this file does not exist yet
encrypted_file = r"C:\Users\James\source\repos\PythonPasswordManager\encrypted_file"
# this file is created by the encryption process
decrypted_file = r"C:\Users\James\source\repos\PythonPasswordManager\dencrypted_file.txt"

salt = PasswordTools.make_salt()

encoded_password = PasswordTools.password_to_bytes(password=password, salt=salt)

# encrypt the file
Encryptor.file_encrypt(encoded_password, unencrypted_file, encrypted_file)

# convert salt to string and
salt_string = PasswordTools.salt_to_string(salt)

# get salt from string
recovered_salt = PasswordTools.string_to_salt_bytes(salt_string)

# try to reconstruct encoded_password with the recovered_salt
reconstructed_password = PasswordTools.password_to_bytes(password=password, salt=recovered_salt)

Encryptor.file_decrypt(reconstructed_password, encrypted_file, decrypted_file)