# Guía de instalación - Proyecto Anemia Detection

Este documento describe paso a paso cómo instalar y poner en marcha el proyecto en un entorno local (Windows PowerShell). Incluye creación de entorno virtual, instalación de dependencias, variables de entorno, migraciones, configuración de modelos ML y comprobaciones rápidas.

## Requisitos previos

- Python 3.10 o 3.11 (recomendado).
- Git (opcional, para clonar el repo).
- PostgreSQL si quieres usar la configuración por defecto; opcionalmente puedes usar SQLite para pruebas rápidas.
- En Windows, PowerShell (esta guía usa PowerShell).
- Espacio en disco suficiente para dependencias (TensorFlow puede ocupar varios cientos de MBs).

## Archivos y rutas importantes en el proyecto

- `manage.py` — punto de entrada de Django.
- `requirements.txt` — lista de dependencias (Django 5.2.7, TensorFlow 2.20, etc.).
- `anemia_project/settings.py` — configuración del proyecto (usa `python-decouple` para variables de entorno).
- `ml_models/` — contiene `best_model.h5`, `model_anemia.h5`, y utilidades (`anemia_detector.py`, `model_loader.py`).
- `static/` y `media/` — recursos estáticos y uploads de usuarios.

## 1) Clonar el repositorio (si corresponde)

En PowerShell:

```powershell
# Opcional: clonar
git clone <repo-url> .
# O si ya tienes la carpeta, navega a ella
Set-Location -Path c:\Users\User\Desktop\anemIA
```

## 2) Crear y activar un entorno virtual (venv)

En PowerShell:

```powershell
# Crear entorno virtual en la carpeta .venv (recomendado)
python -m venv .venv

# Activar el entorno
.\.venv\Scripts\Activate

# Verifica que estás en el entorno (prompt cambiará)
python -V
```

> Nota: si usas Conda, crea un entorno con la versión de Python adecuada.

## 3) Actualizar pip y wheel, e instalar dependencias

```powershell
python -m pip install --upgrade pip wheel
pip install -r requirements.txt
```

El fichero `requirements.txt` incluye paquetes pesados como `tensorflow==2.20.0`. Si tienes problemas con la instalación de TensorFlow en Windows, considera instalar una versión compatible con tu versión de Python y con o sin soporte GPU según tu hardware.

## 4) Variables de entorno y fichero .env

El proyecto usa `python-decouple`. Puedes crear un fichero `.env` en la raíz del proyecto con variables como:

```
# .env (ejemplo)
SECRET_KEY=tu_secret_key_segura_aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (por defecto se espera PostgreSQL)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=anemia_db
DB_USER=postgres
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=5432

# Email (opcional)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_USE_TLS=True
```

Para pruebas rápidas con SQLite (sin instalar PostgreSQL), añade al `.env`:

```
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

> Importante: en producción no dejes `DEBUG=True` y guarda `SECRET_KEY` seguro.

## 5) Crear carpetas necesarias para archivos estáticos y media

```powershell
# Crear carpeta media si no existe
New-Item -ItemType Directory -Path .\media -Force
# (opcional) crear carpeta staticfiles para collectstatic
New-Item -ItemType Directory -Path .\staticfiles -Force
```

`settings.py` ya define:
- `STATICFILES_DIRS = [ BASE_DIR / "static" ]`
- `STATIC_ROOT = BASE_DIR / "staticfiles"`
- `MEDIA_ROOT = BASE_DIR / "media"`

## 6) Migraciones y superusuario

```powershell
# Aplicar migraciones
python manage.py migrate

# Crear superusuario (sigue las indicaciones)
python manage.py createsuperuser
```

## 7) Archivos estáticos

Para recopilar archivos estáticos (útil en despliegue):

```powershell
python manage.py collectstatic --noinput
```

En desarrollo normalmente no es necesario ejecutar `collectstatic` si `DEBUG=True`.

## 8) Modelos de ML

- Los modelos esperados están en `ml_models/`, por ejemplo `ml_models/best_model.h5`.
- `ml_models/anemia_detector.py` usa por defecto la ruta `ml_models/best_model.h5`.
- `ml_models/model_loader.py` contiene un singleton que carga el detector una sola vez.

Asegúrate de que los archivos `.h5` estén en `ml_models/`. Si los mueves, actualiza la ruta al crear `AnemiaDetector(...)` o modifica el atributo `model_path`.

## 9) Prueba rápida de carga del modelo (comprobar que el modelo existe y carga)

En PowerShell (con el entorno virtual activado):

```powershell
python -c 'from ml_models.anemia_detector import AnemiaDetector; d=AnemiaDetector("ml_models/best_model.h5"); d.load_model(); print(d.get_model_info())'
```

Si el archivo no existe, verás `FileNotFoundError` con la ruta esperada. Corrige ubicaciones o coloca el `.h5` en `ml_models/`.

## 10) Ejecutar el servidor de desarrollo

```powershell
python manage.py runserver 0.0.0.0:8000
```

Abre en el navegador: http://127.0.0.1:8000/

## 11) Comprobación desde Django shell (ejemplo de predicción)

Abre la shell de Django:

```powershell
python manage.py shell
```

Dentro de la shell Python:

```python
from ml_models.anemia_detector import AnemiaDetector
det = AnemiaDetector('ml_models/best_model.h5')
det.load_model()
print(det.get_model_info())
# Para predecir sobre una imagen local:
# print(det.predict('static/img/analysis/Pac-1001/some_image.jpg'))
```

## 12) Notas y resolución de problemas comunes

- Error al instalar TensorFlow en Windows: revisa la versión de Python (3.10/3.11 recomendadas) y usa las ruedas oficiales o entornos Conda si hay conflictos.
- Si la carga del modelo falla por memoria, prueba en un equipo con más RAM o desactiva GPU si la instalación de TensorFlow se hizo con soporte GPU.
- Problemas con la base de datos PostgreSQL: asegúrate de que el servicio esté en ejecución y que las credenciales del `.env` sean correctas.
- Permisos de carpeta `media/` y `staticfiles/`: asegúrate de que el usuario que ejecuta el servidor tenga permisos de escritura.

## 13) Deploy básico (pistas)

- Para producción, configura `DEBUG=False`, establece `ALLOWED_HOSTS`, usa un servidor WSGI (Gunicorn + Nginx) o ASGI (Uvicorn + Nginx) según preferencia.
- Usa una base de datos gestionada (Postgres) y guarda `SECRET_KEY` y credenciales en variables de entorno seguras.
- Considera Dockerizar la app (Dockerfile + docker-compose) como siguiente mejora.

## 14) Comandos útiles resumen (PowerShell)

```powershell
# Activar entorno
.\.venv\Scripts\Activate

# Instalar dependencias
pip install -r requirements.txt

# Variables de entorno (temporal en la sesión)
$env:DJANGO_SETTINGS_MODULE='anemia_project.settings'
# (o usar .env)

# Migrar
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
```

## 15) Próximos pasos recomendados

- Añadir un `README.md` con visión general y screenshots.
- Crear un `docker-compose.yml` para reproducibilidad en otros entornos.
- Añadir pruebas automáticas (unit + integration) que validen carga de modelos y endpoints claves.

---

Si quieres, puedo:
- Ajustar el `.env.example` y añadirlo al repo.
- Crear un `run_test_model.py` pequeño para probar la carga/predicción automáticamente.
- Generar un `docker-compose.yml` básico para levantar la app y Postgres localmente.

Fin del documento de instalación.
