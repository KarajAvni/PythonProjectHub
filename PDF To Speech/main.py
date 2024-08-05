import fitz
import pyttsx3

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_number in range(doc.page_count):
        page = doc[page_number]
        text += page.get_text()

    return text

def convert_text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    pdf_path = "your_pdf_file.pdf"  # Replace with the path to your PDF file
    pdf_text = extract_text_from_pdf(pdf_path)

    if pdf_text:
        convert_text_to_speech(pdf_text)
    else:
        print("Failed to extract text from the PDF.")
