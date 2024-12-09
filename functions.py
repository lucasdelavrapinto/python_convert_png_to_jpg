import cv2
import os
import streamlit as st

# Diretórios das pastas
pngs_folder = 'temp'
results_folder = 'results'

def convert_png_to_jpg(fileToConvert):
    for filename in os.listdir(pngs_folder):

        if filename == fileToConvert:

            if filename.endswith('.png'):
                # Carrega a imagem .png
                filepath = os.path.join(pngs_folder, filename)
                image = cv2.imread(filepath)

                # Define o caminho de saída com a extensão .jpg
                output_filename = os.path.splitext(filename)[0] + '.jpg'
                output_filepath = os.path.join(results_folder, output_filename)

                # Salva a imagem em .jpg com qualidade máxima (100)
                cv2.imwrite(output_filepath, image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
                
                print(output_filepath)
                print(output_filename)
                print("Conversão concluída!")
                return output_filename
            else:
                st.error("O arquivo não é um arquivo PNG")
        else:
            print("================ no ================")   


def clear_all_files():
    ## Remove todos os arquivos da pasta pngs_folder
    for filename in os.listdir(pngs_folder):
        if filename.endswith('.png'):
            os.remove(os.path.join(pngs_folder, filename))

    ## Remove todos os arquivos da pasta results_folder
    for filename in os.listdir(results_folder):
        if filename.endswith('.jpg'):
            os.remove(os.path.join(results_folder, filename))