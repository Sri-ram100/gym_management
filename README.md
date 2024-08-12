# Gym Management System
Gym Management System - Built using the Django framework, this system provides a user-friendly interface for gym administrators, trainers and members.
A comprehensive solution for efficiently managing various aspects of a fitness facility. Built using the Django framework, this system provides a user-friendly interface for both gym administrators and members.

Visit the live demo: [Gym Management System](https://arunimads.pythonanywhere.com/)
- **Demo Source**
   - username : admin
   - password : admin

## Features

- **Member Management:** 
  - Add, view, and manage member records.
  - Track membership status, payments, and attendance.

- **Trainer Management:** 
  - Add, view, and manage trainer profiles.
  - Assign trainers to members and monitor their activities.

- **Plan Management:**
  - Create and manage various membership plans.
  - Associate users with specific plans to track payments and facilities offered.

- **Attendance Tracking:**
  - Track member attendance with check-in and check-out features.

- **Payment Management:**
  - Handle membership payments and view payment history.

- **Diet and Workout Plans:**
  - Allow trainers to create personalized workout and diet plans for members.
  - Members can view and follow their assigned plans.

- **Admin Dashboard:**
  - Overview of gym activities including member statistics, payments, and more.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/gym-management-system.git
   cd gym-management-system
2. **Create and activate a virtual environment:**
    ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
3. **Install the dependencies:**
    ```bash
   pip install -r requirements.txt
4. **Run database migrations:**
    ```bash
    python manage.py migrate
5. **Create a superuser (Admin):**
   ```bash
   python manage.py createsuperuser
6. **Start the development server:**
   ```bash
   python manage.py runserver
7. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`



## Technologies Used
- Backend: Django
- Database: SQLite (default, can be replaced with PostgreSQL, MySQL, etc.)
- Frontend: HTML, CSS, JavaScript
- Deployment: PythonAnywhere

## Acknowledgements
- Django Documentation
- PythonAnywhere for deployment support.


## Contact
For any inquiries or feedback, please contact [@Arunimads](https://www.github.com/Arunimads)
