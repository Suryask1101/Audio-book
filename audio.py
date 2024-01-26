import PyPDF2
import pyttsx3
import time
from textblob import TextBlob

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return polarity

def read_pdf_to_audio(pdf_file, keywords=[], speed=150, volume=1.0, pause_between_pages=2):
    # Open the PDF file
    with open(pdf_file, 'rb') as file:
        # Create a PDF reader object
        read_pdf = PyPDF2.PdfFileReader(file)

        # Initialize pyttsx3
        speaker = pyttsx3.init()

        # Set properties
        speaker.setProperty('rate', speed)    # Speed of speech
        speaker.setProperty('volume', volume)   # Volume (0.0 to 1.0)

        # Iterate through each page in the PDF
        for page_number in range(read_pdf.numPages):
            # Extract text from the page
            text = read_pdf.getPage(page_number).extractText()

            # Get sentiment polarity of the text
            polarity = get_sentiment(text)

            # Adjust speech speed based on sentiment polarity
            adjusted_speed = speed + (polarity * 50)  # Adjust speed by 50 wpm per polarity unit

            # Speak the extracted text
            for phrase in text.split("."):  # Split text into phrases
                speaker.say(phrase.strip())
                speaker.runAndWait()
                # Check for keywords and pause if found
                if any(keyword.lower() in phrase.lower() for keyword in keywords):
                    input("Press Enter to continue...")

            # Set speech speed
            speaker.setProperty('rate', adjusted_speed)

            # Add a pause between pages
            time.sleep(pause_between_pages)

        # Shutdown the pyttsx3 engine
        speaker.stop()
        speaker.quit()

if __name__ == "__main__":
    pdf_file = 'novel.pdf'
    speed = 150
    volume = 1.0
    pause_between_pages = 2
    keywords = ["chapter", "end of chapter"]

    print(f"Reading {pdf_file}...")
    read_pdf_to_audio(pdf_file, keywords, speed, volume, pause_between_pages)
    print("Reading completed.")
