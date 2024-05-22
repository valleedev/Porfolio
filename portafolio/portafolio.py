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
            projects(), 
            skills(),  
            flex_direction="column", 
            style={"overflow": "auto"}, 
            bg=styles.Color.BLUE.value,  
            scroll_behavior="smooth" 
        ),
        footer(),  
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,  
    style=styles.BASE_STYLE  
)

title = "Sebastian Valle / Portfolio"
description = "Hola mi nombre es Sebastian Valle desarrollador de software, tambien hago parte de la iglesia Adventista del Séptimo Dia."

app.add_page(
    index,
    title=title,
    description=description,
    meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@valledev"},
    ]
)
