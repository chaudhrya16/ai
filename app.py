import gradio as gr
import os


def respond(message, history):
    result = f"You said: {message}\nAnd I said that I am just learning AI"
    return result


gr.ChatInterface(
    fn=respond,
    title="My First Space",
    description="This is Anurag's first Space. I am learning AI and this is my first Space."
).launch(
    server_name="0.0.0.0",
    server_port=int(os.getenv("PORT", 9050))
)
