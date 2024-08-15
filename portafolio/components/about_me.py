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
                                        rx.text("Experiencia", color=styles.TextColor.LIGHTBLUE, font_weight="bold"),  
                                        rx.text("+3 años", color=styles.TextColor.WHITE), 
                                        rx.text("Desarrollador de software autónomo", color=styles.TextColor.WHITE),  
                                        width=styles.WIDTH_CARD,  
                                    ),
                                    bg=styles.Color.GREY,  
                                    box_shadow=styles.Color.BOXSHADOW, 
                                    text_align="start",
                                    transition=".3s",  
                                    padding="1em",
                                    border_radius="1em",
                                    border="1px solid #fff",
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
                                    rx.text("Estudios", color=styles.TextColor.LIGHTBLUE, font_weight="bold"), 
                                    rx.text("Técnico en programación de software.", font_size=styles.Size.DEFAULT.value, color=styles.TextColor.WHITE), 
                                    rx.text(  
                                        "Tecnólogo en análisis y desarrollo de software(en proceso).",  
                                        font_size=styles.Size.DEFAULT.value,  
                                        color=styles.TextColor.WHITE 
                                    ),
                                    width="17em",  
                                    text_align="start",
                                    bg=styles.Color.GREY,  
                                    box_shadow=styles.Color.BOXSHADOW,  
                                    transition=".3s",  
                                    padding="1em",
                                    border_radius="1em",
                                    border="1px solid #fff",
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
                            "👨‍💻 Mi nombre es Johan Sebastian Valle Barbarán. Desde que comencé en el mundo de la programación, he experimentado una amplia gama de emociones, desde la frustración hasta la satisfacción de resolver problemas complejos. A lo largo de mi trayectoria, he trabajado en varios proyectos en equipo, donde aprendí la importancia de la colaboración y la toma de decisiones conjuntas. Me considero una persona en constante aprendizaje, motivado por la disciplina y el deseo de superación.",
                            rx.link(  
                                    rx.button(  
                                        "Reconocimiento", 
                                        bg=TextColor.LIGHTBLUE.value,  
                                        text_Color=TextColor.WHITE,  
                                        border_radius="15px",  
                                        cursor="pointer",  
                                        box_shadow=styles.Color.BOXSHADOW, 
                                        transition=".3s", 
                                        width="12em",
                                        heigth="12em",
                                        margin_top=styles.Size.SMALL.value,
                                        margin_bottom=styles.Size.DEFAULT.value,
                                        _hover={  
                                            "bg": styles.Color.WHITE.value,  
                                            "color": styles.Color.LIGHTBLUE.value, 
                                            "font_weight":"bold", 
                                        }
                                    ),
                                    href="reconocimiento.jpeg",
                                    is_external=True  
                                ),
                            width=["18em", "18em", "29em", "29em", "29em"],
                            color=styles.TextColor.WHITE,
                            margin_bottom=styles.Size.DEFAULT.value
                        ),
                        rx.text( 
                            "🔭 Actualmente, estoy enfocado en fortalecer mis bases técnicas y desarrollar habilidades blandas a través de cursos especializados y proyectos personales. Disfruto compartiendo mis conocimientos con otros, lo que refuerza mi propio entendimiento y contribuye al crecimiento de la comunidad.",
                            width=["18em", "18em", "29em", "29em", "29em"],  
                            color=styles.TextColor.WHITE  
                        ),
                        padding=styles.Size.DEFAULT.value,
                        
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
                border="2px solid #fff",
                box_shadow=styles.Color.BOXSHADOW, 
                margin_left=styles.Size.DEFAULT.value,
                display=["none", "none", "none","flex", "flex"]
            )
        ),
        id="aboutme", 
        padding_top=[styles.Size.BIG, styles.Size.BIG, styles.Size.VERYVERYBIG, styles.Size.VERYVERYBIG, styles.Size.VERYVERYBIG, ], 
        margin_bottom=styles.Size.VERYVERYBIG,  
    )
