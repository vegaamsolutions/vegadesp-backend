## ⚙️ Configuração do Ambiente (Desenvolvimento)

1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/vegadesp-backend.git
cd vegadesp-backend
```

2. Criar e ativar o ambiente virtual

```bash
python -m venv venv
```

- Para ativar o ambiente virtual se for windows `venv\Scripts\activate` se Linux `source venv/bin/activate`.

3. Instalar dependências

```bash
pip install django djangorestframework
```

4. Rodar migrations iniciais

```bash
cd src
python manage.py migrate
```

5. Subir o servidor

```bash
python manage.py runserver
```

6. Verificar funcionamento da API

- Endpoint de health check: `GET /api/v1/health/` que possui a seguinte resposta:

```json
{
  "status": "ok",
  "service": "vegadesp-backend"
}

```