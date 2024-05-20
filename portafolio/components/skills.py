import reflex as rx
from portafolio.styles.styles import Size, TextColor, Color
import portafolio.constans as constanst
import portafolio.styles.styles as styles

def skills() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.vstack(
                rx.box(
                    rx.text("Explora mís", color=styles.TextColor.WHITE.value),
                    rx.text.strong(
                        "Skills",
                        font_size=styles.Size.BIG.value,
                        color=styles.TextColor.WHITE.value
                    ),
                    text_align="center",
                    width="100%",
                    margin_y=styles.Size.VERYBIG.value
                ),
                # Skills / Front / Back
                rx.hstack(
                    rx.box(
                        rx.box(
                            #Front
                            rx.box(
                                rx.text.strong("Frontend", font_size=styles.Size.MEDIUM, color=styles.TextColor.WHITE.value),
                                width="100%",
                                text_align="center",
                                margin_bottom=styles.Size.DEFAULT.value
                            ),
                            rx.hstack(
                                rx.vstack(
                                    rx.image(
                                        src="html5.svg",
                                        alt="logo de html5",
                                        width=[styles.Size.BIG.value, styles.Size.BIG.value,styles.Size.BIG.value, styles.Size.VERYBIG.value, styles.Size.VERYBIG.value],
                                        height=[styles.Size.BIG.value, styles.Size.BIG.value,styles.Size.BIG.value, styles.Size.VERYBIG.value, styles.Size.VERYBIG.value],
                                    ),
                                    rx.text("HTML5"),
                                    margin=styles.Size.SMALL,
                                    align_items="center",
                                    transition=".1s",
                                    _hover={
                                        "transform":"scale(1.1)"
                                    }
                                ),
                                rx.vstack(
                                    rx.image(
                                        src="css.svg",
                                        alt="logo de css",
                                        width=[styles.Size.BIG.value, styles.Size.BIG.value,styles.Size.BIG.value, styles.Size.VERYBIG.value, styles.Size.VERYBIG.value], 
                                        height=[styles.Size.BIG.value, styles.Size.BIG.value,styles.Size.BIG.value, styles.Size.VERYBIG.value, styles.Size.VERYBIG.value],
                                    ),
                                    rx.text("CSS3"),
                                    margin=styles.Size.SMALL,
                                    align_items="center",
                                    transition=".3s",
                                    _hover={
                                        "transform":"scale(1.1)"
                                    }
                                ),
                                rx.vstack(
                                    rx.image(
                                        src="javascript.svg", 
                                        alt="logo de javascript",
                                        width=[styles.Size.BIG.value, styles.Size.BIG.value,styles.Size.BIG.value, styles.Size.VERYBIG.value, styles.Size.VERYBIG.value],
                                        height=[styles.Size.BIG.value, styles.Size.BIG.value,styles.Size.BIG.value, styles.Size.VERYBIG.value, styles.Size.VERYBIG.value],
                                    ),
                                    rx.text("JavaScript"),
                                    margin=styles.Size.SMALL,
                                    align_items="center",
                                    transition=".3s",
                                    _hover={
                                        "transform":"scale(1.1)"
                                    }
                                ),
                                rx.vstack(
                                    rx.image(
                                        src="figma.svg",
                                        alt="logo de figma",
                                        width=[styles.Size.BIG.value, styles.Size.BIG.value,styles.Size.BIG.value, styles.Size.VERYBIG.value, styles.Size.VERYBIG.value],
                                        height=[styles.Size.BIG.value, styles.Size.BIG.value,styles.Size.BIG.value, styles.Size.VERYBIG.value, styles.Size.VERYBIG.value],
                                    ),
                                    rx.text("Figma"),
                                    margin=styles.Size.SMALL,
                                    align_items="center",
                                    transition=".3s",
                                    _hover={
                                        "transform":"scale(1.1)"
                                    }
                                ),
                                padding=[".2em", ".2em", ".5em", "1em", "1em"],
                                border_radius="1em"
                            ),
                        padding=styles.Size.DEFAULT.value,
                        margin_bottom=styles.Size.BIG.value,
                        color=styles.Color.WHITE,
                        bg=styles.Color.GREY,
                        border_radius="15px",
                        border="1px solid #fff",
                        flex_direction=["column", "column", "row", "row", "row"]
                        ),
                        rx.box(
                            #Backend
                            rx.box(
                                
                                rx.text.strong("Backend", font_size=styles.Size.MEDIUM, color=styles.TextColor.WHITE.value),
                                    width="100%",
                                    text_align="center",
                                    margin_bottom=styles.Size.DEFAULT.value,
                                    
                            ),
                            rx.hstack(
                                rx.vstack(
                                    rx.image(
                                        src="python.svg",
                                        alt="logo de python",
                                        width=[styles.Size.BIG.value, styles.Size.BIG.value,styles.Size.BIG.value, styles.Size.VERYBIG.value, styles.Size.VERYBIG.value],
                                        height=[styles.Size.BIG.value, styles.Size.BIG.value,styles.Size.BIG.value, styles.Size.VERYBIG.value, styles.Size.VERYBIG.value],
                                    ),
                                    rx.text("Python"),
                                    align_items="center",
                                    margin=styles.Size.SMALL,
                                    transition=".3s",
                                    _hover={
                                        "transform":"scale(1.1)"
                                    }
                                ),
                                rx.vstack(
                                    rx.image(
                                        src="mysql.svg", 
                                        alt="logo de mysql",
                                        width=[styles.Size.BIG.value, styles.Size.BIG.value,styles.Size.BIG.value, styles.Size.VERYBIG.value, styles.Size.VERYBIG.value],
                                        height=[styles.Size.BIG.value, styles.Size.BIG.value,styles.Size.BIG.value, styles.Size.VERYBIG.value, styles.Size.VERYBIG.value],
                                    ),
                                    rx.text("MySQL"),
                                    align_items="center",
                                    margin=styles.Size.SMALL,
                                    transition=".3s",
                                    _hover={
                                        "transform":"scale(1.1)"
                                    }
                                ),
                                rx.vstack(
                                    rx.image(
                                        src="django.svg",
                                        alt="logo de django",
                                        width=[styles.Size.BIG.value, styles.Size.BIG.value,styles.Size.BIG.value, styles.Size.VERYBIG.value, styles.Size.VERYBIG.value],
                                        height=[styles.Size.BIG.value, styles.Size.BIG.value,styles.Size.BIG.value, styles.Size.VERYBIG.value, styles.Size.VERYBIG.value],
                                    ),
                                    rx.text("Django"),
                                    align_items="center",
                                    margin=styles.Size.SMALL,
                                    transition=".3s",
                                    _hover={
                                        "transform":"scale(1.1)"
                                    }
                                ),
                                rx.vstack(
                                    rx.image(
                                        src="php.svg", 
                                        alt="logo de php",
                                        width=[styles.Size.BIG.value, styles.Size.BIG.value,styles.Size.BIG.value, styles.Size.VERYBIG.value, styles.Size.VERYBIG.value],
                                        height=[styles.Size.BIG.value, styles.Size.BIG.value,styles.Size.BIG.value, styles.Size.VERYBIG.value, styles.Size.VERYBIG.value],
                                    ),
                                    rx.text("PHP"),
                                    align_items="center",
                                    margin=styles.Size.SMALL,
                                    transition=".1s",
                                    _hover={
                                        "transform":"scale(1.1)"
                                    }
                                ),
                                border_radius="1em",
                                padding="1em"
                            ),
                        padding=styles.Size.SMALL.value,
                        color=styles.TextColor.WHITE,
                        bg=styles.Color.GREY,
                        border_radius="15px",
                        border="1px solid #fff",
                        flex_direction=["column", "column", "row", "row", "row"]
                        ),
                        spacing="4",
                    ),
                    flex_direction=["column", "column", "row", "row", "row"]
                ),
            )
        ),
        margin_bottom=styles.Size.VERYVERYBIG,
        id="skills"
    )