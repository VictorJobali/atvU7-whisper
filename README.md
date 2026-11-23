# Transcrição de Áudio com Whisper + Pontos-Chave com Ollama

## Descrição
Este projeto recebe um arquivo de áudio (`.wav` ou `.mp3`), transcreve o conteúdo
usando o **Whisper** (OpenAI) e envia o texto ao **Ollama**, que devolve um resumo
com os principais pontos-chave. O resultado também é salvo em `resultado.txt`.

## Pré-requisitos
- Python 3.9+
- [ffmpeg](https://ffmpeg.org/download.html) instalado (o Whisper precisa dele)
- [Ollama](https://ollama.com/download) instalado e em execução

## Instalação

```bash
# 1. Clone o repositório
git clone <URL-DO-SEU-REPOSITORIO>
cd <NOME-DA-PASTA>

# 2. (Opcional) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Baixe o modelo do Ollama
ollama pull llama3.2
```

## Como executar

```bash
python transcrever.py caminho/do/audio.mp3
```

## Exemplo de uso

```bash
python transcrever.py data/aula.mp3
```

Saída esperada:

```
=== TRANSCRIÇÃO ===
Hoje vamos falar sobre inteligência artificial...

=== PONTOS-CHAVE ===
- IA é a área que cria sistemas capazes de aprender
- ...
```

## Configurações
No topo do `transcrever.py` você pode trocar:
- `MODELO_WHISPER`: `tiny`, `base`, `small`, `medium` ou `large` (maiores são mais precisos, porém mais lentos).
- `MODELO_OLLAMA`: qualquer modelo que você tenha baixado no Ollama.

## Problemas comuns
- **`ffmpeg not found`**: instale o ffmpeg e reinicie o terminal.
- **Erro de conexão com o Ollama**: abra o app do Ollama (ou rode `ollama serve`).
