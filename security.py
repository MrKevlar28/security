from os import access
import dropbox
import cv2
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time()
        result = False
    
    return img_name

    print("Snapshot Taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.BHci0VVjCLz32ll9JfFcgj7CXqn7JzKZSZNMvy4mLm_wN_YB-5FwjqpdkU2d24goNg8_yibA6jgCQ2VKCfy0A5BZz5aeYCcacupKafLxiMmK5ItgPY8l2677uLd5IYFOHyDFg8M"
    file = img_name
    file_from = file
    file_two = "/newFolder1/" + (img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(), file_two, mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")


def main(): 
    while(True): 
        if ((time.time() - start_time) >= 5): 
            name = take_snapshot() 
            upload_file(name) 
            
            
main()
