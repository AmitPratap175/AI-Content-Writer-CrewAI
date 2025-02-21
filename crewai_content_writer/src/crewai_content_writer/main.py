#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crewai_content_writer.crew import CrewaiContentWriter
import gradio as gr

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

## Simple way to initialize history for the ChatInterface
chatbot = gr.Chatbot(height=500, scale=10,value = [[None, "Hi, what article do you want me to write?"]])

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def chat(message, history, return_buffer=True):
    inputs = {
        'topic': message,
        # 'current_year': str(datetime.now().year)
    }
    buffer = ''
    
    try:
        buffer = str(CrewaiContentWriter().crew().kickoff(inputs=inputs))
    except Exception as e:
        return f"An error occurred while running the crew: {e}"
    
    return buffer


def run():
    """
    Run the crew.
    """
    gr.ChatInterface(chat, chatbot=chatbot).queue().launch(debug=True, share=True, inline=False)



def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        CrewaiContentWriter().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CrewaiContentWriter().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        CrewaiContentWriter().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
