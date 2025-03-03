# Crud loja django

### Passo a passo para rodar o projeto

1. Crie um ambiente virtual com o seguinte comando:
```bash
python -m venv env_project
```

2. Entre no ambiente virtual:

no linux:
```bash
source env_project/bin/activate
```

no windows:
```bash
env_project\Scripts\activate.bat
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Aplique as migrações:
```bash
python manage.py migrate
```

5. Rode o sistema:
```bash
python manage.py runserver
```
