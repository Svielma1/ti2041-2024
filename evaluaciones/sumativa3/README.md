# Requisitos
- Python 3.10 o superior.
- Django 5.1
- Navegador web (Chrome, Firefox, Brave, Etc...).
- Git.

# Instrucciones
- Clona el repositorio desde Github (git clone https://github.com/Svielma1/ti2041-2024.git).
- Dirigete a la carpeta del proyecto (cd evaluaciones\sumativa3)
- Levanta la aplicacion (manage.py runserver)
- Una vez la aplicacion esta levantada, dirigete en tu navegador a la ruta de la app, http://127.0.0.1:8000
- Para bajar la aplicacion basta con irse a la terminal y presionar la combinacion de teclas " Ctrl + C"

# Medidas de seguridad
- CSRF: Con este metodo Django se asegura que los datos vengan estrictamente del formualio y no de un tercero que haya intervenido.
  
  Ejemplo de uso:
  ```html
  <form method="post">
      {% csrf_token %}
      <label for="usuario">Usuario: </label><br>
          <input name="usuario" id="usuario" required/>
      <label for="contrasena">Contraseña: </label><br>
          <input type="password" name="contrasena" id="contrasena"/>
      <button type="submit">Iniciar sesion</button>
  </form>

- XSS: Este metodo evita la injeccion de script malisioso de parte de un tercero.
  
  Ejemplo de uso:
  ```html
    <td>{{ product.code }}</td>

- Errores sensibles: evita mostrar informacion en la consola, amenos que se este ejecutando en 'localhost'.
  
  Ejemplo de uso:
  ```python
    #Archivo settings.py
    DEBUG = False
    ALLOWED_HOSTS = ['localhost']
