#  Sistema TeleVentas

## Descripción

El sistema TeleVentas es una aplicación desarrollada en Python con enfoque orientado a objetos (POO), cuyo objetivo es gestionar el proceso de compras a distancia de productos por parte de clientes.

Este sistema permite:

- Consultar el catálogo de productos
- Realizar órdenes de compra
- Procesar pagos (tarjeta de crédito)
- Gestionar quejas de clientes
- Coordinar la logística de envío de pedidos
- Integrarse con un sistema de inventario

---

## Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos (POO)
- Buenas prácticas (PEP8)
- Principios SOLID

---

###  Programación Orientada a Objetos

- Clase: Estructura que define objetos (ej: Producto).
- Objeto: Instancia de una clase.
- Encapsulamiento: Organización de atributos y métodos.
- Abstracción: Uso de clases abstractas como Pago.
- Herencia: PagoTarjeta hereda de Pago.
- Polimorfismo: Uso de diferentes tipos de pago mediante la misma interfaz.

###  Principios SOLID

- **S (Single Responsibility):** Cada clase tiene una única responsabilidad  
- **O (Open/Closed):** El sistema permite extensión sin modificar código existente  
- **L (Liskov Substitution):** Las clases hijas pueden sustituir a las padres  
- **I (Interface Segregation):** Interfaces específicas  
- **D (Dependency Inversion):** Dependencia de abstracciones  

---


##  Funcionalidades principales

- Gestión de productos
- Consulta de catálogo
- Creación de órdenes de compra
- Procesamiento de pagos
- Registro de quejas
- Gestión de envíos

---

## Autor

Proyecto desarrollado por estudiante como parte de formación en programación orientada a objetos.