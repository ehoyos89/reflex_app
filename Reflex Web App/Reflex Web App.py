"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
import requests

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass

def get_instance_metadata():
    try:
        metadata_url = "http://169.254.169.254/latest/meta-data/"
        instance_id = requests.get(metadata_url + "instance-id").text
        availability_zone = requests.get(metadata_url + "placement/availability-zone").text
        return instance_id, availability_zone
    except requests.exceptions.RequestException as e:
        return None, None


def index() -> rx.Component:
    instance_id, availability_zone = get_instance_metadata()
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading(availability_zone, font_size="2em"),
            rx.heading(instance_id, font_size="2em"),
            rx.box("Get started by editing ", rx.code(filename, font_size="1em")),
            rx.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
