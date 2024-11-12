import cv2
import os

# Diretórios das pastas
pngs_folder = 'pngs_folder'
results_folder = 'results'

# Cria a pasta de resultados se ela não existir
os.makedirs(results_folder, exist_ok=True)

# Itera por todos os arquivos na pasta pngs_folder
for filename in os.listdir(pngs_folder):
    if filename.endswith('.png'):
        # Carrega a imagem .png
        filepath = os.path.join(pngs_folder, filename)
        image = cv2.imread(filepath)

        # Define o caminho de saída com a extensão .jpg
        output_filename = os.path.splitext(filename)[0] + '.jpg'
        output_filepath = os.path.join(results_folder, output_filename)

        # Salva a imagem em .jpg com qualidade máxima (100)
        cv2.imwrite(output_filepath, image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

print("Conversão concluída!")
