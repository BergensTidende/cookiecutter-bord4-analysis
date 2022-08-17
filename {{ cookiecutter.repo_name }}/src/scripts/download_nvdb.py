"""
  The api for NVDB is not available as a package at the monent. 
<<<<<<< HEAD
  This function downloads the api and puts it in the src/nvdbapiv3 folder.
=======
  This function downloads the api and puts it in the src/nvdb folder.
>>>>>>> f9057852fac99743f1a3ee600d2af89c12a6d080

  The api is available at: https://github.com/LtGlahn/nvdbapi-V3/tree/master/nvdbapiv3
"""

import requests
import os
import sys
import logging

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
    logger.info("Remember to create a nvdbapi-clientinfo.json file in the src/nvdbapiv3 folder and it with X-Client and X-Kontaktperson")
    
  else:
    logger.info("The NVDB folder already exists. Delete it and run the script again to download the api")
      

if __name__ == '__main__':
    main()