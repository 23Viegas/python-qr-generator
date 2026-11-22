# Python QR Generator

**Gerador de QR Codes personalizados desenvolvido com Python e Streamlit.**

Uma aplicação web simples, intuitiva e responsiva que permite gerar QR Codes a partir de textos ou links, personalizar suas cores e baixar o resultado em formato PNG.

[**🚀 Acessar aplicação**](https://python-qr-generator.streamlit.app/) | [**💻 Ver repositório**](https://github.com/23Viegas/python-qr-generator)

---

## 📸 Demonstração

Acesse a aplicação online e experimente todas as funcionalidades:

**https://python-qr-generator.streamlit.app/**

### Capturas de tela

![Captura de tela 1](screenshots/image1.png)

---

## ✨ Funcionalidades

- **Geração de QR Codes:** transforme textos e URLs em códigos QR.
- **Personalização de cores:** escolha a cor do QR Code e a cor de fundo.
- **Visualização instantânea:** visualize o resultado diretamente na aplicação.
- **Download em PNG:** baixe os códigos gerados para utilizar em outros projetos.
- **Interface intuitiva:** experiência simples, desenvolvida com Streamlit.
- **Acesso online:** utilize a ferramenta diretamente pelo navegador, sem necessidade de instalação.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem principal do projeto |
| Streamlit | Desenvolvimento da interface web |
| qrcode | Geração dos códigos QR |
| Pillow (PIL) | Manipulação e processamento das imagens |
| Git e GitHub | Versionamento e hospedagem do código |
| Streamlit Community Cloud | Hospedagem da aplicação |

---

## 📂 Estrutura do projeto

```text
python-qr-generator/
├── assets/
│   └── logo.png
├── screenshots/
│   ├── image1.png
│   ├── image2.png
│   ├── image3.png
│   └── image4.png
├── src/
│   ├── app.py
│   └── generator.py
├── .gitignore
├── README.md
└── requirements.txt
```

**Principais arquivos:**

- `src/app.py`: interface da aplicação, campos de entrada, personalização e download.
- `src/generator.py`: lógica responsável pela geração dos QR Codes.
- `assets/`: recursos visuais e identidade do projeto.
- `screenshots/`: capturas de tela utilizadas na documentação.
- `requirements.txt`: dependências necessárias para executar o projeto.

---

## 🚀 Executando localmente

### Pré-requisitos

- Python 3.10 ou superior (recomendado)
- Git
- pip

### 1. Clone o repositório

```bash
git clone https://github.com/23Viegas/python-qr-generator.git
```

### 2. Acesse a pasta do projeto

```bash
cd python-qr-generator
```


### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
python -m streamlit run src/app.py
```

A aplicação será disponibilizada localmente, normalmente em:

`http://localhost:8501`

---

## 📖 Como utilizar

1. Acesse a [aplicação online](https://python-qr-generator.streamlit.app/).
2. Digite ou cole o texto ou link desejado.
3. Escolha as cores do QR Code e do fundo.
4. Clique em **Gerar QR Code**.
5. Visualize o resultado.
6. Clique em **Baixar QR Code** para salvar a imagem PNG.

---

## 🧠 Objetivo do projeto

O Python QR Generator foi desenvolvido com o objetivo de aplicar conhecimentos de programação Python no desenvolvimento de uma aplicação web funcional.

Durante o desenvolvimento, foram trabalhados conceitos como:

- Organização e modularização do código Python.
- Criação de funções e passagem de parâmetros.
- Desenvolvimento de interfaces com Streamlit.
- Manipulação de imagens utilizando Pillow.
- Processamento de arquivos em memória com `BytesIO`.
- Gerenciamento de dependências e ambientes virtuais.
- Versionamento de código com Git e GitHub.
- Publicação de aplicações na nuvem.

Além de oferecer uma ferramenta prática, o projeto faz parte do meu portfólio de desenvolvimento de software.

## 👨‍💻 Autor

**Felipe Sousa Viegas**

Estudante de Técnico em Eletrônica e entusiasta de programação, desenvolvimento de software e inteligência artificial.

**GitHub:** [@23Viegas](https://github.com/23Viegas)

---

## 🌐 Experimente o projeto

**[Acessar Python QR Generator](https://python-qr-generator.streamlit.app/)**

Se o projeto foi útil ou interessante, considere deixar uma ⭐ no repositório!

---

Desenvolvido com Python e Streamlit.
