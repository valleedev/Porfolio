import reflex as rx  
from portafolio.styles.styles import Size, TextColor, Color  
import portafolio.constans as constanst  
import portafolio.styles.styles as styles  

def experience() -> rx.Component:  
    return rx.vstack(  
        
        rx.box(  
            rx.vstack( 
                rx.box(   
                    rx.text("Explora mí"),
                    rx.text.strong( 
                        "Experiencia",  
                        font_size=styles.Size.BIG.value, 
                    ),
                    text_align="center",
                    width="100%",
                    margin_y=styles.Size.BIG.value 
                ),
                rx.hstack(  
                    
                    # Primer trabajo como desarrollador freelance
                    rx.box(  
                        rx.text.strong("Desarrollador Autónomo", color=styles.Color.LIGHTBLUE.value),  
                        rx.text("2022 - actualidad", weight="bold"), 
                        rx.text( 
                            "Teniendo la oportunidad de colaborar con clientes y proyectos personales lo cual ha enriquecido mi experiencia y ampliando mi conjunto de habilidades. ",
                            width="15.5em" 
                        ),
                        padding=styles.Size.DEFAULT.value, 
                        border_right=["none", "none", "none", "2px solid #a1a1a1", "2px solid #a1a1a1"], 
                        width="100%",  
                        height="15.5em"
                    ),
                    
                    # Segundo trabajo como desarrollador backend
                    rx.box(  
                        rx.text.strong("Semillero de Investigación", color=styles.Color.LIGHTBLUE.value),  
                        rx.text("2024 - actualidad", weight="bold"), 
                        rx.text(  
                            "Actualmente soy aprendiz investigador en el semillero de software del Centro de diseño e innovación tecnológica industrial donde me estoy desempeñando como desarrollador backend .",  
                            width="15.5em" 
                            ),
                        padding=styles.Size.DEFAULT.value, 
                        border_right=["none", "none", "none", "2px solid #a1a1a1", "2px solid #a1a1a1"],  
                        heigth="16em", 
                    ),
                    
                    # Tercer trabajo como desarrollador FullStack
                    rx.box(  
                        rx.text.strong("Raptor Tecnologies", color=styles.Color.LIGHTBLUE.value), 
                        rx.text("2022 - 2023", weight="bold"),
                        rx.text( 
                            "Esta empresa fue creada como requisito de grado en el cuál desarrollamos un software de manejo de información de una constructora donde me desempeñe como Full Stack.", 
                            width="16em"
                        ),
                        padding=styles.Size.DEFAULT.value, 
                        heigth="20em"  
                    ),
                    flex_direction=["column", "column", "colummn", "row", "row"]
                ),
                color=styles.TextColor.WHITE 
            )
        ),
        margin_bottom=styles.Size.VERYVERYBIG, 
        id="experience"  
    )
