import logging
import os 
from datetime import datetime

LOFG_FILE=f"{datetime.now().strftime("%m_%d_%y_%H_%M_%S")}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOFG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOFG_FILE_PATH=os.path.join(logs_path,LOFG_FILE)

logging.basicConfig(
    filename=LOFG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)
