import ollama
import reflex as rx
from llama3 import style
from rxconfig import config

class State(rx.State):
    
    content: str
    chat_history: list[dict[str,str]]

    def answer(self):

        self.chat_history.append({"role": "user", "content": self.content})
        chat_call = ollama.chat(model="llama3", messages=self.chat_log)
        response = chat_call["message"]["content"]
        self.chat_history.append({"role": "assistant", "content": response})



def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, text_align="left"),
            style=style.question_style,
        ),
        rx.box(
            rx.text(answer, text_align="left"),
            style=style.answer_style,
        ),
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Message Llama3",
            value=State.question,
            on_change=State.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Send",
            on_click=State.answer,
        ),
    )


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            chat(),
            action_bar(),
            align="center",
        )
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
