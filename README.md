# 🌍 World Building Simulator

![Python](https://img.shields.io/badge/Python-3.8+-blue) ![Terminal](https://img.shields.io/badge/Interface-Terminal-green) ![License](https://img.shields.io/badge/License-MIT-gray)

Simulador interactivo de construcción de mundos ejecutado en terminal. El mundo se representa como una matriz 2D donde el usuario puede agregar ciudades, ríos, montañas y más — todo en tiempo real con colores ANSI.

---

## Demo

```
Ingrese el número de filas del mundo: 8
Ingrese el número de columnas del mundo: 8

T T T A A A T T
T M M A T T T T
T M M A C C T T
T T M A C C T T
T T T A T T T T
T T T A T T T T
T T T T T T T T
T T T T T T T T

T=Tierra  A=Agua(río)  M=Montaña  C=Ciudad
```

*(En terminal, cada elemento se muestra con colores ANSI: verde, cian, rojo y blanco)*

---

## Características

- **Mundo configurable**: el usuario define el tamaño de la matriz (M filas × N columnas) al iniciar
- **Agregar ciudades**: cuadrado de lado L a partir de una coordenada (X, Y)
- **Agregar ríos**: dirección vertical, horizontal, diagonal principal o diagonal inversa
- **Agregar montañas**: círculo generado por distancia euclidiana con radio configurable
- **Aplanar zonas**: restaura tierra en una forma específica
- **Eliminar zonas**: convierte una región en vacío
- **Redimensionar mundo**: cambia las dimensiones preservando el contenido existente
- **Deshacer**: revierte la última acción con `copy.deepcopy`
- **Renderizado en color**: salida con códigos ANSI (verde, cian, rojo, blanco)

---

## Conceptos técnicos aplicados

| Concepto | Implementación |
|---|---|
| Matrices 2D | Representación y manipulación completa del mundo |
| Distancia euclidiana | Generación de montañas con forma circular |
| Recorrido diagonal | Ríos en diagonal principal e inversa con coordenadas |
| Deep copy | Sistema de deshacer con `copy.deepcopy` |
| Type hints | Anotaciones de tipo en todas las funciones |
| Docstrings | Documentación de parámetros y valores de retorno |
| Manejo de errores | `try/except` en todas las entradas del usuario |

---

## Requisitos

```
Python 3.8+
Sin dependencias externas — solo librería estándar (math, copy, typing)
```

---

## Instalación y uso

```bash
git clone https://github.com/tu-usuario/world-building-simulator
cd world-building-simulator
python3 world_building.py
```

### Opciones del menú

```
1. Imprimir mundo
2. Agregar ciudad     → solicita fila X, columna Y, lado L
3. Agregar río        → solicita fila X, columna Y y dirección (vertical/horizontal/diagonal)
4. Agregar montaña    → solicita centro X/Y y radio R
5. Aplanar zona       → restaura tierra en una forma seleccionada
6. Eliminar zona      → convierte una forma en espacio vacío
7. Redimensionar      → cambia dimensiones del mundo
8. Deshacer           → revierte la última modificación
9. Salir
```

---

## Estructura del proyecto

```
world-building-simulator/
├── world_building.py   # Código principal
└── README.md
```

---

## Autor

Carlos Wendehake  
Laboratorio de Algoritmos y Estructuras I — Universidad Simón Bolívar  
carrera: Ingeniería en Computación
