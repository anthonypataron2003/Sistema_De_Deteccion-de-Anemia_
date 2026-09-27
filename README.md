# Sistema de Deteccion de Anemia

Aplicacion web desarrollada con Django para gestionar pacientes, registrar
imagenes y generar analisis asistidos por un modelo de aprendizaje automatico.
Esta herramienta esta orientada al apoyo del personal autorizado y no sustituye
la valoracion de un profesional de la salud.

## Funcionalidades

- Registro e inicio de sesion de usuarios.
- Gestion de pacientes y sus imagenes.
- Analisis de imagenes mediante modelos de TensorFlow incluidos en el proyecto.
- Historial de resultados y reportes.
- Panel de administracion de Django para gestionar usuarios y datos.

## Requisitos

- Python 3.10 o 3.11.
- PowerShell en Windows, o una terminal equivalente.
- Dependencias de `requirements.txt`.
- PostgreSQL para un entorno persistente, o SQLite para pruebas locales.

Los modelos entrenados se encuentran en `ml_models/`. La instalacion de
TensorFlow puede requerir varios cientos de MB y suficiente memoria disponible.

## Inicio rapido

Desde la raiz del proyecto, ejecuta en PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
python -m pip install --upgrade pip wheel
pip install -r requirements.txt
```

Crea un archivo `.env` en la raiz con una `SECRET_KEY`, `DEBUG`,
`ALLOWED_HOSTS` y la configuracion de base de datos. Para una prueba local
puedes usar SQLite:

```dotenv
SECRET_KEY=crea-una-clave-segura
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

No publiques `.env` ni credenciales reales. El repositorio ya excluye `.env`
y `.venv/` mediante `.gitignore`.

Aplica las migraciones y arranca el servidor:

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abre <http://127.0.0.1:8000/> en el navegador. El panel de administracion
esta disponible en <http://127.0.0.1:8000/admin/>.

## Estructura principal

```text
anemia_project/       Configuracion, ASGI, WSGI y rutas del proyecto
apps/core/            Pacientes, analisis, reportes y dashboard
apps/security/        Autenticacion y perfiles
ml_models/            Detector y modelos entrenados
static/                CSS, JavaScript e imagenes estaticas
templates/             Plantillas HTML de Django
```

## Documentacion

- [Guia de instalacion](INSTALLATION.md): configuracion detallada, modelos,
  variables de entorno y resolucion de problemas.
- [Guia de uso](USER_GUIDE.md): flujo de trabajo para usuarios y ejemplos de
  analisis.

## Seguridad y privacidad

Las imagenes de pacientes pueden contener informacion sensible. Usa datos con
el consentimiento correspondiente y aplica controles de acceso adecuados.
Antes de desplegar en produccion, configura `DEBUG=False`, define
`ALLOWED_HOSTS`, protege `SECRET_KEY` y utiliza una base de datos segura.

Los resultados son orientativos y deben ser revisados por personal cualificado.