import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
import pygame
from threading import Thread

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speech Translator")
        self.root.geometry("700x600")
        
      
        self.recognizer = sr.Recognizer()
        self.translator = Translator()
        pygame.mixer.init()
        
     
        self.create_modern_widgets()
        
    def create_modern_widgets(self):
      
        main_frame = ctk.CTkFrame(self.root, 
                                  corner_radius=15, 
                                  fg_color=("#f0f0f0", "#2c2c2c"))
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
       
        title_label = ctk.CTkLabel(main_frame, 
                                   text="Smart Speech Translator", 
                                   font=("Arial", 24, "bold"),
                                   text_color=("black", "white"))
        title_label.pack(pady=(20, 30))
        
       
        lang_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        lang_frame.pack(fill="x", padx=30, pady=10)
        
        
        source_label = ctk.CTkLabel(lang_frame, text="Source Language:", font=("Arial", 14))
        source_label.pack(side="left", padx=(0, 10))
        
        self.source_lang = ctk.CTkComboBox(
            lang_frame, 
            values=['English', 'Arabic', 'French', 'Spanish'],
            state="readonly",
            width=200,
            font=("Arial", 12)
        )
        self.source_lang.set('English')
        self.source_lang.pack(side="left")
        
        # Target Language Dropdown
        target_label = ctk.CTkLabel(lang_frame, text="Target Language:", font=("Arial", 14), padx=10)
        target_label.pack(side="right", padx=(20, 10))
        
        self.target_lang = ctk.CTkComboBox(
            lang_frame, 
            values=['English', 'Arabic', 'French', 'Spanish'],
            state="readonly",
            width=200,
            font=("Arial", 12)
        )
        self.target_lang.set('Arabic')
        self.target_lang.pack(side="right")
        
      
        self.record_button = ctk.CTkButton(
            main_frame, 
            text="🎤 Start Recording", 
            command=self.start_recording,
            corner_radius=10,
            font=("Arial", 16, "bold"),
            fg_color="#4CAF50",
            hover_color="#45a049"
        )
        self.record_button.pack(pady=20)
        
        # Text Frames
        text_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        text_frame.pack(fill="x", padx=30, pady=10)
        
        # Source Text
        source_text_label = ctk.CTkLabel(text_frame, text="Original Text:", font=("Arial", 14))
        source_text_label.pack(side="top", anchor="w")
        
        self.source_text = ctk.CTkTextbox(
            text_frame, 
            height=100, 
            corner_radius=10,
            border_width=1,
            font=("Arial", 12)
        )
        self.source_text.pack(fill="x", pady=(5, 10))
        
     
        translated_text_label = ctk.CTkLabel(text_frame, text="Translation:", font=("Arial", 14))
        translated_text_label.pack(side="top", anchor="w")
        
        self.translated_text = ctk.CTkTextbox(
            text_frame, 
            height=100, 
            corner_radius=10,
            border_width=1,
            font=("Arial", 12)
        )
        self.translated_text.pack(fill="x", pady=(5, 10))
        
        
        self.play_button = ctk.CTkButton(
            main_frame, 
            text="▶️ Listen to Translation", 
            command=self.play_translation,
            corner_radius=10,
            font=("Arial", 16, "bold"),
            fg_color="#2196F3",
            hover_color="#1976D2"
        )
        self.play_button.pack(pady=20)
        
    def start_recording(self):
        Thread(target=self.record_audio).start()
        
    def record_audio(self):
        try:
            with sr.Microphone() as source:
                # Update record button state
                self.record_button.configure(text="Recording...", fg_color="#FFC107")
                
                # Clear previous texts
                self.source_text.delete("0.0", "end")
                self.translated_text.delete("0.0", "end")
                
                # Listen for audio
                audio = self.recognizer.listen(source, timeout=5)
                
                # Convert speech to text
                source_lang = self.map_language(self.source_lang.get())
                text = self.recognizer.recognize_google(audio, language=source_lang)
                self.source_text.insert("0.0", text)
                
                # Translate text
                target_lang = self.map_language(self.target_lang.get())
                translated = self.translator.translate(
                    text, 
                    src=source_lang,
                    dest=target_lang
                ).text
                
                self.translated_text.insert("0.0", translated)
                
               
                self.record_button.configure(text="Start Recording", fg_color="#4CAF50")
                
        except sr.UnknownValueError:
            messagebox.showwarning("Warning", "No speech detected")
            self.record_button.configure(text="Start Recording", fg_color="#4CAF50")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.record_button.configure(text="Start Recording", fg_color="#4CAF50")
            
    def map_language(self, language):
       
        language_map = {
            'English': 'en',
            'Arabic': 'ar',
            'French': 'fr',
            'Spanish': 'es'
        }
        return language_map.get(language, 'en')
    
    def play_translation(self):
        try:
            text = self.translated_text.get("0.0", "end").strip()
            if not text:
                messagebox.showwarning("Warning", "No text to translate")
                return

         
            target_lang = self.map_language(self.target_lang.get())
            
         
            tts = gTTS(text=text, lang=target_lang)
            tts.save("translation.mp3")

            pygame.mixer.music.load("translation.mp3")
            pygame.mixer.music.play()

        
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            
            pygame.mixer.music.unload()
            if os.path.exists("translation.mp3"):
                os.remove("translation.mp3")

        except Exception as e:
            messagebox.showerror("Error", f"Error playing audio: {str(e)}")

def main():
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    app = TranslatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
