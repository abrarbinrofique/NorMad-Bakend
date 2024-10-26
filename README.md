# NorMad - A Travel Share Site

![cover](https://github.com/abrarbinrofique/NorMad-Bakend/blob/main/nor.png)

NorMad is a travel-sharing and booking platform where users can plan trips, share travel plans with friends, and join group chats with other travelers. Users also have personal profiles for easy connections and personalized trip experiences.

---

## Features

- **Sign Up & Login**: Users need to sign up and confirm their email to access the site. After logging in, users can view trip details and interact with other users.
- **Book Travel & Review**: Book travel events, rate your experience, and share reviews.
- **Share Travel Plans**: Share your travel plans with friends. If the shared group reaches a specified number of people, they join the main travel event.
- **Group Chat**: Booked users can participate in group chats for travel discussions and updates.
- **Friend Management**: Users can send, accept, or remove friend requests.
- **User Profile**: Each user has a customizable profile with options to upload a profile picture, set contact info, and make updates.
- **Admin Capabilities**: Admins and designated users can create new travel events, manage users, and assign admin rights.

## Technologies Used

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)
![Cloudinary](https://img.shields.io/badge/Cloudinary-3448C5?style=for-the-badge&logo=cloudinary&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

## Installation

1. Clone the repository:
    ```bash
    git clone git@github.com:abrarbinrofique/NorMad-Bakend.git
    ```

2. Navigate to the project directory:
    ```bash
    cd NorMad-Bakend
    ```

3. Install the required Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Account and Authentication
- **Signup**: `POST https://normad-bakend.vercel.app/account/registration/newuser/`
- **Login**: `POST https://normad-bakend.vercel.app/account/registration/login/`
- **Profile Details**: `GET https://normad-bakend.vercel.app/account/registration/${parseInt(userid)}/`
- **Upgrade Profile**: `POST https://normad-bakend.vercel.app/account/upgrade/?people=${parseInt(userid)}`
- **Add Profile Info (if missing)**: `POST https://normad-bakend.vercel.app/account/upgrade/${travelerid}/`

### Tours and Events
- **All Tours List**: `GET https://normad-bakend.vercel.app/event/list/`
- **Tour Event Details**: `GET https://normad-bakend.vercel.app/event/list/${k}/`
- **Book a Travel Event**: `POST https://normad-bakend.vercel.app/event/list/${k}/addpeople/`
- **Give a Review for a Travel Event**: `POST https://normad-bakend.vercel.app/event/review/?travelname=${k}`
- **Single Travel Reviews**: `GET https://normad-bakend.vercel.app/event/review/?travelname=${k}`

### Reviews
- **All Reviews List**: `GET https://normad-bakend.vercel.app/event/review/`

### Travel Sharing
- **Share the Event with Friends**: `POST https://normad-bakend.vercel.app/sharetravel/join/`
- **Join Friend's Shared Travel**: `POST https://normad-bakend.vercel.app/sharetravel/join/${k}/sharetravel_add/`
- **All Travels Shared by Friends**: `GET https://normad-bakend.vercel.app/sharetravel/join/`

### Friend Requests
- **Send a Friend Request**: `POST https://normad-bakend.vercel.app/account/friendrequest/${l}/send_request/`
- **Incoming Friend Requests**: `GET https://normad-bakend.vercel.app/account/friendrequest/?to_user=${k}`
- **Accept Friend Request**: `POST https://normad-bakend.vercel.app/account/friendrequest/${k}/accept_request/`
- **Delete Incoming Friend Request**: `DELETE https://normad-bakend.vercel.app/account/friendrequest/${k}/remove_request/`

### Travel Plan Messaging
- **All Messages of a Travel Plan**: `GET https://normad-bakend.vercel.app/event/travelplan/?plan=${k}`
- **Send Message to Travel Plan as Participant**: `POST https://normad-bakend.vercel.app/event/travelplan/${k}/sendmessage/`

### Customer Information
- **Get Single Customer Info**: `GET https://normad-bakend.vercel.app/event/list/?people=${l}`

---

## Project Structure

- **chat/**: Handles group chat functionality.
- **contactus/**: Manages customer support inquiries.
- **customer/**: Manages user profiles and customer data.
- **event/**: Manages event-based travel plans.
- **sharetravel/**: Handles travel-sharing with friends.
- **staticfiles/**: Contains static assets like CSS and JavaScript.
- **db.sqlite3**: Development database (SQLite).

## Requirements

Here are the main dependencies used in this project (as listed in `requirements.txt`):

- Django==5.1.1
- djangorestframework==3.15.2
- Cloudinary==1.41.0
- Whitenoise==6.7.0
- django-cors-headers==4.4.0
- psycopg2-binary==2.9.9
- beautifulsoup4==4.12.3
- and more...

## Live Demo

You can check out the live demo of the project [here](https://abrarbinrofique.github.io/NorMad-Frontend/).
