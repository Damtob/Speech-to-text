import speech_recognition as sr
import pyaudio


def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Please say something...")

        audio = r.listen(source)

        print("Recognition in progress...")

        try:
            print("You said : \n " + r.recognize_google(audio))
            print("Audio recorded successfully")

        except Exception as e:
            print("Error : " + str(e))

    with open("recoded-audio.wav", "wb") as f:
        f.write(audio.get_wav_data())


if __name__ == "__main__":
    main()
