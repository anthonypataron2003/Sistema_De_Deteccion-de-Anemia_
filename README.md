# 🩸 Sistema de Detección de Anemia

<p align="center">
  <strong>Aplicación web para el análisis de imágenes y apoyo en la detección de anemia mediante Inteligencia Artificial.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%20%7C%203.11-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Django-Framework-green?logo=django" alt="Django">
  <img src="https://img.shields.io/badge/TensorFlow-Machine%20Learning-orange?logo=tensorflow" alt="TensorFlow">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Status-Development-yellow" alt="Status">
</p>

---

## 📌 Descripción

**Sistema de Detección de Anemia** es una aplicación web desarrollada con **Django** que permite gestionar pacientes, registrar imágenes y generar análisis mediante modelos de **aprendizaje automático desarrollados con TensorFlow**.

El sistema está orientado a servir como una herramienta de **apoyo para personal autorizado**, facilitando el registro de información, consulta de antecedentes y generación de resultados a partir de imágenes.

> ⚠️ **Importante:** Esta aplicación es únicamente una herramienta de apoyo tecnológico. Los resultados generados no sustituyen la valoración, diagnóstico ni criterio de un profesional de la salud.

---

## 🚀 Funcionalidades principales

### 👤 Gestión de usuarios

* 🔐 Registro e inicio de sesión.
* 👥 Gestión de usuarios y perfiles.
* 🛡️ Control de acceso a las funcionalidades del sistema.
* ⚙️ Administración mediante Django Admin.

### 🧑‍⚕️ Gestión de pacientes

* 📝 Registro y administración de pacientes.
* 🖼️ Carga y almacenamiento de imágenes.
* 📂 Consulta del historial de información.
* 🔎 Acceso a los análisis realizados.

### 🤖 Inteligencia Artificial

* 🧠 Análisis de imágenes mediante modelos de **TensorFlow**.
* 📊 Generación de resultados basados en los modelos entrenados.
* 🔬 Integración de modelos de Machine Learning dentro de Django.
* 📁 Modelos almacenados en el directorio `ml_models/`.

### 📑 Historial y reportes

* 📋 Registro histórico de análisis.
* 📈 Consulta de resultados.
* 📄 Generación y visualización de reportes.
* 🕐 Seguimiento de análisis realizados a los pacientes.

---

## 🛠️ Tecnologías utilizadas

| Tecnología                     | Uso                        |
| ------------------------------ | -------------------------- |
| 🐍 **Python**                  | Lenguaje principal         |
| 🌐 **Django**                  | Framework web              |
| 🧠 **TensorFlow**              | Machine Learning           |
| 🐘 **PostgreSQL**              | Base de datos              |
| 🗄️ **SQLite**                 | Base de datos para pruebas |
| 🎨 **HTML / CSS / JavaScript** | Interfaz web               |
| 🔐 **Django Authentication**   | Autenticación y seguridad  |

---

## 📋 Requisitos

Antes de ejecutar el proyecto necesitas tener instalado:

* 🐍 **Python 3.10 o 3.11**
* 💻 **PowerShell** en Windows o una terminal equivalente.
* 📦 Dependencias incluidas en `requirements.txt`.
* 🐘 **PostgreSQL** para un entorno persistente.
* 🗄️ **SQLite** para pruebas locales.

> 💡 Los modelos entrenados se encuentran dentro de `ml_models/`. La instalación de TensorFlow puede requerir varios cientos de MB de almacenamiento y suficiente memoria RAM.

---

# ⚡ Instalación y ejecución

## 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/anthonypataron2003/Sistema_De_Deteccion-de-Anemia_.git
```

Ingresar al proyecto:

```bash
cd Sistema_De_Deteccion-de-Anemia_
```

---

## 2️⃣ Crear el entorno virtual

En **PowerShell**:

```powershell
python -m venv .venv
```

Activar el entorno:

```powershell
.\.venv\Scripts\Activate
```

Si se activó correctamente, aparecerá `(.venv)` al inicio de la terminal.

---

## 3️⃣ Actualizar herramientas

```powershell
python -m pip install --upgrade pip wheel
```

---

## 4️⃣ Instalar dependencias

```powershell
pip install -r requirements.txt
```

---

## 5️⃣ Configurar variables de entorno

Crea un archivo llamado:

```text
.env
```

en la raíz del proyecto.

Para una prueba local utilizando SQLite:

```env
SECRET_KEY=crea-una-clave-segura
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

