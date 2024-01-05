# by m1lean
from googletrans import Translator

def translate_text(text, target_language):
     translator = Translator()
     translation = translator.translate(text, dest=target_language)
     return translation.text

def main():
     # Enter text for translation
     text_to_translate = input("Enter text to translate: ")

     # Select the language to translate the text into
     target_language = input("Select the target language (for example, 'es','en','ru'): ")

     # Text translation
     translated_text = translate_text(text_to_translate, target_language)

     # Output the result
     print("Translated text:", translated_text)

if __name__ == "__main__":
     main()