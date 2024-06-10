import subprocess
import webbrowser
import time

# Path to your Streamlit app file
app_path = 'Gemini_chatbots.py'

# URL that Streamlit will use
url = 'http://localhost:8501'

# Start Streamlit app
process = subprocess.Popen(['streamlit', 'run', app_path])

# Wait a few seconds for the server to start
time.sleep(5)

# Open the browser
webbrowser.open(url)

# Optional: wait for the process to complete (useful if running in a script)
process.communicate()
