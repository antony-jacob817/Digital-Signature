import turtle
import random
from sympy import mod_inverse, isprime
from modular_exponentiation import modular_exponentiation
from euler_totient import euler_totient

public_key = private_key = None
message = signature = None

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_keys():
    global public_key, private_key
    p = int(turtle.textinput("Key Generation", "Enter a prime number (p):"))
    q = int(turtle.textinput("Key Generation", "Enter another prime number (q):"))
    if not (isprime(p) and isprime(q)):
        status_display("❌ Both numbers must be prime!", "red", 12)
        return
    n = p * q
    phi_n = euler_totient(n)
    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)
    d = mod_inverse(e, phi_n)
    public_key = (e, n)
    private_key = (d, n)
    status_display(f"✅ Keys Generated!\nPublic Key: {public_key}\nPrivate Key: (Hidden)", "green", 12)

def sign_message():
    global signature, message
    if not private_key:
        status_display("❌ Generate keys first!", "red", 12)
        return
    message = turtle.textinput("Sign Message", "Enter message to sign:")
    if not message:
        return
    d, n = private_key
    message_hash = hash(message) % n
    signature = modular_exponentiation(message_hash, d, n)
    status_display(f"✍️ Message Signed!\nSignature: {signature}", "yellow", 12)

def verify_signature():
    if not public_key or not signature or not message:
        status_display("❌ Missing data! Generate keys & sign a message first.", "red", 12)
        return
    received_message = turtle.textinput("Verify Signature", "Enter received message:")
    received_signature = int(turtle.textinput("Verify Signature", "Enter received signature:"))
    e, n = public_key
    message_hash = hash(received_message) % n
    decrypted_hash = modular_exponentiation(received_signature, e, n)
    if message_hash == decrypted_hash:
        status_display("✅ Signature VALID!", "green", 12)
    else:
        status_display("❌ Signature INVALID!", "red", 12)

def status_display(message, color, font_size):
    status.clear()
    status.color(color)
    status.goto(0, -170)
    status.write(message, align="center", font=("Arial", font_size, "bold"))

def create_button(text, x, y, action):
    button = turtle.Turtle()
    button.speed(0)
    button.shape("square")
    button.shapesize(stretch_wid=2, stretch_len=10)
    button.color("#2ECC71")
    button.penup()
    button.goto(x, y)
    button.onclick(lambda x, y: action())
    text_turtle = turtle.Turtle()
    text_turtle.hideturtle()
    text_turtle.penup()
    text_turtle.color("white")
    text_turtle.goto(x, y - 10)
    text_turtle.write(text, align="center", font=("Arial", 14, "bold"))

screen = turtle.Screen()
screen.title("🔐 Digital Signature System")
screen.bgcolor("#1A1A1A")
screen.setup(width=800, height=600)

header = turtle.Turtle()
header.hideturtle()
header.penup()
header.color("#3498DB")
header.goto(0, 220)
header.write("Digital Signature System", align="center", font=("Arial", 28, "bold"))

subtitle = turtle.Turtle()
subtitle.hideturtle()
subtitle.penup()
subtitle.color("#95A5A6")
subtitle.goto(0, 180)
subtitle.write("Secure • Fast • Reliable", align="center", font=("Arial", 14))

welcome = turtle.Turtle()
welcome.hideturtle()
welcome.penup()
welcome.color("white")
welcome.goto(0, 120)
welcome.write("🔐 Welcome! Click a button to start.", align="center", font=("Arial", 14, "bold"))

status = turtle.Turtle()
status.hideturtle()
status.penup()
status.color("white")
status.goto(0, -170)

create_button("Generate Keys", 0, 80, generate_keys)
create_button("Sign Message", 0, 0, sign_message)
create_button("Verify Signature", 0, -80, verify_signature)

footer = turtle.Turtle()
footer.hideturtle()
footer.penup()
footer.color("#95A5A6")
footer.goto(0, -250)
footer.write("© 2025 Digital Signature System v2.0", align="center", font=("Arial", 10))

turtle.done()
