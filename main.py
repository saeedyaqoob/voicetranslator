import speech_recognition as sr
import pyttsx3
from googletrans import Translator

LANGUAGES = {
    'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani',
    'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan',
    'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)',
    'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english',
    'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian',
    'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole',
    'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian',
    'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese',
    'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish',
    'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori',
    'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'ps': 'pashto',
    'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian',
    'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi',
    'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese',
    'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish',
    'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish',
    'yo': 'yoruba', 'zu': 'zulu', 'fil': 'Filipino', 'he': 'Hebrew'
}

# init the recognizer, microphone, engine, exit condition, GoogleAPI translator
recognizer = sr.Recognizer()
microphone = sr.Microphone()
translator = Translator()
engine = pyttsx3.init()
translating = True
MyText = None

# Initialize input and output languages
input_language = 'en'
output_language = 'es'


# Function to convert text to speech
def TextToSpeech(text):
    global engine
    engine.say(text)
    engine.runAndWait()


# Function to convert speech to text
def SpeechToText(source):
    global recognizer
    with source as audio_source:
        recognizer.adjust_for_ambient_noise(audio_source, duration=0.2)
        audio = recognizer.listen(audio_source)
        text = recognizer.recognize_google(audio)
        text = text.lower()
        return text


# Function to translate
def translate(sentence):
    global input_language, output_language, translator
    result = translator.translate(sentence, src=input_language, dest=output_language)
    return [result.text, result.pronunciation]


# Main loop
while translating:
    try:
        print('-----------------------------------------\n')
        print('Speak Now...!\n')
        # Pass input from microphone to SpeechToText function
        MyText = SpeechToText(microphone)
        print(f'Your voice input:\n{MyText}\n')
        if MyText == 'exit':
            print('-----------------------------------------\n')
            translating = False
        else:
            translated_text, pronunciation = translate(MyText)[0], translate(MyText)[1]
            if MyText == pronunciation:
                TextToSpeech(translated_text)
                print(f'Translated text:\n{translated_text}\n')
                print(f'Pronunciation:\n{translated_text}\n')
                print('-----------------------------------------\n')
            else:
                TextToSpeech(pronunciation)
                print(f'Translated text:\n{translated_text}\n')
                print(f'Pronunciation:\n{pronunciation}\n')
                print('-----------------------------------------\n')

    except sr.RequestError as error:
        print(f'Error:\n{error}\n')
        print('-----------------------------------------\n')

    except sr.UnknownValueError as error:
        print(f'Error:\n{error}\n')
        print('-----------------------------------------\n')
