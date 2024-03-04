import os
from bunny import BunnyCDNStorage

url=''
# create file with content
with open('test_upload.txt', "w") as file:
    file.write('HELLO WORLD!')

# check file was created
print(f'.path.exists:{os.path.exists('test_upload.txt')}')

# check file content
with open('test_upload.txt', "r") as file:
    print(file.read())

# initiate class
cdn = BunnyCDNStorage()

# upload to Bunny CDN
file_path = 'test_upload.txt'
file_name = file_path.split('/')[-1]
if os.path.exists(file_path):
    with open(file_path, "rb") as file:
        url = cdn.upload_file('files1/', file, file_name)
        print(url)

# remove file from server
os.remove('test_upload.txt')

# check file still exists on server
print(os.path.exists('test_upload.txt'))

# download from bunny net
file_path = 'test_upload.txt'
try:
    file_binary = cdn.download_file(url, '.')
    with open('test_upload.txt', "r") as file:
        print(file.read())
except Exception as e:
    print("An error occurred:", e)
    # Handle the exception appropriately

# check if file exists on bunny
check = cdn.object_exists(url)
print(check)

# 3. delete from bunny net 
cdn.delete_object(url)
check = cdn.object_exists(url)
print(check)

# check if file exists on bunny
check = cdn.object_exists(url)
print(check)

# remove file from server
os.remove('test_upload.txt')