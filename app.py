import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from flask import Flask, request, redirect, url_for, render_template
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__, static_folder='static', template_folder='templates')

# Email configuration
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Welcome page
@app.route("/")
def welcome():
    return render_template("welcome.html")

# Main page (index)
@app.route('/home')
def index():
    return render_template('index.html')

# Menu pages
@app.route('/about')
def about():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/peru')
def peru():
    return render_template('Peru.html')

@app.route('/peru-gourmet')
def peru_gourmet():
    return render_template('peruGourmet.html')

@app.route('/tour')
def tour():
    return render_template('tour.html')

# Dynamic routes
@app.route('/peruroutes/<page>')
def peruroutes(page):
    return render_template(f'peruroutes/{page}')

@app.route('/perugourmet/<page>')
def perugourmet(page):
    return render_template(f'perugourmet/{page}')

@app.route('/tourperu/<page>')
def tourperu(page):
    return render_template(f'tourperu/{page}')

@app.route('/routespecific/<page>')
def routespecific(page):
    return render_template(f'routespecific/{page}')

# Contact form handling
@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form.get('name')
    lastname = request.form.get('lastname')
    email = request.form.get('email')
    date = request.form.get('date')
    phone = request.form.get('phone')
    address = request.form.get('address')
    message_content = request.form.get('message')

    # Validate required fields
    if not name or not email:
        return redirect(url_for('error'))  # Handle validation error

    recipient = "tourperutravellers@gmail.com"
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = recipient
    message['Subject'] = f"Nuevo mensaje de {name} {lastname}"

    body = f"""
    Nombre: {name} {lastname}
    Correo Electrónico: {email}
    Fecha de viaje: {date}
    Teléfono Móvil: {phone}
    Dirección: {address}
    Mensaje: {message_content}
    """
    message.attach(MIMEText(body, 'plain'))

    # Handle multiple file attachments
    files = request.files.getlist("file")  # Obtener lista de archivos
    for file in files:
        if file and file.filename:  # Asegurarse de que hay un archivo seleccionado
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={file.filename}')
            message.attach(part)

    try:
        # Connect to the SMTP server
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        smtp_server.sendmail(SENDER_EMAIL, recipient, message.as_string())
        smtp_server.quit()
        return redirect(url_for('success'))
    except Exception as e:
        print("Error al enviar el correo:", e)
        return redirect(url_for('error'))

# Success and error pages
@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
