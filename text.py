import os
from google.cloud import speech

# Set your Google Cloud project credentials environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/your/credentials.json"


def transcribe_audio(audio_file):
    # Instantiates a client
    client = speech.SpeechClient()

    # Loads the audio file into memory
    with open(audio_file, "rb") as f:
        audio = speech.RecognitionAudio(content=f.read())

    # Configure the speech recognition request
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    # Performs speech recognition on the audio file
    response = client.recognize(config=config, audio=audio)

    # Process the response
    results = []
    for result in response.results:
        transcript = result.alternatives[0].transcript
        confidence = result.alternatives[0].confidence
        results.append({"transcript": transcript, "confidence": confidence})

    return results


# Specify the path to your audio file
audio_file_path = "record 1.m4a"

# Transcribe the audio file
transcripts = transcribe_audio(audio_file_path)

# Print the results
for transcript in transcripts:
    print("Transcript:", transcript["transcript"])
    print("Confidence:", transcript["confidence"])
    print()
