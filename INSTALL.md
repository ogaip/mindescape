
# Mindescape - INSTALL.md

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.9+** (La versión mínima requerida de Python debe estar en el archivo README o en las dependencias del proyecto).
- **Git** (si deseas clonar el proyecto en lugar de descargar el archivo `.zip`).
- **Pip** (debería estar incluido en la instalación de Python).

### 1. Instalación de Python

Si aún no tienes Python instalado, sigue estos pasos:

#### En Windows:
1. Ve a [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. Descarga la última versión de Python 3.x.
3. Durante la instalación, asegúrate de marcar la opción **"Add Python to PATH"**.
4. Completa la instalación.

#### En MacOS y Linux:
1. En MacOS, puedes instalar Python 3 usando Homebrew:
   ```bash
   brew install python
   ```
2. En Linux, dependiendo de tu distribución:
   - Ubuntu/Debian:
     ```bash
     sudo apt update
     sudo apt install python3
     ```
   - Fedora:
     ```bash
     sudo dnf install python3
     ```

### 2. Instalación de Git (opcional)

Si prefieres clonar el repositorio usando Git, necesitarás tener Git instalado. Si ya lo tienes instalado, puedes saltar este paso.

#### En Windows:
1. Ve a [https://git-scm.com/download/win](https://git-scm.com/download/win) y descarga el instalador.
2. Ejecuta el instalador y sigue las instrucciones en pantalla. Puedes dejar la configuración predeterminada.

#### En MacOS:
1. Abre la terminal y ejecuta el siguiente comando:
   ```bash
   brew install git
   ```

#### En Linux:
1. En distribuciones basadas en Debian/Ubuntu:
   ```bash
   sudo apt update
   sudo apt install git
   ```
2. En distribuciones basadas en Fedora:
   ```bash
   sudo dnf install git
   ```

Para verificar que Git se instaló correctamente, ejecuta el siguiente comando en tu terminal o consola de comandos:

```bash
git --version
```

Esto debería mostrar la versión de Git que tienes instalada.

### 3. Descarga del Proyecto

Tienes dos opciones para descargar el proyecto:

#### Opción 1: Clonar el Repositorio con Git

Si prefieres trabajar con Git, puedes clonar el repositorio:

1. Abre tu terminal o consola de comandos.
2. Clona el proyecto con el siguiente comando:
   ```bash
   git clone https://github.com/ogaip/mindescape.git
   ```
3. Entra en el directorio del proyecto:
   ```bash
   cd mindescape
   ```

#### Opción 2: Descargar el Proyecto como `.zip`

Si no tienes Git instalado o prefieres descargar el archivo `.zip`:

1. Ve al siguiente enlace: [https://github.com/ogaip/mindescape](https://github.com/ogaip/mindescape).
2. Haz clic en el botón **Code** y selecciona **Download ZIP**.
3. Descomprime el archivo descargado en una carpeta de tu elección.
4. Abre tu terminal y navega al directorio del proyecto:
   ```bash
   cd ruta/donde/descomprimiste/el/proyecto
   ```

### 4. Crear y Activar un Entorno Virtual

Es recomendable crear un entorno virtual para evitar conflictos con otras instalaciones de Python:

1. Crea el entorno virtual:
   ```bash
   python -m venv venv
   ```
2. Activa el entorno virtual:

   - **En Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **En MacOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

   Verás que tu prompt cambia para reflejar que el entorno virtual está activado.

### 5. Instalar las Dependencias del Proyecto

#### Opción 1: Usar `requirements.txt`

Si el archivo `requirements.txt` está disponible, puedes instalar todas las dependencias con un solo comando:

1. Asegúrate de estar en el directorio del proyecto y que tu entorno virtual esté activado.
2. Ejecuta el siguiente comando:
   ```bash
   pip install -r requirements.txt
   ```

#### Opción 2: Instalar las Dependencias Manualmente

Si el archivo `requirements.txt` no está disponible, instala manualmente las dependencias listadas en el README o en la documentación del proyecto. Ejemplo:

```bash
pip install django
pip install djangorestframework
# Agrega más dependencias según sea necesario
```

### 6. Realizar las Migraciones de la Base de Datos

Una vez que las dependencias estén instaladas, es necesario aplicar las migraciones de base de datos:

1. Ejecuta el siguiente comando para realizar las migraciones:
   ```bash
   python manage.py migrate
   ```

### 7. Ejecutar el Servidor de Desarrollo

Una vez finalizadas las migraciones, puedes ejecutar el servidor de desarrollo de Django con el siguiente comando:

```bash
python manage.py runserver
```

Accede a la aplicación web desde tu navegador en [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

### Resolución de Problemas

- **Problemas con dependencias:** Asegúrate de que el archivo `requirements.txt` esté actualizado con las versiones correctas de las dependencias. Si no está presente, sigue las instrucciones manuales.
- **Errores en migraciones:** Si encuentras algún error relacionado con migraciones, asegúrate de que la base de datos esté correctamente configurada en el archivo `settings.py`.

---

Con esto, deberías tener el proyecto funcionando correctamente en tu entorno local. Para más detalles sobre la estructura del proyecto y cómo contribuir, consulta el archivo `README.md` en el repositorio.
