Project Overview
TourPeruTravellers is designed to streamline the process of exploring tours and routes in Peru. Users can browse different experiences, interact via a contact form (with file attachment support), and access media content. The application automates email responses, enhancing user engagement and support.

Features
Explore Travel Routes: Discover various travel experiences and routes in Peru.
Contact Form with Attachments: Users can send inquiries with file attachments.
Automated Email Responses: Automatically sends an email confirmation to inquiries.
Multimedia Content: Supports video content to enhance user engagement.

## Author

- **Benjamin F. Ontiveros Ordinola** - [Benja1512](https://github.com/Benja1512)
- **Contact Email**: bontiveros15@gmail.com


Requirements

Python 3.x

Libraries:

    Flask
    Flask-Mail
    python-dotenv
    Flask-Cors (optional)
    Flask-MySQL (optional for database functionality)

Install all required libraries with the following command:

    pip install -r requirements.txt

Installation
Clone the Repository:

    git clone https://github.com/Benja1512/tourperutravellers.git
    cd tourperutravellers

Install Dependencies:

    pip install -r requirements.txt
    Configure Environment Variables: Set up your email credentials in a .env file (see Configuration).

Configuration
    Create a .env file in the project root directory to store sensitive information like email credentials. Example content for .env:

    SENDER_EMAIL=your_email@gmail.com
    EMAIL_PASSWORD=your_password

These credentials are used to send automated emails from the application. Do not share this file publicly.

Usage

To start the application, run:

    python app.py
    The application will run locally on http://127.0.0.1:5000.

Key Pages

    Home (/home): Main landing page with introductory content.
    About Us (/about): Information about the project and team.
    Contact Form (/contact): Send inquiries with optional file attachments.
    Peru Routes (/peruroutes/<route>): Dynamic route pages to explore various travel options in Peru.

Using the Contact Form

    Navigate to the Contact page.
    Fill in your information, attach files if needed, and submit your inquiry.
    The application will send an automated response to confirm receipt.

Project Structure

tourperutravellers/
├── app.py               # Main Flask application file
├── requirements.txt     # Project dependencies
├── .env                 # Environment variables for sensitive info (email credentials)
├── templates/           # HTML templates for each page
│   ├── index.html
│   ├── contact.html
│   ├── success.html
│   └── error.html
├── static/              # Static assets (CSS, images, JS files)
│   ├── css/
│   └── images/
└── README.md            # Project documentation

