import requests
import json
import os
import playsound

#url = 'http://35.239.180.29:8890/predict'
#url = 'http://216.48.183.17:8090/predict'
#url= 'http://216.48.183.17:8090/predict'#speaker 1
url = 'http://216.48.184.125:8890/predict' #speaker 2
headers = {
    'Content-Type': 'application/json'
}
tempAudioFile='tempAudio.wav'
class SaarthiTTS(object):

    #@staticmethod
    def synthesize(self,text):
        payload = json.dumps({
            "text": text,
            "language": "hi",
            "sample_rate": "8000",
            "length": 0.6,

            "file_name": tempAudioFile
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        with open('tempAudio.wav', 'wb') as f:
            f.write(response.content)
            f.close()
        if os.path.isfile(tempAudioFile):
            print('Speaking...', text)
            playsound.playsound(tempAudioFile)  # playing audio file
            os.remove(tempAudioFile)  # permanently removing the created audio instance/file
            print('audio synthesized successfully!!!')
        else:
            print('audio could not be exported')