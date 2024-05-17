import reflex as rx 
import portafolio.styles.styles as styles 
from portafolio.views.navbar import navbar  
from portafolio.components.header import header  
from portafolio.components.about_me import about_me  
from portafolio.components.experience import experience  
from portafolio.components.skills import skills  
from portafolio.components.projects import projects  
from portafolio.views.footer import footer  

def index() -> rx.Component: 
    return rx.box(  
    
        navbar(),
        rx.center(  
            header(), 
            about_me(), 
            experience(),  
            skills(),  
            projects(), 
            flex_direction="column", 
            style={"overflow": "auto"}, 
            max_width=styles.MAX_WIDTH,  
            bg=styles.Color.BLUE.value,  
            scroll_behavior="smooth" 
        ),
        footer(),  
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,  
    style=styles.BASE_STYLE  
)

app.add_page(
    index,  
    title="Sebastian Valle / Portfolio", 
    description="Mi portafolio fusiona innovación, estética y funcionalidad, cautivando e inspirando con cada pieza. Deja una impresión duradera.",  
)
