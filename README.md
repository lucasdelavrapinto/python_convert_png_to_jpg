# Como instalar

```bash
pip install -r requirements.txt
```

# Como executar

```bash
python3 -m streamlit run index.py
```

# Configuração

Caso queira alterar o tamanho permitido do upload do arquivo, basta criar um arquivo `.streamlit/config.toml` e adicionar o seguinte código: Caso Caso

```toml
[server]
maxUploadSize = 30
```
