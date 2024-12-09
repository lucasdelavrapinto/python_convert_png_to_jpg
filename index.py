import streamlit as st
import os
import time 
from functions import convert_png_to_jpg, clear_all_files

# clear_all_files()

current_dir = os.path.dirname(os.path.abspath(__file__))
temp_dir = os.path.join(current_dir, 'temp')

uploaded_file = st.file_uploader("Carregue um arquivo PNG", type=["png"])

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()

    if not os.path.exists('temp'):
        os.makedirs('temp')

    # Salvar o arquivo
    file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(file_path, "wb") as binary_file:
        binary_file.write(bytes_data)

    st.image('temp/' + uploaded_file.name)

    if st.button("Converter para JPG", type="primary"):        

        with st.spinner('Wait for it...'):
            
            temp_dir = os.path.join(current_dir, 'results')
            file_name = convert_png_to_jpg(uploaded_file.name)
            file_path = os.path.join(temp_dir, file_name)

            time.sleep(5)
            
            st.success("Conversão concluída com sucesso!")

            #funcionalidade para baixar o arquivo da pasta results
            with open(file_path, 'rb') as f:
                st.download_button('Download file', f, file_name=file_name, mime="image/jpg")  # Defaults to 'text/plain'