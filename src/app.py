import streamlit as st
from io import BytesIO
from generator import gerar_qrcode



st.set_page_config(
    page_title="QR Code Generator",
    page_icon="🔳",
    layout="centered"
)

st.markdown(
    """
    <h1 style='text-align: center;'>Gerador de QR Code com Python</h1>
    <h3 style='text-align: center;'>Crie e personalize seu QR Code gratis!</h3>
    """,
    unsafe_allow_html=True
)
with st.container(border=True):
    conteudo = st.text_input(
        "Digite um link:",
        placeholder="https://github.com"
    )

    col1, col2 = st.columns(2)
    with col1:
        cor_qr = st.color_picker(
        "Cor do QR Code",
        "#000000"
        )
    with col2:
        cor_fundo = st.color_picker(
        "Escolha a cor do fundo:",
        "#FFFFFF"
        )
    tamanho = st.slider(
        "Tamanho do QR Code",
        min_value=5,
        max_value=20,
        value=10
        )

    if st.button("Gerar QR Code"):
        if conteudo.strip():
            imagem = gerar_qrcode(conteudo, cor_qr, cor_fundo)
            buffer = BytesIO()
            imagem.save(buffer, format="PNG")
            dados = buffer.getvalue()
            col1, col2, col3 = st.columns([1, 2, 1])

            with col2:
                st.image(
                imagem,
                width=300,
                use_container_width=True
                )
                st.download_button(
                label="Baixar QR Code",
                data=dados,
                file_name="qrcode.png",
                mime="image/png",
                use_container_width=True
             )
        else:
            st.error("Por favor, digite um link antes de gerar.")