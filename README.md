Project Title:
Audio book using python

Project Overview:
This project extends the functionality of a PDF text-to-speech converter by incorporating sentiment analysis and keyword interaction features. It enables users to convert text content from PDF files into speech while dynamically adjusting speech speed based on sentiment polarity. Additionally, users can specify keywords or phrases that, when encountered during speech synthesis, prompt the program to pause, allowing user interaction before resuming reading.

Features:
PDF Text Extraction
    -Reads text content from PDF files, supporting multi-page documents.
Text-to-Speech Synthesis: 
    -Utilizes the `pyttsx3` library to convert the extracted text into speech, enhancing accessibility and convenience.
Sentiment Analysis:
    -Analyzes the sentiment polarity of the text using the `TextBlob` library, adjusting speech speed dynamically to reflect emotional tones.
Keyword Interaction:
    -Allows users to specify keywords or phrases that trigger pauses during speech synthesis, enabling user interaction or intervention.
Configurable Parameters:
    -Provides flexibility for users to customize parameters such as speech speed, volume, pause between pages, and keywords.
Feedback Mechanism:
    -Offers feedback messages to inform users about the progress of the text-to-speech conversion and interactions.

Implementation:
- The project is implemented in Python, leveraging libraries such as `PyPDF2`, `pyttsx3`, and `TextBlob`.
- Modular design encapsulates functionality into reusable functions, promoting maintainability and extensibility.
- Utilizes natural language processing techniques for sentiment analysis and keyword detection, enhancing the reading experience.

Usage:
- Users specify the PDF file to be read, along with optional parameters such as speech speed, volume, pause between pages, and keywords.
- The program provides feedback during the text-to-speech conversion process, indicating progress and interaction points.
- Users can interact with the program by responding to prompts triggered by specified keywords, enabling flexible navigation and engagement.

Potential Extensions:
- Integration with additional NLP techniques for advanced text analysis and comprehension.
- Support for diverse input formats such as DOCX, TXT, or web content, expanding compatibility and usability.
- Incorporation of voice recognition for hands-free interaction and accessibility enhancements.
- Implementation of bookmarking or annotation features for personalized reading experiences.

