import qrcode
from io import BytesIO
from PIL import Image

def gerar_qrcode(conteudo, cor_qr, cor_fundo):
    qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
    )
    qr.add_data(conteudo)
    qr.make(fit=True)
    imagem = qr.make_image(
    fill_color=cor_qr,
    back_color=cor_fundo
    ).get_image()
    return imagem

