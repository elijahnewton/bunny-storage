import os
import requests
from pathlib import Path
from requests.exceptions import HTTPError
from dotenv import  load_dotenv

load_dotenv()

ftp_key = os.getenv('FTP_KEY')


# BunnyCDN Storage Class
class BunnyCDNStorage:
    def __init__(self):
        self.apikey = ftp_key
        self.storage_zone = 'file-share1'
        self.pull_zone = 'file-share1'
        self.base_url = f'https://jh.storage.bunnycdn.com/{self.storage_zone}/'
        self.headers = {
            'AccessKey': self.apikey,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    
    from requests.exceptions import HTTPError

    def download_file(self, file_url, destination_path):
        file_url =file_url
        file_name = file_url.split("/")[-1]
        download_path = Path(destination_path, file_name)

        try:
            with requests.get(file_url, headers=self.headers, stream=True) as response:
                response.raise_for_status()
                with open(download_path, "wb") as f:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                return response.status_code
        except HTTPError as error:
            return error

    def upload_file(self, storage_path, file_content, file_name):
        storage_url = f'{self.base_url}{storage_path}{file_name}'
        
        try:
            with requests.put(storage_url, data=file_content, headers=self.headers) as response:
                response.raise_for_status()
                cdn_url = f'https://{self.pull_zone}.b-cdn.net/{storage_path}{file_name}'
                return cdn_url
        except HTTPError as error:
            return error

    def object_exists(self, file_url):
        print(file_url)
        response = requests.head(file_url, headers=self.headers)
        return response.status_code == 200

    def delete_object(self, file_url):
        file_url = file_url
        
        try:
            with requests.delete(file_url, headers=self.headers) as response:
                response.raise_for_status()
                return response.status_code
        except HTTPError as error:
            return error