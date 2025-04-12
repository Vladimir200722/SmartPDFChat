from llama_cpp import Llama

class LlamaChatEngine:
    def __init__(self, model_path: str):
        """
        Lädt das lokale Llama-Modell von 'model_path'.
        """
        self.llm = Llama(
            model_path=model_path,
            # n_ctx = 2048,    # ggf. anpassbar, je nach Modell
            # use_mlock=True,  # evtl. auf Windows problematisch
        )

    def ask(self, context: str, question: str) -> str:
        """
        Stellt eine Frage an das Llama-Modell, mit 'context' als Systemprompt.
        """
        prompt = f"""
        Du bist ein KI-Assistent, der Fragen zu einem PDF-Dokument beantwortet.
        Kontext:
        {context}

        Frage: {question}
        Antwort:
        """

        # Der 'prompt' wird an das Modell übergeben
        response = self.llm(
            prompt=prompt,
            max_tokens=256,
            stop=["\nQ:", "\nFrage:"],  # grober Stopp
            echo=False,
            temperature=0.2,
        )

        # 'content' ist die generierte Antwort
        generated_text = response["choices"][0]["text"]
        return generated_text.strip()
