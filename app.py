import streamlit as st
from pdf_reader import extract_text_from_pdf
from chat_engine import LlamaChatEngine
import os

def load_llama_model():
    """
    Lädt das Llama-Modell aus dem 'models/'-Ordner.
    Passen Sie den Dateinamen an Ihr Modell an!
    """
    model_path = os.path.join("models", "YOUR_MODEL_NAME.bin")
    if not os.path.exists(model_path):
        st.error(f"Modell nicht gefunden: {model_path}")
        st.stop()

    st.session_state["chat_engine"] = LlamaChatEngine(model_path=model_path)
    st.success("Lokales Modell erfolgreich geladen!")

def main():
    st.title("📄 Smart PDF Chat Analyzer (Offline)")

    # 1) Modell laden (einmalig)
    if "chat_engine" not in st.session_state:
        with st.spinner("Lade lokales Llama-Modell..."):
            load_llama_model()

    # 2) PDF-Upload
    pdf_file = st.file_uploader("Lade ein PDF hoch", type="pdf")

    if pdf_file:
        text = extract_text_from_pdf(pdf_file)
        st.success("PDF-Inhalt geladen. Stelle jetzt eine Frage!")

        # 3) Frageingabe
        question = st.text_input("Deine Frage zum Dokument:")

        if question:
            # 4) An Llama fragen
            chat_engine = st.session_state["chat_engine"]
            with st.spinner("Denke nach..."):
                answer = chat_engine.ask(context=text, question=question)
            st.markdown("### 💬 Antwort")
            st.write(answer)
    else:
        st.info("Bitte ein PDF hochladen.")

if __name__ == "__main__":
    main()
