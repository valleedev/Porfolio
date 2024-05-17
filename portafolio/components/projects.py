import reflex as rx  
from portafolio.styles.styles import Size, TextColor, Color 
import portafolio.constans as constanst  
import portafolio.styles.styles as styles  



def projects() -> rx.Component: 
    return rx.vstack(  
        # Cuadro principal para los proyectos
        rx.box(  
            rx.text("Explora mís", color=styles.TextColor.WHITE.value),
            rx.text.strong( 
                "Proyectos", 
                font_size=styles.Size.BIG.value,
                color=styles.TextColor.WHITE.value 
            ),
            rx.text("más relevantes", color=styles.TextColor.GREY.value),  
            text_align="center", 
            width="100%",  
            margin_y=styles.Size.VERYBIG.value 
        ),
        rx.hstack(
            
            # Tarjeta para el proyecto JYASistem
            rx.box(  
                rx.image( 
                    src="jyasistem.png",  
                    alt="Imagen del sistema de información de JYA SAS", 
                    width="17em",
                    heigth="100%"
                ),
                rx.box(
                    rx.text.strong("JYASistem"), 
                    rx.text("Sitio de escritorio donde aprendí el manejo de CRUD con PHP ademas del trabajo en equipo ya que eramos 4 personas trabajando en el."), 
                    padding=styles.Size.DEFAULT
                ),
                rx.button(rx.text.strong("PHP"), bg=styles.Color.BLUE), 
                bg=styles.Color.LIGHTBLUE.value,  
                color=styles.TextColor.WHITE,  
                text_align="center", 
                width="17em",  
                height="22em",  
                margin_right=["0", "0", "0", styles.Size.VERYBIG, styles.Size.VERYBIG], 
                border_radius="1em",
                transition="all .5s",
                _hover={
                        "transform":"scale(1.1)"
                }
            ),
            
            # Enlace para el proyecto Angeles4x4
            rx.link(  
                rx.box(  # Tarjeta para el proyecto Angeles4x4
                    rx.image( 
                        src="angeles4x4.jpeg", 
                        alt="Imagen de la web de angeles 4x4",  
                        width="17em",  
                    ),
                    rx.box(
                        rx.text.strong("Angeles4x4"),  
                        rx.text("Página Web donde aprendi el manejo de usuarios y creación de publicaciones, además fue un reto porque fué la primera vez que realice responsive design."),
                        padding=styles.Size.DEFAULT
                    ),
                    rx.button(rx.text.strong("PHP"), bg=styles.Color.BLUE),  
                    bg=styles.Color.LIGHTBLUE.value, 
                    color=styles.TextColor.WHITE, 
                    text_align="center",
                    width="17em",  
                    height="22em", 
                    border_radius="1em",
                    transition="all .5s",
                    _hover={
                        "transform":"scale(1.1)"
                    }
                ),
                href="https://www.angeles4x4.com/", 
                is_external=True  
            ),
            flex_direction=["column", "column", "row", "row", "row"],
            
        ),
        margin_y=styles.Size.BIG, 
        id="projects",
        margin_bottom=styles.Size.BIG.value
    )
