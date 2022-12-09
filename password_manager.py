from cryptography.fernet import Fernet

mst_password=input("enter master password: ")

psw=input()
key=Fernet.generate_key()
crypter=Fernet(key)
pasw=crypter.encrypt(bytes(psw,'UTF8'))
decryptstr=crypter.decrypt(pasw)
print(str(pasw,'UTF8'))
print(str(decryptstr,'UTF8'))


def view():
    with open("password.txt",'r') as f:
        for line in f.readlines():
            line=line.rstrip()
            user,psw=line.split("|")
            print("user: ",user,"| password: ",psw)

def add():
    user=input("enter username: ")
    psw=input("enter password: ")
    
    with open("password.txt","a") as f:
        f.write(user+'|'+psw+'\n')

while True:
    mode=input("would you like to add a new password or to view existing one ? (view/add/ 'q' for quit) ").lower()
    if mode=='q':
        break
    elif mode=='add':
        add()
    elif mode=='view':
        view()
    else:
        print("invalid option")