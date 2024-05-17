import reflex as rx  
from portafolio.styles.styles import Size, TextColor, Color  
import portafolio.constans as constants  
import portafolio.styles.styles as styles  


def about_me() -> rx.Component: 
    return rx.vstack(  
        # Contenedor horizontal para la imagen y el contenido
        rx.hstack(  
            rx.center(  
                rx.vstack( 
                    
                    # Cuadro para el encabezado
                    rx.box(  
                        rx.text("Conoce", color=styles.TextColor.WHITE),
                        rx.text.strong("Sobre mí", font_size=styles.Size.BIG.value, color=styles.TextColor.WHITE),  
                        rx.hstack(  
                            
                            # Tarjeta de experiencia
                            rx.flex(  
                                rx.box(  
                                    rx.box( 
                                        rx.image(  
                                            src="medal-regular-36.png",  
                                            alt="icono de medalla 36 pixeles", 
                                            width=styles.Size.BIG  
                                        ),
                                        # Experiencia
                                        rx.text("Experiencia", color=styles.TextColor.BLUE, font_weight="bold"),  
                                        rx.text("+3 años", color=styles.TextColor.WHITE), 
                                        rx.text("Desarrollador de software autónomo", color=styles.TextColor.WHITE),  
                                        width=styles.WIDTH_CARD,  
                                    ),
                                    bg=styles.Color.LIGHTBLUE,  
                                    box_shadow=styles.Color.BOXSHADOW, 
                                    text_align="start",
                                    transition=".3s",  
                                    padding="1em",
                                    border_radius="1em",
                                    _hover={  
                                        "bg":styles.Color.DARKBLUE,
                                    }
                                ),
                                
                                # Tarjeta de estudios
                                rx.box(  
                                    rx.image(  
                                        src="book-regular-36.png", 
                                        alt="Icono de libro regular",  
                                        width=styles.Size.BIG  
                                    ),
                                    rx.text("Estudios", color=styles.TextColor.BLUE, font_weight="bold"), 
                                    rx.text("Técnico en programación de software.", font_size=styles.Size.DEFAULT.value, color=styles.TextColor.WHITE), 
                                    rx.text(  
                                        "Tecnólogo en análisis y desarrollo de software(en proceso).",  
                                        font_size=styles.Size.DEFAULT.value,  
                                        color=styles.TextColor.WHITE 
                                    ),
                                    width="17em",  
                                    text_align="start",
                                    bg=styles.Color.LIGHTBLUE,  
                                    box_shadow=styles.Color.BOXSHADOW,  
                                    transition=".3s",  
                                    padding="1em",
                                    border_radius="1em",
                                    _hover={  
                                        "bg":styles.Color.DARKBLUE,
                                    }
                                ),
                                spacing="4", 
                                padding=styles.Size.DEFAULT.value,
                                flex_direction=["column","column","row","row","row"] ,
                                align_content="center"
                            ),
                            margin_top=styles.Size.BIG.value 
                        ),
                        text_align="center", 
                        align_content="center",
                        margin_bottom=styles.Size.NOTSOBIG.value,                ),
                    
                    # Texto de presentación
                    rx.box(
                        rx.text(  
                            "👨‍💻 Mi nombre completo es Johan Sebastian Valle Barbarán, soy una persona muy elocuente, con actitud y resiliente tambien soy Adventista del séptimo día lo cual me hace una persona espiritual y centrada en mis desiciones.",
                            width=["18em", "18em", "29em", "29em", "29em"],
                            color=styles.TextColor.WHITE,
                            margin_bottom=styles.Size.DEFAULT.value
                        ),
                        rx.text( 
                            "🔭 Actualmente hago parte del semillero de investigación Teinnova en el área de Informática y desarrollo de software del SENA en el Centro de Diseño e Innovación Tecnológica Industrial, en el cuál he trabajado en equipo lo cuál me ha enseñado a trabajar en equipo para llegar a soluciones efectivas.",
                            width=["18em", "18em", "29em", "29em", "29em"],  
                            color=styles.TextColor.WHITE  
                        ),
                        padding=styles.Size.DEFAULT.value
                    )
                ),
            ),
            #Foto de presentacion
            rx.image( 
                src="valle2.jpeg", 
                alt="Sebastian Valle con fondo natural", 
                width=styles.HEIGHT_IMAGE2,  
                height="auto", 
                border_radius=styles.BORDER_RADIUS,
                border="2px solid #606D80",
                box_shadow=styles.Color.BOXSHADOW, 
                margin_left=styles.Size.DEFAULT.value,
                display=["none", "none", "none","flex", "flex"]
            )
        ),
        id="aboutme", 
        padding_top=[styles.Size.BIG, styles.Size.BIG, styles.Size.VERYVERYBIG, styles.Size.VERYVERYBIG, styles.Size.VERYVERYBIG, ], 
        margin_bottom=styles.Size.VERYVERYBIG,  
    )
