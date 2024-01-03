import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(to_email, subject, body, attachment_path=None):
    # Set up your SMTP server details for Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = '#' #enter the sender email address 
    smtp_password = '#####' #enter the 16 digit access key for refrence visit the website mentioned in the read me 

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the resume if provided
    if attachment_path:
        attachment = open(attachment_path, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename="{attachment_path}"')
        msg.attach(part)
        attachment.close()

    # Add the body text
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and enable a secure connection
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Enable TLS
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_email, msg.as_string())

if __name__ == "__main__":
    # List of HR emails
    hr_emails = [
        # Add all other HR emails
    ]

    # Your resume file path
    resume_path = 'path to resume file.pdf '

    # Email content
    email_subject = 'Job Inquiry'
    email_body = """
    Dear Hiring Manager,

    I hope this email finds you well. I am writing to express my interest in potential job opportunities within your organization. Please find attached my resume for your consideration.

    Thank you for your time and consideration.

    Best regards,
    [Your Name]
    """

    # Send email to each HR
    for hr_email in hr_emails:
        send_email(hr_email, email_subject, email_body, attachment_path=resume_path)
        print(f"Job inquiry email sent to {hr_email}")


# https://support.cloudways.com/en/articles/5131076-how-to-configure-gmail-smtp