# Smart Speech Translator 🎤🔄

A modern speech translation app built with Python. This application enables users to record speech, translate it into another language, and listen to the translated audio.

---

## ✨ Features
- ⏳ Real-time **speech-to-text** conversion.
- 🌐 Translation between multiple languages (**English**, **Arabic**, **French**, **Spanish**).
- 🎧 **Text-to-speech** playback for the translated content.
- 🔧 Intuitive and modern **GUI** using `customtkinter`.

---

## 📚 Technologies Used
- **Python**: The core programming language.
- **Libraries**:
  - 🔹 `customtkinter`: For creating the graphical user interface.
  - 🔹 `speech_recognition`: For recognizing speech from the microphone.
  - 🔹 `googletrans`: For translating text between languages.
  - 🔹 `gtts`: For converting text to speech.
  - 🔹 `pygame`: For playing audio files.

---

## 🔄 How to Run
1. Install the required libraries:
   ```bash
   pip install customtkinter speechrecognition googletrans==4.0.0-rc1 gtts pygame
    ```
2. Run the application:
    ```bash
    python translator_app.py
    ```
3. Use the app to record, translate, and play translations.

## 🔜 Future Improvements
- ➕ Add more language options.
- 🌐 Improve error handling for better user experience.
- 📝 Add a feature to save translations locally.

## 🔒 License
 - This project is licensed under the MIT License. See the LICENSE file for details.
