# Transcrição de Áudio com Whisper e Pontos-Chave com Ollama

## Descrição do projeto

Este projeto é um pipeline em Python que:

1. Recebe um arquivo de áudio (`.wav` ou `.mp3`);
2. Transcreve o conteúdo para texto usando o **Whisper** (OpenAI, código aberto, executado localmente);
3. Envia o texto transcrito ao **Ollama**, que gera um resumo em tópicos com os principais pontos-chave;
4. Exibe o resultado no terminal e o salva no arquivo `resultado.txt`.

Tudo roda localmente, sem necessidade de chaves de API ou serviços pagos.

## Como funciona

```
 áudio (.mp3 / .wav)
        │
        ▼
 ┌───────────────┐      texto       ┌───────────────┐
 │    Whisper    │ ───────────────► │    Ollama     │
 │ (transcrição) │                  │  (resumo com  │
 └───────────────┘                  │ pontos-chave) │
                                    └───────┬───────┘
                                            ▼
                              terminal + resultado.txt
```

## Estrutura de pastas

```
whisper-ollama/
├── data/                  # (opcional) coloque aqui os áudios de teste
│   └── teste.mp3
├── transcrever.py         # script principal
├── requirements.txt       # dependências Python
├── README.md              # este arquivo
└── resultado.txt          # gerado automaticamente após a execução
```

Estrutura do código (`transcrever.py`):

| Função | O que faz |
|---|---|
| `transcrever_audio()` | Carrega o Whisper e converte o áudio em texto |
| `extrair_pontos_chave()` | Envia o texto ao Ollama e retorna o resumo em tópicos |
| `main()` | Valida o arquivo, chama as duas funções, exibe e salva o resultado |

## Pré-requisitos

- **Python 3.9 ou superior**: https://www.python.org/downloads/
- **ffmpeg** (usado pelo Whisper para ler o áudio)
- **Ollama**: https://ollama.com/download

## Instalação

### 1. Baixar o projeto
Na página do repositório no GitHub, clique em **Code > Download ZIP** e extraia a pasta no seu computador.

### 2. Instalar o ffmpeg
- **Windows:** `winget install ffmpeg`
- **Mac:** `brew install ffmpeg`
- **Linux:** `sudo apt install ffmpeg`

Feche e abra o terminal depois de instalar. Para conferir: `ffmpeg -version`

### 3. Instalar o Ollama e baixar o modelo
1. Instale o Ollama pelo link acima e deixe o aplicativo aberto.
2. No terminal, baixe o modelo usado no projeto:
```bash
ollama pull llama3.2
```

### 4. Abrir o terminal na pasta do projeto
```bash
cd caminho/para/whisper-ollama
```

### 5. Criar e ativar o ambiente virtual
```bash
python -m venv venv
```
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

Deve aparecer `(venv)` no início da linha do terminal.

### 6. Instalar as dependências
```bash
pip install -r requirements.txt
```

> No Mac/Linux, se `python` ou `pip` não funcionarem, use `python3` e `pip3`.

## Como executar

Com o ambiente virtual ativo, dentro da pasta do projeto:

```bash
python transcrever.py caminho/do/audio.mp3
```

Na primeira execução, o Whisper baixa o modelo escolhido, o que pode levar alguns minutos.

## Exemplos de uso

**Áudio dentro da pasta `data/`:**
```bash
python transcrever.py data/teste.mp3
```

**Áudio `.wav` na própria pasta do projeto:**
```bash
python transcrever.py gravacao.wav
```

**Exemplo de saída (ilustrativo):**
```
Carregando modelo Whisper 'base'...
Transcrevendo o áudio (pode demorar um pouco)...

=== TRANSCRIÇÃO ===
Hoje vamos falar sobre o Whisper, um modelo de reconhecimento de fala...

Gerando resumo com o Ollama ('llama3.2')...

=== PONTOS-CHAVE ===
- O Whisper transcreve áudio em texto
- Foi lançado em código aberto pela OpenAI
- Pode ser combinado com modelos de linguagem em um mesmo pipeline

Resultado salvo em resultado.txt
```

Se o arquivo não existir ou tiver formato inválido, o script avisa e encerra:
```
Erro: use um arquivo .wav ou .mp3.
```

## Configurações

No topo do `transcrever.py` é possível alterar:

| Variável | Padrão | Descrição |
|---|---|---|
| `MODELO_WHISPER` | `"base"` | `tiny`, `base`, `small`, `medium` ou `large`. Modelos maiores são mais precisos, porém mais lentos. |
| `MODELO_OLLAMA` | `"llama3.2"` | Qualquer modelo baixado no Ollama (`ollama pull nome-do-modelo`). |

## Problemas comuns

| Problema | Solução |
|---|---|
| `ffmpeg not found` | Instale o ffmpeg (passo 2) e reabra o terminal |
| Erro de conexão com o Ollama | Abra o aplicativo do Ollama (ou rode `ollama serve`) |
| `model 'llama3.2' not found` | Rode `ollama pull llama3.2` |
| `No module named 'whisper'` | Ative o ambiente virtual (passo 5) e refaça o passo 6 |
| Avisos sobre `FP16` ou `torch.load` | São apenas avisos, podem ser ignorados |
| Transcrição com muitos erros | Troque `MODELO_WHISPER` para `"small"` ou `"medium"` |

## Tecnologias utilizadas

- [Python](https://www.python.org/)
- [OpenAI Whisper](https://github.com/openai/whisper): reconhecimento de fala
- [Ollama](https://ollama.com/): execução local de modelos de linguagem
