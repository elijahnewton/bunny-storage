# bunny-storage
#this repository is to help python developers connect to the bunny storage services in their program or app.
All you need to use this module is to install the:
[requests, dotenv and pathlib] modules in your environment using the pip command
put the bunny.py file in the main directory of your application together with the bunny-test.py
run the bunny-test.py file to make sure everything is working as expected.
import the bunny file into the file where you want to access your bunnyCDN: using: 
from bunny import BunnyCDNStorage
make sure that you follow the format used in the bunny-test.py file
make sure that in your parent directory, you have a '.env' file which should contain your FTP key from bunny storage API/FTP Keys.In the format FTP_KEY='your-api-key'
and go on to use the different functionalities provided by this module.eg
