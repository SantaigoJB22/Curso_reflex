import reflex as rx


def social_link(label: str, href: str) -> rx.Component:
    return rx.link(rx.text(label, weight="bold"), href=href)


def socials() -> rx.Component:
    return rx.flex(
        social_link("IG", "/#"),
        social_link("XXX", "/#"),
        social_link("f", "/#"),
        social_link("in", "/#"),
        spacing="3",
        justify_content=["center", "center", "end"],
        width="100%",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            
            rx.divider(),
            rx.flex(
                rx.hstack(
                    rx.image(
                        src="https://web.reflex-assets.dev/other/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.text(
                        "© 2024 Reflex, Inc",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                    ),
                    spacing="2",
                    align="center",
                    justify_content=["center", "center", "start"],
                    width="100%",
                ),
                socials(),
                spacing="4",
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            spacing="5",
            width="100%",
        ),
        width="100%",
    )