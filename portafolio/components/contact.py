import reflex as rx  
from portafolio.styles.styles import Size, TextColor, Color  
import portafolio.constans as constants  
import portafolio.styles.styles as styles  



def contact() -> rx.Component:  
    return rx.vstack(  
        # Cuadro principal para el encabezado de contacto
        rx.box(  
            rx.text.strong(  
                "Contáctame", 
                font_size=styles.Size.BIG.value,
                color=styles.TextColor.WHITE.value 
            ),
            text_align="center", 
            width="100%",
            margin_y=styles.Size.VERYBIG.value, 
        ),
        
        # Cuadro para el formulario de contacto
        rx.box(  
            rx.form(  
                rx.vstack(  
                    
                    # Campos de entrada para nombre, correo electrónico y mensaje
                    rx.input(  
                        placeholder="Nombre",  
                        name="placeholder", 
                        width="20em" 
                    ),
                    rx.input(  
                        placeholder="Correo electrónico",  
                        name="Correo Electrónico",  
                        width="20em"  
                    ),
                    rx.text_area(  
                        placeholder="Mensaje",
                        name="Mensaje", 
                        width="17.5em",  
                        height="13em"
                    ),
                    
                    # Botón de enviar
                    rx.button(  
                        "Enviar",  
                        type="submit",  
                        widht="100%",  
                        width="20em",  
                        bg=styles.Color.DARKBLUE,  
                        transition=".3s",  
                        _hover={  
                            "bg":styles.Color.BLUE  
                        }
                    )
                )
            ),
            padding=styles.Size.DEFAULT, 
            border_radius="10px",  
            box_shadow=styles.Color.BOXSHADOW, 
            bg=styles.Color.GREY  
        ),
        
        id="contact",  
        scroll_behavior="smooth",
        margin_bottom=styles.Size.VERYBIG  
    )
