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
+ Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/saurabh78crypto/gas_utility_service.git
cd gas_utility_service
```

2. **Create a Virtual Environment**
+ It is recommended to use a virtual environment to manage dependencies. You can create and activate the   
  virtual environment with the following commands:

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
+ Install the required Python packages by running:
```bash
pip install -r requirements.txt
```

4. **Apply Migrations**
+ Before running the project, make sure the database is set up with the necessary migrations:
```bash
python manage.py migrate
```

5. **Create a Superuser**
+ To access the Django admin panel, you will need to create a superuser. Run the following command to create a superuser:
```bash
python manage.py createsuperuser
```
You will be prompted to enter a username, email, and password for the superuser.

6. **Create a Regular User**
+ Since there is no registration system, you can create a regular user using the Django shell. Run the following command in the rrot directory:
```bash
python manage.py shell
```
Then, inside the shell, use the following Python code to create a regular user:
```bash
from django.contrib.auth.models import User
user = User.objects.create_user('regularuser', 'user@example.com', 'password123')
```
This will create a regular user with the username `regularuser` and password `password123`.

7. **Run the Development Server**
+ Once the setup is complete, you can run the Django development server to start the application:
```bash
python manage.py runserver
```
The application will be available at `http://127.0.0.1:8000/`.

8. **Access the Admin Panel**
+ To access the Django admin panel, you simply login through the username and password entered during the 
  creation of the superuser.

9. **Login as Regular User**
+ To log in as a regular user, use the credentials you created in step 6 (`regularuser` and `password123`) through the login page.

