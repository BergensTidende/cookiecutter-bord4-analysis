"""
  The api for NVDB is not available as a package at the monent. 
  This function downloads the api and puts it in the src/nvdbapiv3 folder.

  The api is available at: https://github.com/LtGlahn/nvdbapi-V3/tree/master/nvdbapiv3
"""

import requests
import os
import sys
import logging
import json


_log_fmt = '%(asctime)s - %(module)s - %(levelname)s - %(message)s'
logging.basicConfig(level=os.environ.get('LOGLEVEL', 'INFO'), format=_log_fmt)
_MODULE = sys.modules[__name__]
logger = logging.getLogger(__name__)

def main():
  PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
  NVDB_DIRECTORY = os.path.join(PROJECT_DIRECTORY, "src", "nvdbapiv3")
  
  NVDB_URL = "https://raw.githubusercontent.com/LtGlahn/nvdbapi-V3/master/nvdbapiv3/"
  

  # Check whether the specified path exists or not
  nvdbExist = os.path.exists(NVDB_DIRECTORY)

  if not nvdbExist:
    # Create the directory
    os.makedirs(NVDB_DIRECTORY)
    logger.info("Created the directory: {}".format(NVDB_DIRECTORY))
    
    files = [
      "__init__.py",
      "apiforbindelse.py",
      "nvdbapiv3.py"
    ]
    
    # Download the files
    for file in files:
      new_file_path = os.path.join(NVDB_DIRECTORY, file)
    
      r = requests.get(f"{NVDB_URL}{file}", allow_redirects=True)
      content = r.text
      
      if file == "nvdbapiv3.py":
        logger.info("Fixing the import in the nvdbapiv3.py file")
        search_text = "from . import apiforbindelse"
        replace_text = "import apiforbindelse"
        content = content.replace(search_text, replace_text)
      
      open(new_file_path, 'wb').write(content.encode())
      
      logger.info("Downloaded the file: {}".format(file))
    
    logger.info("The NVDB api has been downloaded and are available in the src/nvdbapiv3 folder")
    
    new_file_path = os.path.join(NVDB_DIRECTORY, "nvdbapi-clientinfo.json")
    with open(new_file_path, "w") as f:
      contact_data = {"X-Client": "", "X-Kontaktperson": ""}
      json.dump(contact_data, f, indent=2)
      logger.info("The nvdbapi-clientinfo.json has been created in the src/nvdbapiv3 folder. Open it and fill out X-Client and X-Kontaktperson")
    
  else:
    logger.info("The NVDB folder already exists. Delete it and run the script again to download the api")
      

if __name__ == '__main__':
    main()