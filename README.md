# Chatbot de Soporte Técnico Nivel 1 — Mesa de Ayuda IT

Trabajo Práctico Integrador — **Organización Empresarial** (TUPaD – UTN)
Estudiantes: Josias Avram · Nahuel Sandoval

Simulador de consola (CLI) en **Python puro** que automatiza el proceso administrativo de Soporte Técnico Nivel 1: valida el legajo del empleado, clasifica el problema, emite un ticket, lo persiste en una base de datos de texto, verifica la resolución y escala a Nivel 2 si corresponde.

El bot está construido como una **máquina de estados finita (FSM)** y modela fielmente el diagrama BPMN 2.0 del informe (lanes Usuario / Bot, 3 gateways de decisión y manejo de caminos infelices).

## Requisitos

- Python 3.x (no usa librerías externas, solo `sys` y `random` de la stdlib)

## Cómo ejecutarlo

1. Cloná el repositorio:

   ```bash
   git clone https://github.com/nawi2k/tpi-organizacion-empresarial.git
   cd tpi-organizacion-empresarial
   ```

2. Ejecutá el simulador:

   ```bash
   python tpi.py
   ```

   (En algunos sistemas puede ser `python3 tpi.py`)

## Cómo usarlo

El bot guía paso a paso desde la consola:

1. **Legajo** — ingresá un legajo válido: `101`, `102`, `103`, `104` o `105`. Tenés 3 intentos.
2. **Tipo de problema** — `1` para Hardware o `2` para Software.
3. **Ticket** — el bot genera un número de ticket y lo guarda en `base_de_datos_tickets.txt`.
4. **Resolución** — respondé `S` (resuelto, cierra el ticket) o `N` (escala a Técnico Nivel 2).

## Persistencia

Al ejecutar, el bot crea/actualiza el archivo `base_de_datos_tickets.txt` (modo append) con cada ticket y sus cambios de estado: `Pendiente` → `Resuelto por el usuario` o `Escalado a Soporte Nivel 2`.

## Estados del bot (FSM)

| Estado | Función |
|---|---|
| `BIENVENIDA` | Mensaje de inicio → pasa a validar legajo |
| `VALIDANDO_LEGAJO` | Valida legajo (numérico + en lista, máx. 3 intentos) |
| `SELECCION_MENU` | Elige categoría Hardware / Software |
| `GENERANDO_TICKET` | Genera ticket aleatorio (4000–9999) y lo guarda en BD |
| `RESOLUCION` | Verifica resolución (S/N) y cierra o escala |
| `FIN` | Cierra la sesión |

## Estructura del repositorio

```
tpi-organizacion-empresarial/
├── tpi.py          # Código fuente del simulador
└── README.md       # Este archivo
```