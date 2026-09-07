from typing import Dict, Any, Optional

# Base de datos simulada en memoria (puedes enlazarla a tu vectorstore o SQL)
CATALOGO_PRECIOS = {
    "PKM-001-PLA-U": {"nombre": "Pikachu (PLA Sin Pintar)", "precio": 12.00, "dias_fab": 1},
    "PKM-001-RES-P": {"nombre": "Pikachu (Resina Pintado)", "precio": 35.00, "dias_fab": 3},
    "PKM-004-PLA-U": {"nombre": "Charmander (PLA Sin Pintar)", "precio": 12.00, "dias_fab": 1},
    "PKM-006-RES-P": {"nombre": "Charizard (Resina Pintado)", "precio": 110.00, "dias_fab": 7},
    "PKM-094-RES-U": {"nombre": "Gengar (Resina Sin Pintar)", "precio": 28.00, "dias_fab": 2},
    "PKM-094-RES-P": {"nombre": "Gengar (Resina Pintado)", "precio": 65.00, "dias_fab": 5},
    "PKM-143-PLA-U": {"nombre": "Snorlax (PLA Sin Pintar)", "precio": 45.00, "dias_fab": 4},
    "PKM-143-PLA-P": {"nombre": "Snorlax (PLA Pintado)", "precio": 95.00, "dias_fab": 8},
    "PKM-150-RES-P": {"nombre": "Mewtwo (Resina Pintado)", "precio": 85.00, "dias_fab": 6},
    "PKM-249-RES-P": {"nombre": "Lugia (Resina Pintado)", "precio": 140.00, "dias_fab": 10},
}

COSTOS_ENVIO = {
    "medellin": {"costo": 3.50, "dias": 0, "nombre": "Medellín & Área Met. (Mensajería Local)"},
    "colombia_estandar": {"costo": 7.00, "dias": 3, "nombre": "Colombia Nacional (Servientrega)"},
    "colombia_express": {"costo": 12.00, "dias": 2, "nombre": "Colombia Express (FedEx)"},
    "latam": {"costo": 22.00, "dias": 10, "nombre": "Latinoamérica (DHL)"},
    "usa_canada": {"costo": 28.00, "dias": 6, "nombre": "USA & Canadá (FedEx Express)"},
    "europa": {"costo": 35.00, "dias": 10, "nombre": "Europa (UPS)"},
}

def calcular_cotizacion_figura(
    id_producto: str,
    cantidad: int = 1,
    es_shiny: bool = False,
    cambio_pose: bool = False,
    accesorio_extra: bool = False,
    incluir_diorama: bool = False,
    costo_diorama: float = 20.0,
    destino_envio: Optional[str] = None
) -> Dict[str, Any]:
    """
    Calcula el costo total, desglose de precios y tiempo estimado de fabricación
    y envío para una figura de PokéPrint 3D.
    """
    if id_producto not in CATALOGO_PRECIOS:
        return {
            "error": f"El ID de producto '{id_producto}' no existe en el catálogo.",
            "ids_validos": list(CATALOGO_PRECIOS.keys())
        }
    
    prod = CATALOGO_PRECIOS[id_producto]
    precio_base_unitario = prod["precio"]
    dias_fabricacion_unitario = prod["dias_fab"]
    
    # Adicionales por unidad
    costo_adicionales_unitario = 0.0
    dias_adicionales = 0
    desglose_adicionales = []

    if es_shiny:
        costo_adicionales_unitario += 5.0
        desglose_adicionales.append("Versión Shiny (+$5.00)")
        
    if cambio_pose:
        costo_adicionales_unitario += 15.0
        dias_adicionales += 2
        desglose_adicionales.append("Cambio de Pose Custom (+$15.00)")
        
    if accesorio_extra:
        costo_adicionales_unitario += 10.0
        dias_adicionales += 1
        desglose_adicionales.append("Accesorio Extra (+$10.00)")
        
    if incluir_diorama:
        costo_adicionales_unitario += costo_diorama
        dias_adicionales += 3
        desglose_adicionales.append(f"Base Diorama (+${costo_diorama:.2f})")

    # Cálculos acumulados
    precio_unitario_total = precio_base_unitario + costo_adicionales_unitario
    subtotal_productos = precio_unitario_total * cantidad
    
    # Envíos
    costo_envio = 0.0
    dias_envio = 0
    metodo_envio_nombre = "Sin envío seleccionado"
    
    if destino_envio:
        if destino_envio in COSTOS_ENVIO:
            envio_info = COSTOS_ENVIO[destino_envio]
            costo_envio = envio_info["costo"]
            dias_envio = envio_info["dias"]
            metodo_envio_nombre = envio_info["nombre"]
        else:
            return {
                "error": f"Destino de envío '{destino_envio}' no válido.",
                "destinos_validos": list(COSTOS_ENVIO.keys())
            }

    # Totales
    total_general = subtotal_productos + costo_envio
    tiempo_total_dias = (dias_fabricacion_unitario + dias_adicionales) + dias_envio

    return {
        "producto": prod["nombre"],
        "id_producto": id_producto,
        "cantidad": cantidad,
        "desglose": {
            "precio_base_unitario_usd": precio_base_unitario,
            "adicionales_unitarios_usd": costo_adicionales_unitario,
            "detalles_adicionales": desglose_adicionales,
            "subtotal_productos_usd": subtotal_productos,
            "metodo_envio": metodo_envio_nombre,
            "costo_envio_usd": costo_envio
        },
        "total_usd": round(total_general, 2),
        "tiempo_estimado_entrega_dias_habiles": tiempo_total_dias
    }