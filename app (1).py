import gradio as gr

responses = {
    "hello": "Hey! Welcome to DecodeLabs Bot",
    "hi": "Hi there!",
    "how are you": "Running at 100%!",
    "what is ai": "AI simulates human intelligence!",
    "who made you": "A DecodeLabs Engineer Batch 2026!",
    "your name": "I am DecoBot!",
    "bye": "Goodbye!",
    "help": "Try: hello, how are you, what is ai",
}

def chatbot(message, history):
    clean = message.lower().strip()
    return responses.get(clean, "I do not understand!")

demo = gr.ChatInterface(
    fn=chatbot,
    title="DecoBot - DecodeLabs",
    description="Rule-Based AI Chatbot | Project 1 | Batch 2026",
    examples=["hello", "what is ai", "how are you"],
    theme=gr.themes.Soft()
)

demo.launch(share=True)
