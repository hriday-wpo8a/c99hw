import os 
import shutil
import time
def main():
    deleted_folder_count =0
    deleted_file_count =0

    path="/Users/matha/Dropbox/My PC (LAPTOP-J9AF6618)/Desktop/test folder/"

    days = 30

    seconds = time.time()-(5)

    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            if seconds>= get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deleted_folder_count+=1
                break
            else:
                for folder in folders:
                    folder_path  = os.path.join(root_folder,folder)
            
                    if seconds>= get_file_or_folder_age(root_folder):
                        remove_folder(root_folder)
                        deleted_folder_count+=1
                for files in files: 
                    file_path  = os.path.join(root_folder,file)
            
                    if seconds>= get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deleted_file_count+=1

        else :
             if seconds>= get_file_or_folder_age(path):
                remove_file(path)
                deleted_file_count+=1
    else:
        print("path not found")
    print(deleted_folder_count , deleted_file_count)
def remove_folder(path):
    if not shutil.rmtree(path):
        print("folder removed successfully")

    else: 
        print("unable to delete")

def remove_file(path):
    if not os.remove(path):
        print("file removed successfully")

    else: 
        print("unable to delete")

def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime
if __name__ =='__main__':
    main()