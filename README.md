# What is it?
A Django-based REST API for library management, using Python and PostgreSQL. Ideal for integrating or developing a library system with a scalable backend.

# Why I need to this project?
- If you develop the library project and you need a REST API. And you don't want to spend your time on the Back-end. This project is for you because it's easy to understand and useful.
- If your library application involves managing various models such as book checkouts, user information, and reviews, a REST API is an ideal solution for these functionalities. REST APIs effectively handle such data management, enhancing the scalability and flexibility of your application.

# What kind of end-points does this project contain?
1. **Contains user list and detail end-point.**
   - ....../api/users/
   - ....../api/users/<int:pk>
2. **Contains review list and detail end-point.**
   - ....../api/review/
   - ....../api/review/<int:pk>/
3. **Contains do review end-point.**
   - This end-point alowed only reviewer and admin person  editting and deleting
   - ....../api/review/<int:book_pk>/make_review/
4. **Contains book list and detail end-point.**
   - ....../api/books/
   - ....../api/books/<int:pk>
  
Whether you are a user or not, you have the authority to 'SAFE_METHODS' except for commenting.
For other methods, the user must log in and the user cannot change the comment if it is not his/her own comment.





# What is the api models ?
![diagram](https://github.com/user-attachments/assets/affbd1db-4a27-4445-b9ab-8644f877faae)


# How to install and run this repository?

1. **Download the repository** either via the interface or the terminal.

2. **Navigate to the project directory**.

  ![location](https://github.com/user-attachments/assets/0048bdd8-7d00-4c72-a6d2-df532ed181df)


3. **Create and activate your virtual environment**:

   - **For Windows:**

     ```bash
     python -m venv myenv
     myenv\Scripts\activate
     ```

   - **For macOS and Linux:**

     ```bash
     python3 -m venv myenv
     source myenv/bin/activate
     ```

4. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt

5. **Than we need to PostgreSQL Database**:
   - So you must download PostgreSQL and create Database.

7. **Perform migration operations**:

   - **For Windows:**

     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

   - **For macOS and Linux:**

     ```bash
     python3 manage.py makemigrations
     python3 manage.py migrate
     ```
8. **Run the project**:

   - **For Windows:**

     ```bash
     python manage.py runserver
     ```

   - **For macOS and Linux:**

     ```bash
     python3 manage.py runserver
     ```




