import streamlit as st
import json
from pipeline import plan_pipeline

# Set up the Streamlit page
st.set_page_config(page_title="Function Call Planner", layout="wide")
st.title("🤖 Natural Language to Function Call Planner")
st.markdown("Enter a natural language query, and the AI will generate a structured plan of function calls to fulfill your request.")

# --- User Input ---
user_query = st.text_area("Enter your query here:", height=100, placeholder="e.g., Summarize the invoices for May and email the report to manager@example.com")

# --- Plan Generation ---
if st.button("Generate Plan", use_container_width=True):
    if not user_query:
        st.warning("Please enter a query before generating a plan.")
    else:
        with st.spinner("🧠 Thinking... Contacting Ollama to generate the plan..."):
            try:
                # Call the planning pipeline
                plan = plan_pipeline(user_query)
                
                # Display the results
                st.success("Successfully generated the plan!")
                st.json(plan)
                
            except ConnectionError as e:
                st.error(f"🔌 Connection Error: {e}")
                st.info("Please make sure the Ollama server is running. You can start it by running 'ollama serve' in your terminal.")
            except ValueError as e:
                st.error(f"📄 JSON Parsing Error: {e}")
                st.info("The model's response could not be parsed into a valid plan. This can sometimes be fixed by rephrasing the query or trying again.")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

# --- Footer ---
st.markdown("---")
st.markdown("Powered by [Ollama](https://ollama.com/) and [Streamlit](https://streamlit.io/).") 