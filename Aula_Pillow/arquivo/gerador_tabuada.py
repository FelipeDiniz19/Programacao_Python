from PIL import Image, ImageDraw, ImageFont
import os

def cria_imagem_tabuada():
    largura = 600
    altura = 600
    cor_fundo =(245,235,220) 

    imagem = Image.new('RGB',(largura, altura), color=cor_fundo)

    desenho = ImageDraw.Draw(imagem)

    pasta_saida = "saida_imagem"
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

        caminho_ficaheiro = os.path.join(pasta_saida),"tabuada_base.png"
        imagem.save(caminho_ficaheiro)
        print(f"Imagem guardada com sucesso em: {caminho_ficaheiro}")

    if __name__ == "__main__":
        cria_imagem_tabuada()   