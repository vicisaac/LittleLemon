Test Cases: API Path to Test

1. Register new user: 
POST  http://127.0.0.1:8000/auth/users/
Body (JSON)
{
    "username": "newuser3",
    "password": "newpassword123",
    "email": "newuser@example.com"
}


2. User Login: 
POST http://127.0.0.1:8000/auth/token/login/
{
    "username": "newuser3",
    "password": "newpassword123"
}

Use the generated token for other test authentication.

3. Create table booking 
POST  http://127.0.0.1:8000/restaurant/booking/tables/
{
    "name": "Sarah Isaac",
    "no_of_guests": 5,
    "booking_date": "2023-01-20T18:00:00Z"
}

4. Display all table booking:  
GET  http://127.0.0.1:8000/restaurant/booking/tables/

5. Dispay specific table booking:
    GET http://127.0.0.1:8000/restaurant/booking/tables/2

6. Display All menu items:
GET http://127.0.0.1:8000/restaurant/menu/

7. Display specific menu items:
GET http://127.0.0.1:8000/restaurant/menu/1

8. Update a menu item:
PUT http://127.0.0.1:8000/restaurant/menu/3/
{
    "title": "Sushi Deluxe",
    "price": 19.99,
    "inventory": 25
}

9. Delete a menu item: 
DELETE http://127.0.0.1:8000/restaurant/menu/5/
