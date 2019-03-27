# Calculadora Django

Realiza una calculadora con Django. Esta calculadora responderá a URLs de la forma /suma/num1/num2, /multi/num1/num2, /resta/num1/num2, /div/num1/num2, realizando las operaciones correspondientes, y devolviendo error "Not Found" para las demás.

Parte del repositorio en GitLab: https://gitlab.etsit.urjc.es/cursosweb/x-serv-15.4-django-calc.

El proyecto Django se llamará project y la aplicación calc.
Recuerda que para realizar la aplicación básica sólo tendrás que modificar los siguientes ficheros: settings.py, urls.py y views.py.

Si quieres añadir persistencia, puedes aprovechar y tener peticiones /suma/num1 y luego /suma/num2. Para ello, además, debes tocar models.py (y si quieres ver el contenido de la base de datos vía web, admin.py).
