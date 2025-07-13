# Word-Genius-System
Word Genius is a vocabulary and brain-training game that challenges players to solve word puzzles, unscramble letters, and improve their English language skills. It’s designed to test your knowledge, boost memory, and expand your vocabulary through fun and interactive levels.



# Word Genius - Advanced Edition

## Description
This is a desktop application built using Python Tkinter and NLTK. It allows users to input (or speak) a word, and displays its definitions, synonyms, and an example sentence. Users can also save their search results and view search history.

## Features
- Word definition lookup using WordNet
- Synonyms listing
- Example usage sentence (if available)
- Voice input using speech recognition
- Save results to `word_output.txt`
- Clear and reset output
- Search history tracker

## Requirements
Install the following Python packages before running:

```bash
pip install nltk speechrecognition pyaudio
```

If you haven’t used NLTK before, run this once in your script:
```python
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
```

## How to Run

1. Open terminal or command prompt.
2. Navigate to the folder where the script is located.
3. Run using:

```bash
python word_genius_advanced.py
```

Make sure your microphone is working for the voice input feature.

## Author
- Developed for academic project (NLP + GUI Based Application)
