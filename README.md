# 🧠 Smart PDF Chat Analyzer (Offline LLM)

Ein lokaler KI-gestützter PDF-Chatbot, der PDF-Inhalte analysiert und in natürlicher Sprache beantwortet – **vollständig offline**, ohne Cloud, ohne API-Key.  
Entwickelt mit **Python**, **Streamlit**, **llama-cpp-python** und **PyMuPDF**.

---

## 🚀 Projektübersicht

Dieses Projekt ermöglicht es, ein PDF-Dokument (z. B. Vertrag, Report, E-Book) hochzuladen und in natürlicher Sprache Fragen dazu zu stellen.  
Die Antworten kommen von einem **lokal laufenden LLM (Large Language Model)** wie z. B. TinyLlama, das auf dem Rechner des Users ausgeführt wird.

### 🔐 Kein Cloud-Zwang:
- Keine Registrierung
- Kein API-Key (wie bei OpenAI)
- 100 % lokal & datenschutzfreundlich

---

## 🧱 Technologien

| Funktion | Tool |
|----------|------|
| PDF-Text extrahieren | [`PyMuPDF`](https://pymupdf.readthedocs.io/) |
| Chat-Interface (Frontend) | [`Streamlit`](https://streamlit.io) |
| Offline LLM-Backend | [`llama-cpp-python`](https://github.com/abetlen/llama-cpp-python) |
| Modellformat | GGUF / GGML (z. B. TinyLlama, Mistral, Vicuna) |

---

## 📂 Projektstruktur

```plaintext
SmartPDFChat/
├── app.py               # Streamlit App-Logik & UI
├── pdf_reader.py        # Extrahiert Text aus PDF (mit PyMuPDF)
├── chat_engine.py       # Bindet das lokale LLM über llama-cpp-python ein
├── requirements.txt     # Python-Abhängigkeiten
├── models/              # Lokale LLM-Modelle (.gguf/.ggml)
└── README.md            # Diese Datei

### 📌 Hinweis

Das Projekt befindet sich in aktiver Weiterentwicklung.  
Ein separates, benutzerfreundlicheres Frontend ist bereits in Planung, um die AI-Funktionalität optimal zu präsentieren.
