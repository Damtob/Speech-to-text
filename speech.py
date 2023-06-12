import pocketsphinx as ps


def speech_to_text(audio_file):
    # Set up pocketsphinx configuration
    config = ps.Decoder.Config()
    config.set_string('-hmm', '/record 1.m4a')  # Update with the path to the acoustic model
    config.set_string('-dict', '/record 1.m4a')  # Update with the path to the language dictionary
    config.set_string('-lm', '/record 1.m4a')  # Update with the path to the language model

    # Create decoder using the configuration
    decoder = ps.Decoder(config)

    # Open the audio
    with open(audio_file, 'rb') as f:
        # Decode the audio file
        decoder.start_utt()
        while True:
            buf = f.read(1024)
            if buf:
                decoder.process_raw(buf, False, False)
            else:
                break
        decoder.end_utt()

    # Get the transcribed speech
    hypothesis = decoder.hyp()
    if hypothesis is not None:
        return hypothesis.hypstr
    else:
        return None


# Specify the path to your audio file
audio_file = 'record 1.m4a'
result = speech_to_text(audio_file)
print(result)
