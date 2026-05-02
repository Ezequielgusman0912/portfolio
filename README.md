# Portfolio Django - Ezequiel Gusman

Portfolio personal construido con Django y preparado para desplegar en Railway.

## Desarrollo local

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Luego abrir `http://127.0.0.1:8000`.

## Variables para Railway

Configurar estas variables en el servicio:

```text
SECRET_KEY=una-clave-segura
DEBUG=False
ALLOWED_HOSTS=tu-dominio.railway.app
CSRF_TRUSTED_ORIGINS=https://tu-dominio.railway.app
```

Si agregas PostgreSQL en Railway, la variable `DATABASE_URL` se usa automaticamente.
