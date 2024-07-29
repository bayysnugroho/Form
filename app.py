from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)

# Ganti dengan kredensial email Anda
EMAIL_ADDRESS = 'haulisyahran@gmail.com'
EMAIL_PASSWORD = 'fnfhotqzkajppshe'

# Fungsi untuk mengirim email
def send_email(subject, body, to_email):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email

    msg.attach(MIMEText(body, 'plain'))

    try:
        print("Trying to connect to the SMTP server...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            print("Logging in...")
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            print("Sending email...")
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Ambil data dari form
    data = request.form.to_dict()

    # Format data menjadi string
    body = "\n".join(f"{key}: {value}" for key, value in data.items())

    # Kirim email
    send_email('Form Submission', body, 'baysen@student.telkomuniversity.ac.id')

    return 'Selamat Anda Berhasil Mendaftar'

if __name__ == '__main__':
    # Pastikan secret key diatur untuk keamanan
    app.secret_key = os.urandom(24)
    app.run(debug=True)
