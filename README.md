# Gutenberg Text Cleaner

A Flask web application that allows users to fetch, clean, analyze, and summarize texts from Project Gutenberg URLs. This project is part of CSE 510's Scaffolding Assignment 3 on text preprocessing and web development.

---

## Overview

This web service fetches raw text from Project Gutenberg or any `.txt` URL, preprocesses the text by cleaning headers and footers, normalizes and tokenizes the text, and provides basic statistics along with a three-sentence summary. The project includes:

- A Flask backend with two API endpoints (`/api/clean` and `/api/analyze`)
- A simple and clean frontend interface to submit URLs and display results
- Text preprocessing methods implemented in `starter_preprocess.py`
- Integration of frontend and backend for real-time cleaning and analysis

---

## Setup Instructions

1. **Clone your forked GitHub repository and create a Codespace in GitHub**

2. **Install dependencies**

      pip install -r requirements.txt


3. **Verify your environment**

      python test_setup.py

Ensure all tests pass before proceeding.

4. **Run the Flask web application**



5. **Open your browser**
Navigate to [http://localhost:5000](http://localhost:5000) to access the application.

---

## Usage

- Enter a valid Project Gutenberg `.txt` URL or any accessible `.txt` URL in the input field.
- Click **Clean & Analyze Text**.
- View summary, cleaned text (first 500 characters), and detailed statistics including:
- Total characters
- Total words
- Total sentences
- Average word length
- Average sentence length
- Top 10 most common words

---

## Features Completed

### Part 2: Text Preprocessor
- `fetch_from_url(url: str) -> str`: Fetches raw text from `.txt` URLs.
- `get_text_statistics(text: str) -> Dict`: Computes text statistics including counts and averages.
- `create_summary(text: str, num_sentences: int = 3) -> str`: Extracts an extractive summary by returning the first N sentences.

### Part 3: Flask API
- `/api/clean`: Accepts a URL as JSON, returns cleaned text with statistics and summary.
- `/api/analyze`: Accepts raw text as JSON, returns text statistics.

### Part 4: Frontend
- Clean and modern UI with form validation.
- Displays loading state, error messages, and results dynamically.
- Sample example URLs for quick testing.

---

## Example URLs to Test

- [Pride and Prejudice by Jane Austen](https://www.gutenberg.org/files/1342/1342-0.txt)
- [Frankenstein by Mary Shelley](https://www.gutenberg.org/files/84/84-0.txt)
- [Alice in Wonderland by Lewis Carroll](https://www.gutenberg.org/files/11/11-0.txt)
- [Moby Dick by Herman Melville](https://www.gutenberg.org/files/2701/2701-0.txt)

---

## Screenshots

_Add screenshots of your application’s working interface and results here_

---









