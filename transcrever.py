import sys
import os
import whisper
import ollama

# ---------------- Configurações ----------------
MODELO_WHISPER = "base"
MODELO_OLLAMA = "llama3.2"
EXTENSOES_VALIDAS = (".wav", ".mp3")
# -----------------------------------------------


def transcrever_audio(caminho_audio):
    print(f"Carregando modelo Whisper '{MODELO_WHISPER}'...")
    modelo = whisper.load_model(MODELO_WHISPER)

    print("Transcrevendo o áudio (pode demorar um pouco)...")
    resultado = modelo.transcribe(caminho_audio)
    return resultado["text"]


def extrair_pontos_chave(texto):
    prompt = (
        "Leia o texto abaixo e responda em português com um resumo "
        "em tópicos, destacando apenas os pontos-chave.\n\n"
        f"TEXTO:\n{texto}"
    )

    print(f"Gerando resumo com o Ollama ('{MODELO_OLLAMA}')...")
    resposta = ollama.chat(
        model=MODELO_OLLAMA,
        messages=[{"role": "user", "content": prompt}],
    )
    return resposta["message"]["content"]


def main():
    if len(sys.argv) != 2:
        print("Uso: python transcrever.py caminho/do/audio.mp3")
        sys.exit(1)

    caminho_audio = sys.argv[1]

    if not os.path.isfile(caminho_audio):
        print(f"Erro: arquivo '{caminho_audio}' não encontrado.")
        sys.exit(1)
    if not caminho_audio.lower().endswith(EXTENSOES_VALIDAS):
        print("Erro: use um arquivo .wav ou .mp3.")
        sys.exit(1)

    texto = transcrever_audio(caminho_audio)
    print("\n=== TRANSCRIÇÃO ===")
    print(texto)

    pontos_chave = extrair_pontos_chave(texto)
    print("\n=== PONTOS-CHAVE ===")
    print(pontos_chave)

    with open("resultado.txt", "w", encoding="utf-8") as f:
        f.write("TRANSCRIÇÃO\n" + texto + "\n\nPONTOS-CHAVE\n" + pontos_chave)
    print("\nResultado salvo em resultado.txt")


if __name__ == "__main__":
    main()
