import reflex as rx  # Importa la biblioteca reflex como rx
# Importa tamaños, colores y estilos de otro módulo
from portafolio.styles.styles import Size, TextColor, Color  
# Importa constantes de otro módulo
import portafolio.constans as constants  
# Importa estilos de otro módulo
import portafolio.styles.styles as styles  


def footer() -> rx.Component:  # Define una función llamada 'footer' que devuelve un componente reflex
    return rx.vstack(  # Crea un contenedor vertical
    
        # Texto del pie de página
        rx.text(  
            "Hecho con ❤️ y con ☕ por ValleDev",  # Texto
            color=styles.TextColor.WHITE,  # Color de texto
            margin= "0 auto"  # Margen centrado horizontalmente
        ),
        width="100%",  # Establece el ancho al 100%
        heigth="20em",  # Establece la altura a 20em
        bg=styles.Color.LIGHTBLUE,  # Establece el color de fondo
        padding="2em"  # Establece el relleno de 2em
    )
