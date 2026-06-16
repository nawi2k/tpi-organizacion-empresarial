import sys

# Definición de los Estados del Chatbot
ESTADO_BIENVENIDA = "BIENVENIDA"
ESTADO_VALIDANDO_LEGAJO = "VALIDANDO_LEGAJO"
ESTADO_SELECCION_MENU = "SELECCION_MENU"
ESTADO_GENERANDO_TICKET = "GENERANDO_TICKET"
ESTADO_FIN = "FIN"

class BotSoporteTI:
    def __init__(self):
        self.estado_actual = ESTADO_BIENVENIDA
        # Base de datos simulada de empleados (Regla de negocio)
        self.legajos_validos = [101, 102, 103, 104, 105]
        self.intentos_legajo = 0
        self.max_intentos = 3
        self.legajo_usuario = None
        self.categoria_problema = None

    def iniciar_chat(self):
        print("=== CHATBOT DE SOPORTE TÉCNICO NIVEL 1 ===")
        print("Bot: ¡Hola! Bienvenido al asistente automático de IT de la empresa.")
        self.estado_actual = ESTADO_VALIDANDO_LEGAJO
        self.procesar_estados()

    def procesar_estados(self):
        while self.estado_actual != ESTADO_FIN:
            
            # --- ESTADO: VALIDANDO LEGAJO ---
            if self.estado_actual == ESTADO_VALIDANDO_LEGAJO:
                print(f"\nBot: Por favor, para comenzar ingresá tu número de legajo (Intentos: {self.intentos_legajo}/{self.max_intentos}):")
                entrada = input("Usuario: ").strip()
                
                # --- MANEJO DEL CAMINO INFELIZ (Errores de entrada) ---
                if not entrada.isdigit():
                    print("Bot: ❌ Error: El legajo debe contener solo números.")
                    self.intentos_legajo += 1
                else:
                    legajo_num = int(entrada)
                    if legajo_num in self.legajos_validos:
                        print(f"Bot: ¡Legajo {legajo_num} verificado con éxito!")
                        self.legajo_usuario = legajo_num
                        self.estado_actual = ESTADO_SELECCION_MENU  # Transición de estado
                    else:
                        print("Bot: ❌ Error: El número de legajo no existe en el sistema.")
                        self.intentos_legajo += 1
                
                # Control de bloqueo por intentos fallidos (Robusted del sistema)
                if self.intentos_legajo >= self.max_intentos and self.estado_actual != ESTADO_SELECCION_MENU:
                    print("\nBot: 🛑 Demasiados intentos fallidos. Solicitud denegada por seguridad.")
                    self.estado_actual = ESTADO_FIN

            # --- ESTADO: SELECCIÓN DE MENÚ ---
            elif self.estado_actual == ESTADO_SELECCION_MENU:
                print("\nBot: Seleccioná el tipo de problema informático que estás teniendo:")
                print("1 - Problema de HARDWARE (PC no enciende, monitor negro, periféricos, cables).")
                print("2 - Problema de SOFTWARE (Falla en el correo, sistema caído, instalación de apps).")
                entrada = input("Usuario: ").strip()
                
                # --- MANEJO DEL CAMINO INFELIZ (Opción inválida) ---
                if entrada not in ["1", "2"]:
                    print("Bot: ❌ Opción inválida. Por favor, ingresá solo el número '1' o '2'.")
                else:
                    self.categoria_problema = "Hardware" if entrada == "1" else "Software"
                    self.estado_actual = ESTADO_GENERANDO_TICKET  # Transición

            # --- ESTADO: GENERANDO TICKET ---
            elif self.estado_actual == ESTADO_GENERANDO_TICKET:
                print(f"\nBot: Procesando solicitud... Conectando con la Base de Datos...")
                # Simulación de número de ticket único aleatorio
                import random
                num_ticket = random.randint(4000, 9999)
                
                print("\n=======================================================")
                print("🚨 ¡TICKET DE SOPORTE GENERADO CON ÉXITO! 🚨")
                print(f"• Número de Ticket: #{num_ticket}")
                print(f"• Legajo de Empleado: {self.legajo_usuario}")
                print(f"• Categoría de Falla: {self.categoria_problema}")
                print("• Estado actual: Asignado a Técnico de Guardia Nivel 1.")
                print("=======================================================")
                
                print("\nBot: El equipo de sistemas se comunicará con vos a la brevedad. ¡Que tengas un buen día!")
                self.estado_actual = ESTADO_FIN

        print("\n[Simulación finalizada - Conexión cerrada]")

# Bloque principal para ejecutar
if __name__ == "__main__":
    bot = BotSoporteTI()
    bot.iniciar_chat()