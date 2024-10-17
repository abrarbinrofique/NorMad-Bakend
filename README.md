# NorMad- A travel share site.




Normad is a travel booking and sharing platform where users can book travel plans, share them with friends, and engage in group chats for trip discussions. Users also have personal profiles that include a profile picture and contact information.

## Features

- **Book Travel**: Users can book travel plans and review their experiences.
- **Share Travel**: Users can share their travel plans with friends.
- **Group Chat**: Engage in discussions and chat with fellow travelers in a group chat.
- **User Profile**: Every user has a profile with a profile picture and contact information.

## Technologies Used

- **Backend**: Django REST Framework
- **Frontend**: JavaScript
- **Database**: SQLite (for development), PostgreSQL (production-ready)
- **Cloud Storage**: Cloudinary for image uploads
- **Deployment**: Vercel

## Installation

1. Clone the repository:
    ```bash
   https://github.com/abrarbinrofique/NorMad-Bakend
    ```

2. Navigate to the project directory:
    ```bash
    cd NorMad-Frontend
    ```

3. Install the required Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

## Project Structure

- **chat/**: Handles group chat functionality.
- **contactus/**: For handling customer support and inquiries.
- **customer/**: Manages user profiles and customer data.
- **event/**: Manages event-based travel plans.
- **sharetravel/**: Handles sharing travel plans with friends.
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

## License

This project is licensed under the MIT License.
"""

# Saving the content to a file
with open("/mnt/data/README_Normad.md", "w") as file:
    file.write(readme_content)

"/mnt/data/README_Normad.md"
