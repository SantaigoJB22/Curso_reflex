import reflex as rx
from .base import base_page


def data_base() -> rx.Component:
    # Welcome Page (Index)
    data_base_child = rx.container(
       
        rx.vstack(
            rx.heading(
                "Base de datos", 
                size="9"
            ),
            

            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
        ),
    )
    return base_page(data_base_child)
