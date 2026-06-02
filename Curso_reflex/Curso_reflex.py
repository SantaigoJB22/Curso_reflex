"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .pages.base import base_page
from .pages.datos import data_base

from rxconfig import config


class State(rx.State):
    """The app state."""








def index() -> rx.Component:
    # Welcome Page (Index)
    index_child = rx.container(
       
        rx.vstack(
            rx.heading(
                "bienvenido a Reflex!", 
                size="9"
            ),
            rx.text(
                "listo",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),

            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
        ),
    )

    return base_page(index_child)



app = rx.App()
app.add_page(index)
app.add_page(data_base,route="/database")
