import sys
from google import genai
import atexit
model_name = "gemini-3.1-flash-lite"

client = genai.Client(api_key="AIzaSyAicF2UHgr26HjK1XFxV6yp7xs698p2Di0")
chat = client.chats.create(
        model= model_name
)
def bye():
    print("\nProgram closing\n")

atexit.register(bye)

msg = ""
flag = False
while True:
    lines = []
    print("Paste your error. Type END when finished:")
    while True:
        line = input()
        if line == "END":
            break
        elif line == "exit":
            sys.exit() 
        lines.append(line)
    msg = "\n".join(lines)
    msg = msg.strip()
    if len(msg) == 0:
        continue
    elif len(msg) > 100:
        print("Error is too long, sorry\n")
    elif len(msg) < 5:
        print("Error is too short\n")
    else:
        prompt = ""
        if not flag:
            prompt = " You are a Python debugging assistant. Explain this error simply: "
            flag = True
        prompt += msg
        response = chat.send_message(prompt)
        print(response.text, "\n")