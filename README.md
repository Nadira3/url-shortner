# URL Shortener

A simple web application that allows users to shorten their long and extensive URLs. This project aims to provide a quick and easy way to convert lengthy URLs into short, shareable links.

## Features

- **URL Shortening**: Easily shorten long URLs for easier sharing.
- **User-Friendly Interface**: A simple, clean, and intuitive UI for users to input and shorten their URLs.
- **Backend Logic**: Efficient URL shortening service powered by Django with a PostgreSQL database.
- **Fully Responsive**: Works on all screen sizes, ensuring accessibility for mobile and desktop users.
- **Hosted on Render**: Application is deployed on [Render](https://render.com/), providing easy access to the service.

## Technology Stack

### Frontend:
- **HTML**: Structure and layout of the web pages.
- **CSS**: Styling to make the web application look clean and modern.
- **JavaScript**: Client-side logic for interactivity and validation.

### Backend:
- **Django**: Python-based web framework for the server-side logic and URL shortening.
- **PostgreSQL**: Database used to store original and shortened URLs.

### Hosting:
- **Render**: Application is deployed and hosted on Render, ensuring reliable access and scalability.

## Installation & Setup

To run this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/url-shortener.git
   cd url-shortener
   ```

2. **Backend setup:**

   - Install the necessary Python packages:

     ```bash
     pip install -r requirements.txt
     ```

   - Set up your PostgreSQL database and configure the connection in `settings.py`.

   - Run migrations:

     ```bash
     python manage.py migrate
     ```

   - Start the Django server:

     ```bash
     python manage.py runserver
     ```

3. **Frontend setup:**
   
   - The frontend files (HTML, CSS, and JavaScript) are located in the `static/` folder and can be modified as needed.

4. **Access the application:**
   
   Open a browser and visit `http://127.0.0.1:8000/` to access the application locally.

## Usage

1. Enter a long URL in the input field.
2. Click on the "Shorten URL" button.
3. The shortened URL will be displayed, ready to copy and share.
