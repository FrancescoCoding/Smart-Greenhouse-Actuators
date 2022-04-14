from pybleno import Characteristic

class SprinklerStateCharacteristic(Characteristic):
  def __init__(self, uuid):
        Characteristic.__init__(self, {
            'uuid': uuid,
            'properties': ['read', 'write'],
            'value': None
          })
          
        self._value = "OFF"
        self._updateValueCallback = None
        self._sense_hat = SenseHat()

  def onReadRequest(self, offset, callback):

    print('EchoCharacteristic - %s - onReadRequest: value = %s' % (self['uuid'], self._value))
    callback(Characteristic.RESULT_SUCCESS, self._value[offset:])

  def onWriteRequest(self, data, offset, withoutResponse, callback):
    self._value = data.decode("UTF-8")

    print('EchoCharacteristic - %s - onWriteRequest: value = %s' % (self['uuid'], self._value))

    if (self._value == "ON"):
        self._sense_hat.clear((255,255,255))
    else:
        self._sense_hat.clear((0,0,0))

    if self._updateValueCallback:
        print('EchoCharacteristic - onWriteRequest: notifying');
        
        self._updateValueCallback(self._value)
    
    callback(Characteristic.RESULT_SUCCESS)
  
    def onSubscribe(self, maxValueSize, updateValueCallback):
      print('EchoCharacteristic - onSubscribe')
      
      self._updateValueCallback = updateValueCallback

    def onUnsubscribe(self):
        print('EchoCharacteristic - onUnsubscribe');
        
        self._updateValueCallback = None
