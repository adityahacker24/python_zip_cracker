import zipfile
import os

#getting path of files required
w_list = input("$ Enter the path of word_list : ")
w_list_nme = input("\n$ Enter the name of word_list file : ")
com_w_list = os.path.join(w_list,w_list_nme)

z_file = input("\n$ Enter the path of zip_file : ")
z_file_nme = input("\n$ Enter the name of zip file : ")
com_z_file = os.path.join(z_file,z_file_nme)

sve_path = input("\n$Enter the path to extract zip file : ")

#file names 
pwd_filename = com_w_list
filename="chromedriver_win32.zip"
zip_filename = com_z_file

#read passwords_list file in binary mode
with open(pwd_filename, "rb") as passwords:
    
    #convert all the passwords into a list 
    passwords_list = passwords.readlines()
    
    #total number of passwords
    total_passwords = len(passwords_list)

    #load zipfile
    my_zip_file = zipfile.ZipFile(zip_filename)
    
    for index, password in enumerate(passwords_list):
        #try if password is correct
        try:
            my_zip_file.extractall(path=sve_path,  pwd=password.strip())
            print("\n$ ++++ [ SUCCESS ] ++++")
            print("$ Password Found: ", password.decode().strip())
            print("$ All Files has been Extracted inside the New DIrectory Extracted Folder")
            break
        
        #if password fails
        except:
            
            print(f"!................Scanning complete {round((index/total_passwords)*100, 2)}%")
            print(f"\n Trying password {password.decode().strip()} ")
            print("!!!!!!!! [ FAIL ] !!!!!!!!\n")
            continue