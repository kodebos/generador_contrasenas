from generador import GeneradorContrasenas
from evaluador import EvaluadorContrasenas

class Interfaz:
    """
    Clase para manejar la interfaz de usuario
    """
    def __init__(self):
        self.generador = GeneradorContrasenas()
        self.evaluador = EvaluadorContrasenas()

    def mostrar_menu(self):
        """
        Muestra el menu principal
        """
        print("\n" + "="*60)
        print("GENERADOR Y EVALUADOR DE CONTRASEÑAS")
        print("="*60)
        print("\n1. Generar una contraseña segura")
        print("2. Evaluar una contraseña existente")
        print("3. Generar multiples contraseñas")
        print("4. Salir")

    def mostrar_analisis(self, resultado):
        """
        Muestra el analisis completo de una contraseña
        """
        print("\n" + "="*60)
        print("ANALISIS DE CONTRASEÑA")
        print("="*60)
        print(f"\nContraseña analizada: {'*' * resultado['longitud']}")
        print(f"Longitud: {resultado['longitud']} caracteres")
        print(f"Entropia: {resultado['entropia']:.2f} bits")
        print(f"\n{'█' * (resultado['puntuacion'] * 10)} Nivel: {resultado['nivel']}")
        print(f"\nTiempo estimado para hackear: {resultado['tiempo_hackeo']}")
        print(f"(con 10 mil millones de intentos por segundo)")

        if resultado['problemas']:
            print("\nADVERTENCIAS:")
            for problema in resultado['problemas']:
                print(f"   - {problema}")

        print("\nRECOMENDACIONES:")
        if resultado['puntuacion'] < 4:
            print("    - Usa al menos 12-16 caracteres")
            print("    - Combina mayusculas, minusculas, numeros y simbolos")
            print("    - Evita palabras comunes y secuencias")
            print("    - No uses informacion personal")
        else:
            print("    - Excelente! Tu contraseña es muy segura")
        
        print("="*60 + "\n")
    
    def menu_generar(self):
        """
        Menu para generar contraseñas
        """
        print("\n--- GENERADOR DE CONTRASEÑAS ---")
        try:
            longitud = int(input("Logitud de la contraseña (recomendado: 16+): ") or "16")

            print("\nQue tipos de caracteres deseas incluir?")
            mayusculas = input("Mayusculas (A-Z)? (s/n): ").lower() == 's'
            minusculas = input("Minusculas (a-z)? (s/n): ").lower() == 's'
            numeros = input("Numeros (0-9)? (s/n): ").lower() == 's'
            simbolos = input("Simbolos (!@#$...)? (s/n): ").lower() == 's'

            contrasena = self.generador.generar(
                longitud, mayusculas, minusculas, numeros, simbolos
            )

            print(f"\nContraseña generada: {contrasena}")

            evaluar = input("\nDeseas ver el analisis de esta contraseña? (s/n): ")
            if evaluar.lower() == 's':
                resultado = self.evaluador.evaluar(contrasena)
                self.mostrar_analisis(resultado)

        except ValueError as e:
            print(f"Error: {e}")

    def menu_evaluar(self):
        """
        Menu para evaluar contraseñas
        """
        print("\n--- EVALUADOR DE CONTRASEÑAS ---")
        contrasena = input("Ingresa la contraseña a evaluar: ")
        resultado = self.evaluador.evaluar(contrasena)
        self.mostrar_analisis(resultado)

    def menu_generar_multiple(self):
        """
        Menu para generar multiples contraseñas
        """
        print("\n--- GENERADOR MULTIPLE ---")
        try:
            cantidad = int(input("Cuantas contraseñas deseas generar? (1-20): ") or "5")
            cantidad = min(max(cantidad, 1), 20)
            longitud = int(input("Longitud de las contraseñas: ") or "16")

            contrasenas = self.generador.generar_multiple(
                cantidad=cantidad,
                longitud=longitud,
                usar_mayusculas=True,
                usar_minusculas=True,
                usar_numeros=True,
                usar_simbolos=True
            )

            print(f"\n{cantidad} contraseñas generadas: ")
            print("-" * 60)
            for i, pwd in enumerate(contrasenas, 1):
                print(f"{i}. {pwd}")
            print("-" * 60)

        except ValueError as e:
            print(f"Error: {e}")
    
    def ejecutar(self):
        """
        Ejectua el programa principal
        """
        while True:
            self.mostrar_menu()
            opcion = input("\nSelecciona una opcion (1-4): ").strip()

            if opcion == "1":
                self.menu_generar()
            elif opcion == "2":
                self.menu_evaluar()
            elif opcion == "3":
                self.menu_generar_multiple()
            elif opcion == "4":
                print("\nHasta luego! Manten tus contraseñas seguras.\n")
                break
            else:
                print("Opcion invalida. Intente de nuevo.")
