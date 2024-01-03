# Automated Job Inquiry Email Sender

## Overview
This Python script automates the job inquiry process by sending personalized emails to multiple HR contacts. It leverages Gmail's SMTP server for secure communication, allowing users to attach their resumes seamlessly.

## Features
- **Configurability:** Easily set up the script with Gmail SMTP server details, HR contacts, and resume file path.
- **Personalized Outreach:** Send tailored job inquiry emails to each HR contact for a more effective outreach.
- **Attachment Support:** Option to include a resume attachment with each email.

## Getting Started
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/EmailSender.git
    ```

2. **Install required Python libraries:**
    ```bash
    pip install secure-smtplib
    ```

3. **Update the script with your Gmail SMTP server details, HR contacts, and resume file path.**

4. **Run the script:**
    ```bash
    python script.py
    ```
## Configuration
Edit the script to configure:

- `smtp_username`: Your Gmail email address.
- `smtp_password`: Your Gmail app password.
- `hr_emails`: List of HR email contacts.
- `resume_path`: File path to your resume.

## Usage
Run the script to initiate automated job inquiry emails. The script will send personalized emails to each HR contact, enhancing your outreach efforts.

Feel free to customize the email content in the script according to your preferences.

## Note
Ensure your Gmail account allows less secure app access or generate an app password for secure authentication.
visit to learn more 
https://support.cloudways.com/en/articles/5131076-how-to-configure-gmail-smtp
