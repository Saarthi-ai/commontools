from SaarthiTTS import SaarthiTTS
from TextProcessor import TextProcessor
print('*************** Saarthi Hindi TTS *************** ')
srTTS=SaarthiTTS()
txtPro=TextProcessor()
while True:
    print('<<< Saarthi TTS: Provide your text below >>>')
    strs=input()
    print('waiting...')
    if strs!='exit-':
        strs=txtPro.toDeva(strs)
        srTTS.synthesize(strs)
    elif strs =='exit-':
        print('SaarthiAI Hindi TTS terminated!')
        break