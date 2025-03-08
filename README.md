# Sistema de Gestão de Portaria com IA e IoT

Este projeto é parte do Trabalho de Conclusão de Curso (TCC) e consiste em um sistema de gestão de portaria que utiliza Inteligência Artificial (IA) e Internet das Coisas (IoT). O sistema realiza a leitura de placas de veículos através de uma câmera, verifica as informações em um banco de dados e controla a abertura do portão utilizando um Arduino.

## 🚀 Funcionalidades

- **📷 Reconhecimento de Placas**: Captura e processa imagens das placas dos veículos utilizando a biblioteca OpenCV e técnicas de OCR (Reconhecimento Óptico de Caracteres) para extrair as informações das placas.
- **🔍 Verificação de Acesso**: Consulta as informações das placas reconhecidas em um banco de dados para determinar se o veículo tem permissão de acesso.
- **🚪 Controle do Portão**: Envia comandos para um Arduino que controla a abertura ou fechamento do portão com base na verificação de acesso.

## 🛠 Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada para o desenvolvimento do sistema.
- **OpenCV**: Biblioteca de processamento de imagens utilizada para capturar e processar as imagens das placas.
- **Tesseract-OCR**: Tecnologia de OCR utilizada para reconhecer os caracteres das placas.
- **Arduino**: Microcontrolador utilizado para controlar o mecanismo de abertura e fechamento do portão.

## 📂 Estrutura do Projeto

📦 smartentry-ia-python ├── 📁 src │ ├── 📄 reconhecimento_caracter.py # Módulo de OCR para reconhecimento de placas │ ├── 📄 processamento_img.py # Processamento de imagens das placas │ ├── 📄 conexao.py # Comunicação com o Arduino │ ├── 📄 main.py # Script principal do sistema ├── 📄 requirements.txt # Dependências do projeto ├── 📄 README.md # Documentação do projeto


## ⚙️ Pré-requisitos

Antes de executar o projeto, certifique-se de ter os seguintes requisitos instalados:

- Python 3.x instalado.
- Bibliotecas Python necessárias (listadas no `requirements.txt`).
- OpenCV e Tesseract-OCR instalados.
- Arduino configurado com o código adequado para receber os comandos.

## 📥 Instalação

1. **Clone este repositório**:

   ```bash
   git clone https://github.com/JoaoLacerda27/smartentry-ia-python.git
2. **Acesse o diretório do projeto:**
   cd smartentry-ia-python
   
4. **Instale as dependências:**
   pip install -r requirements.txt

## ▶️ Execução

1. Conecte o Arduino ao computador e verifique a porta serial utilizada.
2. Execute o módulo principal do sistema:
   python main.py
3. O sistema iniciará a captura de imagens, realizará o reconhecimento das placas e controlará o portão conforme as permissões configuradas no banco de dados.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias ou correções.


