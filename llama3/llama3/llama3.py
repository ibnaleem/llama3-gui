"""Welcome to Reflex!."""

from llama3 import styles

# Import all the pages.
from llama3.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.compile()
