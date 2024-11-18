# Gas Utility Company Web Application

This is a web application for managing customer service requests, supporting users, and providing admin functionalities for managing service requests.

## Features

- **Customer Service:** Allows customers to submit and track service requests.
- **Support:** Provides customers access to support resources.
- **Admin Panel:** Superusers can access the admin panel for managing service requests and other data.

## Technologies Used

- Django
- Bootstrap 5
- Python 3.x

## Setup Instructions

1. **Clone the Repository**
Clone this repository to your local machine using the following command:
```bash
git clone <repository-url>
```

2. **Create a Virtual Environment**
It is recommended to use a virtual environment to manage dependencies. You can create and activate the virtual environment with the following commands:
**For Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**For macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**
Install the required Python packages by running:
```bash
pip install -r requirements.txt
```

4. **Apply Migrations**
Before running the project, make sure the database is set up with the necessary migrations:
```bash
python manage.py migrate
```

5. **Create a Superuser**
To access the Django admin panel, you will need to create a superuser. Run the following command to create a superuser:
```bash
python manage.py createsuperuser
```
You will be prompted to enter a username, email, and password for the superuser.

6. **Run the Development Server**
Once the setup is complete, you can run the Django development server to start the application:
```bash
python manage.py runserver
```
The application will be available at `http://127.0.0.1:8000/`.

7. **Access the Admin Panel**
To access the Django admin panel, you simply login through the username and password entered during the creation of the superuser.


