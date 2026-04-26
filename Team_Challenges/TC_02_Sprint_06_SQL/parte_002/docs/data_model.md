# Data Model Documentation

Este documento describe las decisiones de diseño del modelo de datos, incluyendo campos categóricos, reglas de negocio y justificaciones de normalización.

---

## orders

Contiene la información de los pedidos realizados por los clientes, incluyendo su estado y las fechas clave del proceso de envío y entrega.

### status
Campo categórico que indica el estado del pedido.

Valores posibles:
- pending
- confirmed
- shipped
- delivered
- cancelled
- returned

---

## payments

Un pedido puede tener uno o varios pagos asociados a lo largo de su ciclo de vida.

Esto permite contemplar escenarios como:
- reintentos de pago tras fallos
- pagos fallidos
- reembolsos

### status
Estado del pago asociado a un pedido.

Valores posibles:
- completed → pago realizado correctamente
- refunded → pago reembolsado
- pending → pago en proceso
- failed → pago fallido

El estado del pago permite analizar incidencias y tasas de fallo en el proceso de compra.

Un pedido se considera pagado cuando al menos uno de sus pagos tiene estado `completed`.

### payment_type
Tipo de operación asociada al pago.

Valores posibles:
- payment → pago realizado por el cliente
- refund → devolución del importe al cliente

### payment_method
Método de pago utilizado por el cliente.

Ejemplos:
- credit_card
- paypal
- bank_transfer

La combinación de `status` y `payment_type` permite modelar de forma flexible el ciclo completo de pagos y devoluciones.

---

## reviews

### rating
Valor numérico que representa la valoración del producto.

Rango permitido:
- mínimo: 1
- máximo: 5

Solo se permiten valoraciones para productos asociados a líneas de pedido entregadas.

Esto garantiza que las valoraciones provienen de compras reales y evita datos inconsistentes.

---

## products

### is_available

Indica si el producto está activo en el catálogo.

Valores:
- true → producto activo y disponible para la venta
- false → producto inactivo (no visible o no vendible), independientemente del stock

### price y cost
Los campos `price` y `cost` se han definido como `float` por simplicidad y compatibilidad con BigQuery, aunque en entornos productivos se recomienda el uso de tipos `decimal` para evitar problemas de precisión.

#### is_available vs stock
Un producto puede tener stock disponible y estar inactivo por motivos comerciales, logísticos o de catálogo.

---

## customers

### source_channel
Canal por el cual el cliente conoció la empresa.

Valores posibles:
- organic
- paid_ads
- social_media
- referral

Este campo permite analizar el rendimiento de los distintos canales de adquisición.

---

## categories

Contiene la clasificación de los productos en distintas categorías del catálogo.

### name
Nombre de la categoría.

### description
Descripción opcional de la categoría.

---

## order_items

Tabla intermedia que representa la relación entre `orders` y `products`, resolviendo la relación de muchos a muchos entre ambas entidades.

Incluye información específica de cada línea de pedido, como cantidad, precio unitario en el momento de la compra y descuentos aplicados.

El campo `unit_price` permite preservar el precio histórico del producto en el momento de la compra.

---

## Decisiones de diseño

### Diferencia entre `order_items.unit_price` y `products.price`

El campo `unit_price` se almacena en `order_items` para preservar el precio del producto en el momento de la compra. Esto permite mantener un histórico fiable de los pedidos, incluso si el precio del producto cambia con el tiempo.

Por otro lado, `products.price` representa el precio actual del producto en el catálogo, que puede modificarse.

Esta separación evita inconsistencias en el análisis de pedidos y garantiza la integridad de los datos históricos, especialmente en escenarios donde los precios varían a lo largo del tiempo.

### `customers.country`

Se mantiene como atributo directo para simplificar el modelo, ya que no se considera necesario normalizar esta información en una tabla independiente para este caso de uso.

### Evitar redundancia en orders (3NF)

Incumpliría 3NF porque `customer_name` dependería de `customer_id`, y no directamente de la clave primaria de `orders`, generando una dependencia transitiva y vulnerando la tercera forma normal.

### Relación reviews con order_items

No relacionamos `reviews` con `orders` porque la valoración no se hace sobre el pedido completo, sino sobre un producto concreto dentro de ese pedido.

Un pedido puede contener varios productos, y cada uno puede tener una valoración distinta. Por eso, la relación correcta es con `order_items`, que representa cada producto dentro del pedido.