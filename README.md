# Coupon Generator Project
This is a Django-based web application that allows users to generate and validate coupons. The project includes features for creating coupons, associating them with products, and ensuring they are validated based on the specific user.
# Requirements:
Python 3.8+ <br>
Django 4.0+ <br>
PostgreSQL <br>
# Setup Instructions:
1. Clone the Repository
First, clone the repository to your local machine:
```https://github.com/Yuvaprakash24/Bargenix_YuvaPrakashSaiGunupuru_Backend.git```
Then,
```cd Bargenix_YuvaPrakashSaiGunupuru_Backend```
2. Create a Virtual Environment
Create a virtual environment to manage the dependencies:
```python3 -m venv env```
Then, Activate the virtual environment:
```.\env\Scripts\activate```
4. Install Dependencies:
```pip install -r requirements.txt```
5. Set Up Database
A online PostgreSQL is setuped already you can check it in settings.py (No need to do anything)
Just change DEBUG = False to DEBUG = True in line number 26 in settings.py
7. Run the Server:
Start the development server:
```python manage.py runserver```

Visit http://127.0.0.1:8000/ in your browser to view the project. And the end are shown in it!
<img width="950" alt="{46C27B42-07AB-4DFD-841A-BC6282432FB1}" src="https://github.com/user-attachments/assets/bf77c202-892a-4db0-91cb-f3af7dfc58a8" />
<br>
The end points are: <br>
for products: http://127.0.0.1:8000/products/ <br>
for coupons: http://127.0.0.1:8000/coupons/ <br>
edit or delete coupons: http://127.0.0.1:8000/coupons/<int:pk>/ replace <int:pk> with actual id's i.e., 1/2<br>
for coupon-validation: http://127.0.0.1:8000/apply-coupon/ <br>
for the successful entries and logs: http://127.0.0.1:8000/logs/ <br>

# if any queries contact me: yuvaprakashsai@gmail.com
