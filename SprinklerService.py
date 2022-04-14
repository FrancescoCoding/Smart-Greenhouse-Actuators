from pybleno import *
from SprinklerStateCharacteristic import *

class SprinklerService(BlenoPrimaryService):
    def __init__(self):
        BlenoPrimaryService.__init__(self, {
          'uuid': '2A78', 
          'characteristics': [
              SprinklerStateCharacteristic("2A78")
          ]})