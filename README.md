# Number Statistics Application using Django

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. It takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel.
Django is a full-featured web framework that follows the Model-View-Controller (MVC) architectural pattern. It provides a set of tools and libraries for building web applications, including an ORM, a templating engine, and a built-in admin interface.

In this project,
A Django web application that calculates various statistics operations such as Additions, Mean, Medium, Mode, Givivng number is prime, armest or not for a list of numbers.

## Setup

1. **Unzip the folder**
   ```bash
   unzip assignment.zip
   cd assignment
   ```
2.  **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Setup**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

To get started with Django, you’ll need to install it on your computer. You can do this by running the above command in your terminal.

4.  **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the server**
   ```bash
   python manage.py runserver
   ```
Now, Open your browser at [http://127.0.0.1:8000].

## Project Structure

```
assignment/
  manage.py
  assignment/        # Django project settings
  Statistics/        # Django app
    templates/
    static/
```
## How to usa

- In the homepage, enter numbers or upload a text file containing numbers, also make sure that all the number is seperated by comma, in the file also.
- Click **Submit** button to view the statistics result, including additions, mean, median, mode, range, prime numbers, and Armstrong numbers.
- The cart badge in the navigation bar shows the count of unique numbers entered so far in your current session.


## Notes

- Uses in‑memory sessions for simplicity.
- Use version of django is grater then Django 5.x and Python 3.10.
- I am using the macos M1 with apple 