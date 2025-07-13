
import tkinter as tk
from nltk.corpus import wordnet
import nltk
import speech_recognition as sr

# Optional: Uncomment the first time to download
# nltk.download('wordnet')
# nltk.download('omw-1.4')

history = []

def get_definitions():
    word = entry.get().strip().lower()
    output.delete("1.0", tk.END)
    if not word:
        output.insert(tk.END, "Please enter a word.")
        return
    if word not in history:
        history.append(word)
    synsets = wordnet.synsets(word)
    if not synsets:
        output.insert(tk.END, f"No definitions found for '{word}'.")
        return
    output.insert(tk.END, f"Definitions for '{word}':\n\n")
    for i, syn in enumerate(synsets[:5], 1):
        output.insert(tk.END, f"{i}. Definition: {syn.definition()}\n")
        synonyms = ", ".join(set(lemma.name() for lemma in syn.lemmas()))
        output.insert(tk.END, f"   Synonyms: {synonyms}\n")
        examples = syn.examples()
        if examples:
            output.insert(tk.END, f"   Example: {examples[0]}\n")
        output.insert(tk.END, "\n")

def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        output.insert(tk.END, "🎤 Listening...\n")
        try:
            audio = recognizer.listen(source, timeout=5)
            word = recognizer.recognize_google(audio)
            entry.delete(0, tk.END)
            entry.insert(0, word)
            get_definitions()
        except:
            output.insert(tk.END, "❌ Could not recognize your voice.\n")

def save_to_file():
    content = output.get("1.0", tk.END)
    if content.strip():
        with open("word_output.txt", "w") as file:
            file.write(content)
        output.insert(tk.END, "\n✔ Saved to 'word_output.txt'")

def clear_output():
    entry.delete(0, tk.END)
    output.delete("1.0", tk.END)

def show_history():
    output.delete("1.0", tk.END)
    if not history:
        output.insert(tk.END, "No word history yet.")
    else:
        output.insert(tk.END, "🔁 Words You've Searched:\n\n")
        for word in history:
            output.insert(tk.END, f"- {word}\n")

root = tk.Tk()
root.title("Word Genius - Advanced")
root.geometry("600x450")
tk.Label(root, text="Enter a word:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack()
tk.Button(root, text="🔍 Find Definitions", command=get_definitions, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="🎤 Speak", command=voice_input, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="📄 Save to File", command=save_to_file, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="🧹 Clear", command=clear_output, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="📜 Show History", command=show_history, font=("Arial", 12)).pack(pady=5)
output = tk.Text(root, height=12, width=70, wrap=tk.WORD, font=("Arial", 10))
output.pack(padx=10, pady=10)
root.mainloop()
