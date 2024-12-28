# Coupon Generator Project
This is a Django-based web application that allows users to generate and validate coupons. The project includes features for creating coupons, associating them with products, and ensuring they are validated based on the specific user.

## Live Application
If there is any problem with requirements or setup you can directly checkout the functinalities through Live Application deployed through Vercel using this repository.<br>
You can access the application here:  <br>
[https://bargenix-yuva-prakash-sai-gunupuru-backend.vercel.app/](https://bargenix-yuva-prakash-sai-gunupuru-backend.vercel.app/) <br>
The end points are for this live application are (Use Psotman API because CORS is not installed for this project): <br>
for products: https://bargenix-yuva-prakash-sai-gunupuru-backend.vercel.app/products/ <br>
for coupons: https://bargenix-yuva-prakash-sai-gunupuru-backend.vercel.app/coupons/ <br>
For coupons:
Get is used to fetch the check the existing Coupons and POST is used to create Coupon(Post format):
{
        "product": 1,
        "coupon_id": "Check-1",
        "discount": 1,
        "user_ids": "",
        "expiry_date": "2024-12-27 10:25:00"
}
user_ids can be empty such that all users have access and for only specific persons if required it should be added as string with coma(,) for example "user_ids": "1,2,3,4,5"
and expiry date as "yyyy-mm-dd hr:mins:secs"
edit or delete coupons: https://bargenix-yuva-prakash-sai-gunupuru-backend.vercel.app/coupons/9/
It can be 8 or 1 or 2 any coupon's id
For edit set PUT and format as follows:
{
    "id": 9,
    "product": 2,
    "coupon_id": "NewCoupon-90",
    "discount": "91.00",
    "user_ids": "",
    "expiry_date": "2024-12-27 10:25:00"
}
For delete put it to delete 
for coupon-validation: https://bargenix-yuva-prakash-sai-gunupuru-backend.vercel.app/apply-coupon/ <br>
Set it to post and format as follows:
{
    "product_id": 1,
    "coupon_id": "WELCOME_50",
    "user_id": 98765
}
for the successful entries and logs: https://bargenix-yuva-prakash-sai-gunupuru-backend.vercel.app/logs/ <br>
set it to GET and then entry it to get the log details.

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
7. Run the Server:
Start the development server:
```python manage.py runserver```

Visit http://127.0.0.1:8000/ in your browser to view the project. And the end are shown in it!<br>
<img width="930" alt="{7D5C6B0C-87A3-4A54-9042-327C94777AC2}" src="https://github.com/user-attachments/assets/fc3765fb-da72-49c4-83d1-70f5213d0101" />
<br>
The end points are: <br>
for products: host_name(like localhost/127.0.0.1:8000)/products/ <br>
for coupons: host_name(like localhost/127.0.0.1:8000)/coupons/ <br>
edit or delete coupons: host_name(like localhost/127.0.0.1:8000)/coupons/<int:pk>(like with actual id's i.e., 1/2<br>
for coupon-validation: host_name(like localhost/127.0.0.1:8000)/apply-coupon/ <br>
for the successful entries and logs: host_name(like localhost/127.0.0.1:8000)/logs/ <br>


## Live Application
If there is any problem with requirements or setup you can directly checkout the functinalities through Live Application deployed through Vercel using this repository.<br>
You can access the application here:  <br>
[https://bargenix-yuva-prakash-sai-gunupuru-backend.vercel.app/](https://bargenix-yuva-prakash-sai-gunupuru-backend.vercel.app/) <br>
The end points are for this live application are (Use Psotman API because CORS is not installed for this project): <br>
for products: https://bargenix-yuva-prakash-sai-gunupuru-backend.vercel.app/products/ <br>
for coupons: https://bargenix-yuva-prakash-sai-gunupuru-backend.vercel.app/coupons/ <br>
For coupons:
Get is used to fetch the check the existing Coupons and POST is used to create Coupon(Post format):
{
        "product": 1,
        "coupon_id": "Check-1",
        "discount": 1,
        "user_ids": "",
        "expiry_date": "2024-12-27 10:25:00"
}
user_ids can be empty such that all users have access and for only specific persons if required it should be added as string with coma(,) for example "user_ids": "1,2,3,4,5"
and expiry date as "yyyy-mm-dd hr:mins:secs"
edit or delete coupons: https://bargenix-yuva-prakash-sai-gunupuru-backend.vercel.app/coupons/9/
It can be 8 or 1 or 2 any coupon's id
For edit set PUT and format as follows:
{
    "id": 9,
    "product": 2,
    "coupon_id": "NewCoupon-90",
    "discount": "91.00",
    "user_ids": "",
    "expiry_date": "2024-12-27 10:25:00"
}
For delete put it to delete 
for coupon-validation: https://bargenix-yuva-prakash-sai-gunupuru-backend.vercel.app/apply-coupon/ <br>
Set it to post and format as follows:
{
    "product_id": 1,
    "coupon_id": "WELCOME_50",
    "user_id": 98765
}
for the successful entries and logs: https://bargenix-yuva-prakash-sai-gunupuru-backend.vercel.app/logs/ <br>
set it to GET and then entry it to get the log details.
# if any queries contact me: yuvaprakashsai@gmail.com or [LinkedIn](https://www.linkedin.com/in/yuvaprakashsai-gunupuru)
