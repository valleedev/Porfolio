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
                color=TextColor.LIGHTBLUE.value,  
            ),
            # Enlaces de navegación
            rx.hstack(  
                # Enlace de Inicio
                rx.link(  
                    "Inicio", 
                    href="#header",
                    color=TextColor.WHITE.value, 
                    margin_x=Size.DEFAULT.value,
                    _hover={
                        "font_weight":"600"
                    }
                ),
                # Enlace de Sobre mí
                rx.link(  
                    "Sobre mí",  
                    href="#aboutme",  
                    color=TextColor.WHITE.value,  
                    margin_x=Size.DEFAULT.value,
                    _hover={
                        "font_weight":"600"
                    }
                ),
                # Enlace de Experiencia
                rx.link(  
                    "Experiencia",  
                    href="#experience",  
                    color=TextColor.WHITE.value,  
                    margin_x=Size.DEFAULT.value,
                    _hover={
                        "font_weight":"600"
                    }
                ),
                # Enlace de Skills
                rx.link(  
                    "Proyectos",  
                    href="#projects",  
                    color=TextColor.WHITE.value,  
                    margin_x=Size.DEFAULT.value,
                    _hover={
                        "font_weight":"600"
                    }  
                ),
                # Enlace de Proyectos
                rx.link(  
                    "Skills",  
                    href="#skills",  
                    color=TextColor.WHITE.value,  
                    margin_x=Size.DEFAULT.value,
                    _hover={
                        "font_weight":"600"
                    }  
                ),
                margin_left=["5em", "5em", "5em", "10em", "15em", "15em"],
                display=["none", "none", "none", "flex", "flex", "flex"]
            ),
        ),
        backdrop_filter="blur(40px)",
        position="fixed",
        padding_x=Size.BIG.value, 
        padding_y=Size.DEFAULT.value,  
        z_index="999", 
        top="0",  
        width="100%" 
    )
