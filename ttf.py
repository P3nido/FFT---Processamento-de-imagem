import sys
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
try:
    from skimage.io import imread, imshow
    from skimage.color import rgb2hsv, rgb2gray, rgb2yuv
    from skimage import color, exposure, transform
    from skimage.exposure import equalize_hist
except (ImportError, ModuleNotFoundError):
    print("Biblioteca 'scikit-image' não encontrada. Instale as dependências: ")
    print("  pip install scikit-image numpy matplotlib")
    sys.exit(1)

dark_image = imread('img-galo.jpg')

def fourier_masker_ver(image, i):
    # Esta função aplica uma máscara no domínio de Fourier de uma imagem em escala de cinza,
    # exibindo o espectro mascarado, a imagem em tons de cinza e a reconstrução espacial.
    f_size = 15
    dark_image_grey_fourier = np.fft.fftshift(np.fft.fft2(rgb2gray(image)))
    dark_image_grey_fourier[:225, 235:240] = i
    dark_image_grey_fourier[-225:,235:240] = i
    fig, ax = plt.subplots(1,3,figsize=(15,15))
    ax[0].imshow(np.log(abs(dark_image_grey_fourier)), cmap='gray')
    ax[0].set_title('Masked Fourier', fontsize = f_size)
    ax[1].imshow(rgb2gray(image), cmap = 'gray')
    ax[1].set_title('Greyscale Image', fontsize = f_size);
    reconstructed = np.fft.ifft2(np.fft.ifftshift(dark_image_grey_fourier))
    ax[2].imshow(np.abs(reconstructed), cmap='gray')
    ax[2].set_title('Transformed Greyscale Image', fontsize = f_size);
    fig.tight_layout()
    return fig

def fourier_masker_hor(image, i):
    """
    Breve descrição:
    Aplica a transformada de Fourier 2D em uma versão em tons de cinza da imagem, desloca o espectro,
    mascara duas faixas horizontais específicas no domínio de Fourier definindo-as para o valor fornecido,
    e reconstrói a imagem por transformada inversa exibindo os resultados.

    Parâmetros:
    image : ndarray
        Imagem de entrada (espera-se array RGB que será convertido para escala de cinza).
    i : scalar ou complex
        Valor a ser atribuído às faixas mascaradas no domínio de Fourier.

    Retorno:
    matplotlib.figure.Figure
        Figura contendo três subplots: (1) espectro de Fourier mascarado (log da magnitude),
        (2) imagem em tons de cinza original e (3) imagem reconstruída pela transformada inversa.

    """
    f_size = 15
    dark_image_grey_fourier = np.fft.fftshift(np.fft.fft2(rgb2gray(image)))
    dark_image_grey_fourier[235:240, :230] = i
    dark_image_grey_fourier[235:240,-230:] = i
    fig, ax = plt.subplots(1,3,figsize=(15,15))
    ax[0].imshow(np.log(abs(dark_image_grey_fourier)), cmap='gray')
    ax[0].set_title('Masked Fourier', fontsize = f_size)
    ax[1].imshow(rgb2gray(image), cmap = 'gray')
    ax[1].set_title('Greyscale Image', fontsize = f_size);
    reconstructed = np.fft.ifft2(np.fft.ifftshift(dark_image_grey_fourier))
    ax[2].imshow(np.abs(reconstructed), cmap='gray')
    ax[2].set_title('Transformed Greyscale Image', fontsize = f_size);
    fig.tight_layout()
    return fig

# Descrição:
# - fourier_iterator(image, value_list):
#     Itera sobre uma lista de valores e aplica a função fourier_masker_ver para cada valor,
#     produzindo as figuras correspondentes (útil para visualizar variações de máscara).
# - fourier_transform_rgb(image):
#     Para cada canal RGB:
#       * calcula a FFT 2D e desloca o espectro (fftshift),
#       * aplica máscaras verticais fixas no domínio de Fourier,
#       * reconstrói o canal por IFFT,
#     Em seguida empilha os três canais reconstruídos, normaliza os valores para o intervalo
#     [0,255] e retorna a imagem final (uint8) junto com uma figura comparativa (original vs transformada).
def fourier_iterator(image, value_list):
    for i in value_list:
        fourier_masker_ver(image, i)

def fourier_transform_rgb(image):
    f_size = 25
    transformed_channels = []
    for i in range(3):
        rgb_fft = np.fft.fftshift(np.fft.fft2((image[:, :, i])))
        rgb_fft[:225, 235:237] = 1
        rgb_fft[-225:,235:237] = 1
        channel_rec = np.fft.ifft2(np.fft.ifftshift(rgb_fft))
        transformed_channels.append(np.abs(channel_rec))

    stacked = np.stack(transformed_channels, axis=-1).astype(float)
    min_val = stacked.min()
    stacked -= min_val
    max_val = stacked.max()
    if max_val == 0:
        final_image = np.zeros_like(stacked, dtype=np.uint8)
    else:
        final_image = (stacked / max_val * 255).astype(np.uint8)

    fig, ax = plt.subplots(1, 2, figsize=(17,12))
    ax[0].imshow(image)
    ax[0].set_title('Original Image', fontsize = f_size)
    ax[0].set_axis_off()

    ax[1].imshow(final_image)
    ax[1].set_title('Transformed Image', fontsize = f_size)
    ax[1].set_axis_off()

    fig.tight_layout()
    return final_image, fig

# Executa a transformacao RGB e salva/exibe o resultado
if __name__ == '__main__':
    # fechar figuras antigas e criar apenas as duas desejadas
    plt.close('all')

    # figura de comparativo de construção (vertical mask) — equivalente à figura desejada
    fig_construction = fourier_masker_ver(dark_image, 1)

    # figura de comparativo final das imagens coloridas
    processed, fig_final = fourier_transform_rgb(dark_image)

    # salvar ambas as figuras
    fig_construction.savefig('construction_comparison.png', bbox_inches='tight')
    fig_final.savefig('final_color_comparison.png', bbox_inches='tight')

    # não exibir janelas — apenas salvar os arquivos (backend 'Agg')

    print("Processamento concluído. A imagem pós-processada foi retornada na variável 'processed' e as figuras foram salvas:")
    print("  - construction_comparison.png (comparativo de construção)")
    print("  - final_color_comparison.png (comparativo final colorido)")