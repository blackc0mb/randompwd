from pwd import pwd

password = pwd()
nopass = input('Number of passwords? ')
password.set_numpasswords(nopass)
length = input('Password length? ')
password.set_length(length)

ret_passwords = password.get_passwords()
print(ret_passwords)
