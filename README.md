# Natural Language to Function Call Planner

## Overview
This project takes a user's natural language query and generates a structured sequence of function calls (a "plan") using a locally-run, lightweight LLM. It does not execute the functions, only simulates the planning phase.

This implementation uses **Ollama** and the **phi3:mini** model to run efficiently on hardware with as little as 8GB of RAM.

## Structure
- `functions_library.py`: A library of ~50 utility function stubs with detailed docstrings.
- `prompt_builder.py`: Constructs the prompt that is sent to the LLM.
- `pipeline.py`: The core logic that gets a plan from Ollama.
- `main.py`: A command-line interface (CLI) to interact with the planner.
- `requirements.txt`: Python package dependencies.
- `README.md`: This file.

## Setup & Usage

### Step 1: Install Ollama
Download and install Ollama from the official website:
👉 **https://ollama.com/download**

### Step 2: Download the LLM
Open your terminal and pull the `phi3:mini` model:
```bash
ollama pull phi3:mini
```
This model is small, modern, and very capable for this task.

### Step 3: Install Python Dependencies
Clone the repository and install the required packages:
```bash
git clone <your-repo-url>
cd <your-repo-name>
pip install -r requirements.txt
```

### Step 4: Run the Ollama Server
For the Python code to communicate with the model, the Ollama server must be running. Open a **separate terminal** and run:
```bash
ollama serve
```
Keep this terminal window open.

### Step 5: Run the Application
You now have two ways to run the planner:

**Option A: Run the CLI (Command-Line Interface)**
In your original terminal, you can run the planner via the CLI.
```bash
python main.py "Your query here"
```

**Option B: Run the Streamlit Web Interface**
For a more interactive experience, run the Streamlit app:
```bash
streamlit run app.py
```
This will open a new tab in your web browser with the application.

## Extending the Planner
- **Add New Functions**: Simply add new function definitions with proper docstrings to `functions_library.py`. The pipeline will automatically detect and include them in the prompt for the LLM.
- **Change the Model**: You can use a different model (e.g., `mistral`) by changing the `model` parameter in the `ask_ollama` function call within `pipeline.py`. Remember to `ollama pull` the new model first.

## Adding Collaborators
- Make the GitHub repo private
- Add Kshitij, Ayush, and Shama as collaborators

## Notes
- The system only generates plans; it does not execute the functions.
- Ensure your system has enough RAM for the model. 