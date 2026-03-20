# Sistema de Gestión de Museo

## Descripción

El sistema de Gestión de Museo es una aplicación desarrollada en Python con enfoque orientado a objetos (POO), cuyo objetivo es automatizar la administración de obras de arte dentro de un museo.

Este sistema permite:

- Mantener el catálogo de obras de arte (cuadros, esculturas y otros objetos)
- Gestionar procesos de restauración de obras
- Controlar el estado de las obras (exposición o restauración)
- Administrar la cesión de obras a otros museos
- Consultar la valoración total del museo
- Gestionar usuarios con diferentes roles
- Permitir autenticación para el acceso al sistema
- Consultar listados de obras por parte de visitantes


## Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos (POO)
- Buenas prácticas (PEP8)
- Clean Code
- Principios SOLID


## Programación Orientada a Objetos
- Clase: Estructura que define objetos (ej: Obra, Cuadro, Museo)
- Objeto: Instancia de una clase
- Encapsulamiento: Uso de atributos y métodos dentro de cada clase
- Abstracción: Uso de clases abstractas como Obra y Usuario
- Herencia: Cuadro y Escultura heredan de Obra
- Polimorfismo: Uso de métodos como mostrar_detalle() en diferentes tipos de obras


## Principios SOLID

- S (Single Responsibility): Cada clase tiene una única responsabilidad
    (Ej: GestorRestauracion solo gestiona restauraciones)
- O (Open/Closed): El sistema permite agregar nuevos tipos de obras sin modificar las existentes
- L (Liskov Substitution): Las clases hijas (Cuadro, Escultura) pueden usarse como Obra
- I (Interface Segregation): Uso de interfaces como Autenticable
- D (Dependency Inversion): Uso de servicios desacoplados (AutenticacionService, GestorCesion)


## Funcionalidades principales

### Gestión de obras

- Registro de obras de arte
- Clasificación por tipo (cuadro, escultura, otros)
- Consulta de información detallada

### Restauración de obras

- Inicio y finalización de restauraciones
- Restauraciones automáticas cada 5 años
- Registro histórico de restauraciones
Consulta de restauraciones ordenadas por fecha

### Cesión de obras

- Registro de préstamos a otros museos
- Control de periodos de cesión
- Gestión de ingresos por cesión

### Gestión del museo

- Cálculo de la valoración total de las obras
- Administración de museos colaboradores

### Usuarios del sistema

- Director del museo
- Restaurador jefe
- Encargado del catálogo
- Visitante

### Seguridad

- Autenticación de usuarios
- Control de acceso según rol


## Autor

Proyecto desarrollado por estudiante como parte de formación en Programación Orientada a Objetos y diseño de software.