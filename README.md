# Blog Sofia Mosquera

Este proyecto es la **entrega final del Playground** desarrollado con **Python** y **Django**.

Creado por: **Sofia Mosquera** (GitHub: [ssephtis](https://github.com/ssephtis))  
Repositorio: [Blog-Sofia-Mosquera](https://github.com/ssephtis/Blog-Sofia-Mosquera)

---

## 🌐 Descripción
Una aplicación web estilo blog donde los usuarios pueden registrarse, iniciar sesión, publicar entradas, editar su perfil y navegar contenido. Incluye sistema de autenticación, subida de imágenes, CKEditor para contenido enriquecido y mensajes entre usuarios.

---

##  Funcionalidades principales

- Página de Inicio y "Acerca de mí"
- Sistema de login, logout y registro de usuarios
- Vista de perfil y edición del mismo
- CRUD de entradas de blog (crear, ver, editar, eliminar)
- Subida de imágenes con `MEDIA`
- Contenido enriquecido con `django-ckeditor`
- Herencia de templates (`base.html` con NavBar funcional)
- Seguridad con mixins y control de permisos

---

##  Estructura básica

```bash
Blog-Sofia-Mosquera/
├── accounts/
├── pages/
├── media/
├── static/
├── templates/
├── manage.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

##  Instalación y uso

1. Cloná el repositorio:

```bash
git clone https://github.com/ssephtis/Blog-Sofia-Mosquera.git
cd Blog-Sofia-Mosquera
```

2. Activá el entorno virtual y cargá dependencias:

```bash
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -r requirements.txt
```

3. Corré las migraciones y lanzá el servidor:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

4. Accedé desde:

- http://127.0.0.1:8000/ → Página principal
- http://127.0.0.1:8000/about/ → Acerca de mí
- http://127.0.0.1:8000/accounts/login/ → Login
- http://127.0.0.1:8000/accounts/signup/ → Registro

---

## 🛑 Importante

### `.gitignore` incluye:

```
__pycache__/
db.sqlite3
media/
venv/
```

Esto evita subir la base de datos y archivos pesados innecesarios.

---

##  Requisitos técnicos cumplidos

✅ Modelo principal con campos CharField, texto enriquecido, imagen, fecha  
✅ Sistema de usuarios con perfiles, edición y avatar  
✅ Login, logout y registro funcionando correctamente  
✅ CRUD completo de páginas con permisos  
✅ Vista de detalle, listado y manejo de "no hay páginas"  
✅ CKEditor y archivos multimedia  
✅ Uso de Class Based Views, mixins y decoradores  
✅ Templates reutilizables y herencia de `base.html`

---

## 🎥 Video de presentación

Podés ver el video demostrativo del blog acá:  
 [Ver video en Google Drive](https://drive.google.com/file/d/1rhXAiLFqIbksMCubDCq-rGBpNcuM6w4L/view?usp=sharing)

##  Autoría
**Sofia Mosquera**  
Estudiante 
Proyecto para entrega final del Playground.