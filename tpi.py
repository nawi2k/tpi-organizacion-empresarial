import sys
import random

# Definición de los Estados del Chatbot
ESTADO_BIENVENIDA = "BIENVENIDA"
ESTADO_VALIDANDO_LEGAJO = "VALIDANDO_LEGAJO"
ESTADO_SELECCION_MENU = "SELECCION_MENU"
ESTADO_GENERANDO_TICKET = "GENERANDO_TICKET"
ESTADO_RESOLUCION = "RESOLUCION" 
ESTADO_FIN = "FIN"

class BotSoporteTI:
    def __init__(self):
        self.estado_actual = ESTADO_BIENVENIDA
        self.legajos_validos = [101, 102, 103, 104, 105]
        self.intentos_legajo = 0
        self.max_intentos = 3
        self.legajo_usuario = None
        self.categoria_problema = None
        self.num_ticket = None

    def iniciar_chat(self):
        print("=== CHATBOT DE SOPORTE TÉCNICO NIVEL 1 ===")
        self.procesar_estados()  # Arranca directo a procesar desde el __init__

    def procesar_estados(self):
        while self.estado_actual != ESTADO_FIN:
            
            # --- ESTADO: BIENVENIDA 
            if self.estado_actual == ESTADO_BIENVENIDA:
                print("Bot: ¡Hola! Bienvenido al asistente automático de IT de la empresa.")
                self.estado_actual = ESTADO_VALIDANDO_LEGAJO
            
            # --- ESTADO: VALIDANDO LEGAJO ---
            elif self.estado_actual == ESTADO_VALIDANDO_LEGAJO:
                print(f"\nBot: Por favor, para comenzar ingresá tu número de legajo (Intentos: {self.intentos_legajo}/{self.max_intentos}):")
                entrada = input("Usuario: ").strip()
                
                if not entrada.isdigit():
                    print("Bot: ❌ Error: El legajo debe contener solo números.")
                    self.intentos_legajo += 1
                else:
                    legajo_num = int(entrada)
                    if legajo_num in self.legajos_validos:
                        print(f"Bot: ¡Legajo {legajo_num} verificado con éxito!")
                        self.legajo_usuario = legajo_num
                        self.estado_actual = ESTADO_SELECCION_MENU
                    else:
                        print("Bot: ❌ Error: El número de legajo no existe en el sistema.")
                        self.intentos_legajo += 1
                
                if self.intentos_legajo >= self.max_intentos and self.estado_actual != ESTADO_SELECCION_MENU:
                    print("\nBot: 🛑 Demasiados intentos fallidos. Solicitud denegada por seguridad.")
                    self.estado_actual = ESTADO_FIN

            # --- ESTADO: SELECCIÓN DE MENÚ ---
            elif self.estado_actual == ESTADO_SELECCION_MENU:
                print("\nBot: Seleccioná el tipo de problema informático que estás teniendo:")
                print("1 - Problema de HARDWARE (PC no enciende, monitor negro, periféricos, cables).")
                print("2 - Problema de SOFTWARE (Falla en el correo, sistema caído, instalación de apps).")
                entrada = input("Usuario: ").strip()
                
                if entrada not in ["1", "2"]:
                    print("Bot: ❌ Opción inválida. Por favor, ingresá solo el número '1' o '2'.")
                else:
                    self.categoria_problema = "Hardware" if entrada == "1" else "Software"
                    self.estado_actual = ESTADO_GENERANDO_TICKET

            # --- ESTADO: GENERANDO TICKET (Con guardado en Base de Datos de texto) ---
            elif self.estado_actual == ESTADO_GENERANDO_TICKET:
                print(f"\nBot: Procesando solicitud... Guardando en la Base de Datos...")
                self.num_ticket = random.randint(4000, 9999)
                
                # --- AQUÍ SE GUARDA EN EL ARCHIVO (BASE DE DATOS SOLICITADA) ---
                try:
                    with open("base_de_datos_tickets.txt", "a", encoding="utf-8") as archivo_bd:
                        linea_ticket = f"Ticket: #{self.num_ticket} | Empleado: {self.legajo_usuario} | Categoría: {self.categoria_problema} | Estado: Pendiente\n"
                        archivo_bd.write(linea_ticket)
                    print("Bot: 💾 ¡Datos registrados en el archivo de persistencia con éxito!")
                except Exception as e:
                    print(f"Bot: ⚠️ Error al conectar con el archivo de datos: {e}")
                
                print("\n=======================================================")
                print("🚨 ¡TICKET DE SOPORTE GENERADO CON ÉXITO! 🚨")
                print(f"• Número de Ticket: #{self.num_ticket}")
                print(f"• Legajo de Empleado: {self.legajo_usuario}")
                print(f"• Categoría de Falla: {self.categoria_problema}")
                print("=======================================================")
                self.estado_actual = ESTADO_RESOLUCION

            # --- ESTADO: RESOLUCIÓN Y ESCALABILIDAD (Camino lógico extra) ---
            elif self.estado_actual == ESTADO_RESOLUCION:
                print("\nBot: El sistema aplicó una solución automática estándar para tu problema.")
                print("¿Se solucionó el inconveniente con esta guía rápida? (S / N):")
                respuesta = input("Usuario: ").strip().upper()
                
                if respuesta == "S":
                    print(f"\nBot: ¡Excelente! Procedemos a cerrar el Ticket #{self.num_ticket} en la base de datos. Gracias.")
                    
                    # Actualizamos el estado en el archivo si quieren ser ultra detallistas
                    with open("base_de_datos_tickets.txt", "a", encoding="utf-8") as archivo_bd:
                        archivo_bd.write(f"-> Actualización Ticket #{self.num_ticket}: Resuelto por el usuario.\n")
                        
                    self.estado_actual = ESTADO_FIN
                elif respuesta == "N":
                    print(f"\nBot: Entendido. El Ticket #{self.num_ticket} fue derivado de forma URGENTE a un Técnico Nivel 2.")
                    
                    with open("base_de_datos_tickets.txt", "a", encoding="utf-8") as archivo_bd:
                        archivo_bd.write(f"-> Actualización Ticket #{self.num_ticket}: Escalado a Soporte Nivel 2.\n")
                        
                    self.estado_actual = ESTADO_FIN
                else:
                    print("Bot: ❌ Opción inválida. Por favor, respondé con 'S' para Sí o 'N' para No.")

        print("\n[Simulación finalizada - Conexión cerrada]")

if __name__ == "__main__":
    bot = BotSoporteTI()
    bot.iniciar_chat()