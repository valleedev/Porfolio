import reflex as rx
import json
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
            bg=styles.Color.BGCOLOR.value,
        ),
        footer(),
        scroll_behavior="smooth"
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

title = "Sebastian Valle / Portfolio"
description = "Hola mi nombre es Sebastian Valle desarrollador de software, tambien hago parte de la iglesia Adventista del Séptimo Dia."
canonical_url = "https://sebasvalle.vercel.app/"

schema_markup = {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Sebastian Valle",
    "jobTitle": "Desarrollador de Software",
    "url": canonical_url,
    "sameAs": [
        "https://www.linkedin.com/in/sebasvalle/",
        "https://github.com/ValleDeve"
    ],
    "description": description,
    "alumniOf": {
        "@type": "Organization",
        "name": "Centro de Diseño e Innovación Tecnológica Industrial"
    },
    "memberOf": {
        "@type": "Organization",
        "name": "Iglesia Adventista del Séptimo Dia"
    }
}

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
        {"rel": "canonical", "href": canonical_url},
        {"type": "application/ld+json", "content": json.dumps(schema_markup)},
        # Agregar el código de Google Analytics
        {"src": "https://www.googletagmanager.com/gtag/js?id=G-T900HM6T4F", "async": "true"},
        {
            "content": """
                window.dataLayer = window.dataLayer || [];
                function gtag(){dataLayer.push(arguments);}
                gtag('js', new Date());
                gtag('config', 'G-T900HM6T4F');
            """
        },
    ]
)
