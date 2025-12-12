# Generador y Evaluador de Contraseñas

Un programa completo en Python para generar contraseñas seguras y evaluar la fortaleza de contraseñas existentes.

## Características

- **Generador de Contraseñas**: Crea contraseñas aleatorias y seguras con opciones personalizables
- **Evaluador de Seguridad**: Analiza la fortaleza de cualquier contraseña
- **Cálculo de Tiempo de Hackeo**: Estima cuánto tiempo tomaría descifrar la contraseña
- **Detección de Patrones Débiles**: Identifica vulnerabilidades comunes
- **Clasificación por Niveles**: Precaria, Débil, Moderada, Segura, Muy Segura

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/tu-usuario/generador-contraseñas.git
cd generador-contraseñas
```

2. Requisitos:
- Python 3.6 o superior
- No requiere librerías externas (solo módulos estándar)

## Uso

### Ejecución básica

```bash
python main.py
```

## Estructura del Proyecto

```
generador_contrasenas/
│
├── main.py              # Punto de entrada del programa
├── generador.py         # Clase GeneradorContraseñas
├── evaluador.py         # Clase EvaluadorContraseñas
├── interfaz.py          # Interfaz de usuario en consola
├── LICENSE              # Licencia MIT
└── README.md            # Este archivo
```

## Funcionalidades Detalladas

### Generador de Contraseñas

- Longitud personalizable
- Opciones para incluir/excluir:
  - Letras mayúsculas (A-Z)
  - Letras minúsculas (a-z)
  - Números (0-9)
  - Símbolos especiales (!@#$%^&*...)
- Generación de múltiples contraseñas simultáneamente

### Evaluador de Contraseñas

**Métricas de evaluación:**
- **Entropía**: Mide la aleatoriedad en bits
- **Tiempo de hackeo**: Estimación basada en 10 mil millones de intentos/segundo
- **Nivel de seguridad**: Clasificación en 5 niveles
- **Detección de patrones**:
  - Contraseñas comunes (password, 123456, etc.)
  - Secuencias numéricas (123, 456, 789)
  - Secuencias alfabéticas (abc, def, ghi)
  - Caracteres repetidos

**Niveles de seguridad:**
- **Precaria** (< 28 bits): Se puede hackear en minutos/horas
- **Débil** (28-36 bits): Se puede hackear en días
- **Moderada** (36-60 bits): Se puede hackear en años
- **Segura** (60-80 bits): Se puede hackear en miles de años
- **Muy Segura** (> 80 bits): Se puede hackear en millones/miles de millones de años

## Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz un Fork del proyecto
2. Crea una rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`)
3. Haz commit de tus cambios (`git commit -m 'Agrega nueva funcionalidad'`)
4. Haz Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
