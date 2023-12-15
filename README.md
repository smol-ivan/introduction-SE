# Manual 

## Consideraciones

Para la implementacion de la interfaz, se tuvieron las siguientes consideraciones, con el fin de no extenderse mas de lo necesario

- Existe la clase cliente, que solo tiene atributos el nombre y una matricula que es asignada por el sistema

- Para las verificacion de cliente, se espera que el input sea en el formato requerido(Numeros)

- Se considera que hay un administrador o encargado que es capaz de eliminar y agregar clientes, de estos casos, el unico implementado fue el de agregar

- Al entrar con exito al sistema de citas solo se da un mensaje de Bienvenida y el programa finaliza

- El programa no cuenta con la implementacion para la serializacion de los objetos por lo que los clientes creados durante la ejecicion del programa solo existiran durante este tiempo de ejecucion del mismo

## Instrucciones
1. Para ejecutar la aplicacion se hace desde el archivo que lleva por nombre `main`
```console
py main.py
```
2. Dentro de la aplicacion se encontrara con un menu para el admin que como primera vez
    - Caso **admin**: Aqui se puede agregar/eliminar un cliente
    - Caso **clientes**: Aqui el cliente tendra que iniciar sesion ingresando su matricula asignada

3. El programa finalizara una vez que el cliente inicie sesion
