import reflex as rx 
from portafolio.styles.styles import Size, TextColor, Color  
import portafolio.constans as constanst  
import portafolio.styles.styles as styles 
from portafolio.components.contact import contact  


def header() -> rx.Component: 
    return rx.vstack( 
    
        rx.center(  
            rx.flex(  
                # Contenido del encabezado
                rx.hstack( 
                    
                    # Imagen de perfil
                    rx.image( 
                        src="valle1.jpeg",  
                        alt="ValleDev en el nevado del ruiz", 
                        width=["15em", "15em", "25em", "25em", "25em",],  
                        heigth=["15em", "15em", "25em", "25em", "25em",],
                        border_radius="250px", 
                        border=f"2px solid {styles.Color.WHITE.value}",  
                        margin_right=["0", "0", Size.VERYBIG.value, Size.VERYBIG.value, Size.VERYBIG.value],  
                        box_shadow=styles.Color.BOXSHADOW 
                    ),
                    
                    # Información del encabezado
                    rx.center(
                        rx.vstack(
                            rx.text("Hola!👋 Soy", color=styles.TextColor.WHITE), 
                            rx.text.strong(  
                                rx.html("<h1>Sebastian Valle</h1>"),  
                                font_size=Size.BIG.value,  
                                color=styles.TextColor.WHITE  
                            ),
                            rx.text.strong( 
                                "Desarrollador de software",
                                color=TextColor.LIGHTBLUE, 
                            ),
                            
                            # Boton de descarga de CV 
                            rx.hstack(  
                                rx.link(  
                                    rx.button(  
                                        "Descargar CV", 
                                        bg=TextColor.LIGHTBLUE.value,  
                                        text_Color=TextColor.WHITE,  
                                        border_radius="15px",  
                                        cursor="pointer",  
                                        box_shadow=styles.Color.BOXSHADOW, 
                                        transition=".3s", 
                                        width="15em",
                                        heigth="12em",
                                        _hover={  
                                            "bg": styles.Color.WHITE.value,  
                                            "color": styles.Color.LIGHTBLUE.value, 
                                            "font_weight":"bold", 
                                        }
                                    ),
                                    href="CV_Sebastian_Valle.pdf",
                                    is_external=True  
                                ),
                            ),
                            
                            # Iconos de redes sociales
                            rx.hstack( 
                                rx.link( 
                                    rx.image( 
                                        src="icons8-instagram.svg",
                                        alt="logo de instagram"
                                    ),
                                    alt="icono de instagram", 
                                    href=constanst.INSTAGRAM_URL, 
                                    is_external=True, 
                                    border_radius=styles.Size.SMALL.value, 
                                    transition=".3s", 
                                    _hover={  
                                        "bg":styles.Color.LIGHTBLUE  
                                    }  
                                ),
                                rx.link(  
                                    rx.image(  
                                        src="icons8-github.svg",  
                                        alt="logo de github"
                                    ),
                                    alt="logo de github", 
                                    href=constanst.GITHUB_URL, 
                                    is_external=True, 
                                    border_radius=styles.Size.SMALL.value,  
                                    transition=".3s",  
                                    _hover={  
                                        "bg":styles.Color.LIGHTBLUE  
                                    }     
                                ),
                                rx.link(  
                                    rx.image(  
                                        src="linkedin.svg",  
                                        alt="logo de linkedin",
                                        width="30px"
                                    ),
                                    href=constanst.LINKEDIN, 
                                    is_external=True, 
                                    border_radius=styles.Size.SMALL.value,  
                                    transition=".3s",  
                                    _hover={  
                                        "bg":styles.Color.LIGHTBLUE  
                                    }
                                )
                            ),
                        align="center", 
                        justify_content=["center","center", "center", "center", "center", ],
                        align_items=["center", "center", "center", "center", "center", ]
                        ),
                        margin_y=[styles.Size.BIG.value, styles.Size.BIG.value, styles.Size.VERYBIG.value, styles.Size.VERYBIG.value, styles.Size.VERYBIG.value, styles.Size.VERYBIG.value], 
                    ),
                    width="100%",
                    align_content="center",
                    flex_direction=["column", "column", "row", "row", "row"],
                ),
                margin_top=styles.Size.VERYVERYBIG.value, 
                justify_content="center",
                width="100%",
            ),
        ),
        id="header",  # ID del encabezado
        margin_bottom=styles.Size.VERYVERYBIG,  # Margen inferior muy grande
    )