> 🔒 **Importante:** Nunca publiques el archivo `.env` ni credenciales reales en GitHub.

El proyecto ya contempla excluir archivos sensibles como:

```text
.env
.venv/
```

mediante `.gitignore`.

---

## 6️⃣ Ejecutar migraciones

```powershell
python manage.py migrate
```

---

## 7️⃣ Crear usuario administrador

```powershell
python manage.py createsuperuser
```

Completa los datos solicitados en la terminal.

---

## 8️⃣ Ejecutar el servidor

```powershell
python manage.py runserver
```

Si todo está correcto, Django mostrará:

```text
Starting development server at http://127.0.0.1:8000/
```

🌐 Abre en tu navegador:

**http://127.0.0.1:8000/**

### 🔐 Panel de administración

Puedes acceder al administrador de Django desde:

**http://127.0.0.1:8000/admin/**

---

# 📁 Estructura del proyecto

```text
Sistema_De_Deteccion-de-Anemia_/
│
├── 📂 anemia_project/
│   ├── ⚙️ settings.py
│   ├── 🌐 urls.py
│   ├── 🚀 asgi.py
│   └── 🚀 wsgi.py
│
├── 📂 apps/
│   ├── 📂 core/
│   │   ├── 👤 Pacientes
│   │   ├── 🤖 Análisis
│   │   ├── 📊 Reportes
│   │   └── 📈 Dashboard
│   │
│   └── 📂 security/
│       ├── 🔐 Autenticación
│       └── 👥 Perfiles
│
├── 📂 ml_models/
│   ├── 🧠 Modelos entrenados
│   └── 🔬 Detector
│
├── 📂 static/
│   ├── 🎨 CSS
│   ├── ⚡ JavaScript
│   └── 🖼️ Imágenes
│
├── 📂 templates/
│   └── 🌐 Plantillas HTML
│
├── 📄 manage.py
├── 📄 requirements.txt
├── 📄 INSTALLATION.md
├── 📄 USER_GUIDE.md
└── 📄 .gitignore
```

---

# 📚 Documentación

📘 **Guía de instalación**

Consulta la documentación completa sobre configuración, modelos, variables de entorno y solución de problemas:

👉 [INSTALLATION.md](https://github.com/anthonypataron2003/Sistema_De_Deteccion-de-Anemia_/blob/main/INSTALLATION.md)

📗 **Guía de usuario**

Consulta el flujo de trabajo del sistema y ejemplos de análisis:

👉 [USER_GUIDE.md](https://github.com/anthonypataron2003/Sistema_De_Deteccion-de-Anemia_/blob/main/USER_GUIDE.md)

---

# 🔐 Seguridad y privacidad

Las imágenes y datos de pacientes pueden contener **información sensible**. Por este motivo:

* 🔒 Utiliza los datos únicamente con la autorización correspondiente.
* 👥 Implementa controles de acceso adecuados.
* 🔑 Protege las credenciales y variables de entorno.
* 🚫 No publiques información personal en el repositorio.
* ⚙️ En producción utiliza `DEBUG=False`.
* 🌐 Configura correctamente `ALLOWED_HOSTS`.
* 🔐 Protege la `SECRET_KEY`.
* 🗄️ Utiliza una base de datos segura.

---

# ⚕️ Uso responsable

Los resultados generados por los modelos de aprendizaje automático son **orientativos** y deben ser revisados e interpretados por personal cualificado.

El sistema no pretende reemplazar los procedimientos médicos, diagnósticos clínicos ni la valoración de profesionales de la salud.

---

# 👨‍💻 Autor

**Anthony Steven Pataron Naula**

🎓 Estudiante de Ingeniería de Software
🏫 Universidad Estatal de Milagro — UNEMI

---

<p align="center">
  🩸 <strong>Sistema de Detección de Anemia</strong>  
  <br>
  🤖 Inteligencia Artificial + 🌐 Desarrollo Web + 🧠 Machine Learning
</p>
