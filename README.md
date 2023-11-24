PlaygroundFinalProject-Forlano
Este es un proyecto Django llamado Forla_SA.
Dentro del proyecto principal agregamos en settings las configuraciones pertinentes sobre apps, templates, staticfiles. En los urls, con la funcion include hicimos que los todas las rutas salvo admin las maneje el urls.py de la app.
Luego creamos una app llamada forla_app. Aqui creamos:
Views que le dicen a nuestros templates como actuar. 
Paths en urls para conectar views con templates.
Templates que van a mostrarle al usuario lo que ve en la web.
Descargamos archivos estaticos de Bootstrap para darle formato a nuestro template padre y heredarlo a los hijos. (CSS, Imagenes, JS)
Es decir, el formato del template sera el mismo ya que se hereda del padre (inicio.html) para todos los otros templates. El contenido del cuerpo varia en cada uno.
Creamos modelos para darle estructura a nuestra base de datos en models.
Creamos formularios en forms para poder usarlos en nuestras views y que los users los pueden completar en la web.
Con estos formularios se dan los ingresos de objetos a nuestros distintos modelos (clientes, pedidos y productos). Esto se hace mediante metodo POST.
Estos ingresos quedaran guardados y podran ser modificados, administrados, borrados y llamados en nuestra base de datos.
La misma informacion se puede acceder con el DB Browser o tambien vamos a poder ver nuestros modelos y ojbetos en admin.
Para verlo en admin tenemos que crear un superuser y tambien tenemos que registrar nuestros modelos en admin.py.
Tambien creamos un buscador de precios que con uso del metodo GET, el usuario ingresa el nombre de un producto y se le muestra el precio del mismo.

Cambios adicionales:
Agregamos la funcionalidad de subir imagenes. 
Ahora las imagenes de los productos se ven mediante el listado.
Se piden permisos de administrador agregar, modificar y eliminar productos.
Se crea log in, register y log out.
Se crean distintos redirects para que una vez que se realice un proceso se lleve al usuario a una pagina apropiada.
