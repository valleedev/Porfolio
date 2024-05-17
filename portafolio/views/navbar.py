import reflex as rx 
from portafolio.styles.styles import Size, TextColor, Color  
from portafolio.styles.colors import Color  


def navbar() -> rx.Component: 
    return rx.vstack(
        rx.hstack(  
            # Logotipo
            rx.text(  
                "{ ValleDev }",  
                weight="bold",  
                size="6",  
                color=TextColor.WHITE.value,  
            ),
            # Enlaces de navegación
            rx.hstack(  
                # Enlace de Inicio
                rx.link(  
                    "Inicio", 
                    href="#header",
                    color=TextColor.WHITE.value, 
                    margin_x=Size.DEFAULT.value  
                ),
                # Enlace de Sobre mí
                rx.link(  
                    "Sobre mí",  
                    href="#aboutme",  
                    color=TextColor.WHITE.value,  
                    margin_x=Size.DEFAULT.value  
                ),
                # Enlace de Experiencia
                rx.link(  
                    "Experiencia",  
                    href="#experience",  
                    color=TextColor.WHITE.value,  
                    margin_x=Size.DEFAULT.value  
                ),
                # Enlace de Skills
                rx.link(  
                    "Skills",  
                    href="#skills",  
                    color=TextColor.WHITE.value,  
                    margin_x=Size.DEFAULT.value  
                ),
                # Enlace de Proyectos
                rx.link(  
                    "Proyectos",  
                    href="#projects",  
                    color=TextColor.WHITE.value,  
                    margin_x=Size.DEFAULT.value  
                ),
                # Enlace de Contacto
                #rx.link(  
                #    "Contácto",  
                #   href="#contact",  
                #  color=TextColor.WHITE.value,  
                # margin_x=Size.DEFAULT.value  
                #),
                margin_left=["5em", "5em", "5em", "10em", "15em", "15em"],
                display=["none", "none", "none", "flex", "flex", "flex"]
            ),
        ),
        bg=Color.DARK.value, 
        position="fixed",
        padding_x=Size.BIG.value, 
        padding_y=Size.DEFAULT.value,  
        z_index="999", 
        top="0",  
        width="100%" 
    )
