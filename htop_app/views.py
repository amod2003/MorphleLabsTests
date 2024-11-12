from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import subprocess
import datetime
import pytz
import os

def htop_view(request):
    # Full name
    name = "Amod Kumar"
    
    # System username
    username = os.getenv("USER", "codespace")
    
    # Server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    
    # Execute `top` command
    top_output = subprocess.getoutput("top -b -n 1")
    
    # HTML output
    html_output = f"""
    <html>
    <head><title>System Information</title></head>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <h2>Top Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return HttpResponse(html_output)

