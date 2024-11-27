from gtts import gTTS
import os

# Dictionary of languages and their language codes
languages = {
    'English': 'en',
    'Hindi': 'hi',
    'French': 'fr',
    'Spanish': 'es',
    'German': 'de',
    'Tamil': 'ta'
}

# Text to convert to speech
myText = "Welcome to github, Nice to meet you! how can i help you."

# Function to generate speech in a given language
def generate_speech(text, lang_code, filename):
    tts = gTTS(text=text, lang=lang_code, slow=False)
    tts.save(filename)
    print(f"Saved: {filename}")

# Iterate over all selected languages
for lang_name, lang_code in languages.items():
    output_file = f"output_{lang_name}.mp3"
    generate_speech(myText, lang_code, output_file)

# Optionally play the last generated file
os.system(f"start {output_file}")  # Replace with "open" for macOS or "xdg-open" for Linux
