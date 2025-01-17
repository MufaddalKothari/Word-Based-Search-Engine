import sys
import os
 
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to
# the sys.path.
sys.path.append(parent)

from constants.global_constants import GC
import os
import json

from services.app_service import AppService


class InitializeApp:

    def __init__(self):

        GC.INDEXEDWORDS = self.loadIndex()

    def loadIndex(self):

        index_file_path = os.path.join(os.path.join(
            os.getcwd(), GC.DATASET_FOLDER), GC.JSON_FILE)

        print(index_file_path)

        mode = 'r+' if os.path.exists(index_file_path) else 'w+'

        index_file = {}
        with open(index_file_path, mode) as idxfile:
            try:
                index_file = json.load(idxfile)
            except:
                print("Index File is Blank or of wrong format, Trying to index it")
                if AppService().isIndexed():
                    print("Indexed Successfully")
                else:
                    print("Cant Index")
            # print(index_file, type(index_file))
            return index_file
