markdown_content = """# Base de Datos de Conocimiento - PokéPrint 3D
**Descripción**: Archivo estructurado con información detallada sobre productos, precios, envíos y políticas de **PokéPrint 3D**, una empresa dedicada a la impresión 3D y pintado a mano de figuras de Pokémon. Diseñado para ser vectorizado e ingerido por un sistema RAG (Retrieval-Augmented Generation).

---

## 1. Información General de la Empresa

*   **Nombre Comercial:** PokéPrint 3D S.A.S.
*   **Sede Central:** Medellín, Antioquia, Colombia.
*   **Materiales Utilizados:** 
    *   **PLA (Poliácido Láctico):** Plástico biodegradable, ideal para figuras grandes y resistentes.
    *   **Resina 8K:** Alta precisión, recomendada para figuras pequeñas con alto nivel de detalle.
*   **Acabados Disponibles:**
    *   *Impresión Cruda (Sin pintar):* Se entrega con los soportes retirados y lijado básico, color base gris o blanco.
    *   *Pintado a Mano (Premium):* Imprimación, pintura acrílica de alta calidad y doble capa de barniz protector (mate o brillante).

---

## 2. Catálogo de Figuras Estándar (Precios en USD)

| ID_Producto | Pokémon | Tipo de Impresión | Tamaño Alto (cm) | Acabado | Precio (USD) | Stock Actual | Tiempo de Fabricación |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| PKM-001-PLA-U | Pikachu | PLA Estándar | 10 cm | Sin Pintar | $12.00 | 15 | 1 día |
| PKM-001-RES-P | Pikachu | Resina 8K | 10 cm | Pintado a Mano | $35.00 | 5 | 3 días |
| PKM-004-PLA-U | Charmander | PLA Estándar | 10 cm | Sin Pintar | $12.00 | 10 | 1 día |
| PKM-006-RES-P | Charizard | Resina 8K | 25 cm | Pintado a Mano | $110.00 | 2 | 7 días |
| PKM-094-RES-U | Gengar | Resina Alta Def. | 15 cm | Sin Pintar | $28.00 | 8 | 2 días |
| PKM-094-RES-P | Gengar | Resina Alta Def. | 15 cm | Pintado a Mano | $65.00 | 3 | 5 días |
| PKM-143-PLA-U | Snorlax | PLA Estándar | 30 cm | Sin Pintar | $45.00 | 4 | 4 días |
| PKM-143-PLA-P | Snorlax | PLA Estándar | 30 cm | Pintado a Mano | $95.00 | 1 | 8 días |
| PKM-150-RES-P | Mewtwo | Resina 8K | 20 cm | Pintado a Mano | $85.00 | 2 | 6 días |
| PKM-249-RES-P | Lugia | Resina 8K | 35 cm | Pintado a Mano | $140.00 | 0 (Bajo pedido)| 10 días |

---

## 3. Costos y Tiempos de Envío

Los envíos se realizan a través de diferentes transportadoras según el destino. Los días mencionados son **días hábiles** tras finalizar la etapa de fabricación.

| Destino | Método de Envío | Transportadora | Costo (USD) | Tiempo Estimado | Rastreo Incluido |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Medellín & Área Met. | Mensajería Local | EnvíaExpress | $3.50 | Mismo día | Sí |
| Colombia (Nacional) | Estándar Nacional| Servientrega | $7.00 | 2 - 4 días | Sí |
| Colombia (Nacional) | Express Nacional | FedEx Colombia | $12.00 | 1 - 2 días | Sí |
| Latinoamérica | Estándar Int. | DHL eCommerce | $22.00 | 7 - 14 días | Sí |
| USA & Canadá | Priority Int. | FedEx Express | $28.00 | 5 - 8 días | Sí |
| Europa | Priority Int. | UPS | $35.00 | 8 - 12 días | Sí |

---

## 4. Trabajos Personalizados y Comisiones

Ofrecemos modelado 3D personalizado y modificación de poses o accesorios (ej. un Pikachu usando el gorro de Ash o sosteniendo una Pokéball específica).

| Servicio Adicional | Descripción | Costo Adicional (USD) | Tiempo Extra |
| :--- | :--- | :--- | :--- |
| Cambio de Pose | Alteración del archivo 3D base | + $15.00 | + 2 días |
| Accesorio Extra | Añadir objeto no canónico a la figura | + $10.00 | + 1 día |
| Versión Shiny | Pintura con paleta de colores Shiny | + $5.00 | + 0 días |
| Tamaño Custom | Escalar la figura a una altura específica | Cotización a medida | Variable |
| Base Diorama | Creación de base temática (Ej. césped, agua) | Desde $20.00 | + 3 días |

---

## 5. Preguntas Frecuentes (FAQ) y Políticas

### 5.1. ¿Qué pasa si mi figura llega rota?
Contamos con una **Garantía de Llegada Segura**. Si la figura llega dañada por el transporte, el cliente tiene **48 horas** desde la recepción para enviar evidencia fotográfica al correo `soporte@pokeprint3d.com`. Cubriremos el costo de enviar un reemplazo sin costo adicional.

### 5.2. ¿Aceptan devoluciones?
Debido a la naturaleza personalizada y bajo demanda de nuestros productos, **no aceptamos devoluciones** por cambio de opinión una vez que el proceso de fabricación ha comenzado. Solo se aceptan devoluciones o reembolsos en caso de defectos de fabricación graves.

### 5.3. ¿Hacen figuras de otras franquicias (Digimon, Yu-Gi-Oh)?
Actualmente, nuestro foco comercial, catálogo y permisos artísticos están limitados a Pokémon. No realizamos modelados desde cero de otras franquicias, pero si el cliente proporciona el archivo `.stl` ya listo para imprimir, podemos ofrecer el servicio de impresión bajo la categoría de "Impresión Genérica".

### 5.4. ¿Cómo cuidar mi figura pintada?
Se recomienda:
1.  Mantenerla alejada de la luz solar directa prolongada (los rayos UV pueden decolorar la pintura acrílica y quebrar la resina).
2.  Limpiar el polvo con un pincel de cerdas suaves o un soplador de aire, **nunca** con paños húmedos o productos químicos.
3.  Evitar caídas; la resina 8K, aunque detallada, es un material rígido que puede fracturarse con impactos fuertes.

---

*Última actualización de la base de datos: 7 de Septiembre de 2026*
"""

file_path = "/tmp/pokeprint_3d_db_rag.md"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(markdown_content)

file_path