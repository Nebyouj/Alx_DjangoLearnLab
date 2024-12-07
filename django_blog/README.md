# Django Blog Authentication System

## Overview

This project implements a comprehensive user authentication system for the Django blog project. The system includes the following features:
- User Registration
- Login and Logout
- Profile Management
- Security Enhancements

The following sections provide detailed instructions for setting up, using, and testing the authentication system.

---

## Features

1. **User Registration**: Allows new users to create an account by providing a username, email, and password.
2. **User Login**: Enables registered users to log in to their accounts.
3. **User Logout**: Safely logs users out of the system.
4. **Profile Management**: Authenticated users can view and manage their profile details, including adding optional fields like a bio or profile picture.

---

## Setup Instructions

### 1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd django_blog
   ```

### 2. **Apply Migrations**
   Run the following commands to create database tables for authentication:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### 3. **Create a Superuser**
   For admin access, create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

### 4. **Run the Development Server**
   Start the local server:
   ```bash
   python manage.py runserver
   ```
   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in a browser.

---

## User Guide

### **User Registration**
- Navigate to `/register/` to create a new account.
- Fill in the required fields: `username`, `email`, and `password`.
- Upon successful registration, users will be redirected to the login page.

### **User Login**
- Navigate to `/login/` to access the login page.
- Enter your username and password to log in.

### **User Logout**
- Use the `Logout` button or navigate to `/logout/` to log out of your account.

### **Profile Management**
- Navigate to `/profile/` to view and edit your profile details.
- If extended with optional fields (e.g., bio, profile picture), these can also be updated.

---

## Testing Instructions

### **Manual Testing**
1. **User Registration**
   - Test account creation with valid and invalid data.
   - Ensure error messages display for incorrect input (e.g., mismatched passwords).

2. **Login**
   - Test logging in with valid credentials.
   - Verify error messages appear for invalid credentials.

3. **Logout**
   - Ensure users are logged out securely and redirected appropriately.

4. **Profile Management**
   - Test editing profile details as an authenticated user.
   - Verify that unauthenticated users cannot access the profile page.

### **Automated Testing**
Add tests to `blog/tests.py` to verify functionality programmatically:
```python
from django.test import TestCase
from django.contrib.auth.models import User

class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_login(self):
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'password'})
        self.assertEqual(response.status_code, 200)

    def test_profile_access(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
```

---

## Security Features

1. **Password Hashing**  
   Passwords are securely hashed using Django’s built-in PBKDF2 algorithm.

2. **CSRF Protection**  
   All forms include CSRF tokens to prevent cross-site request forgery.

3. **Access Control**  
   Profile management pages are restricted to authenticated users using the `@login_required` decorator.

---

## Directory Structure

```plaintext
django_blog/
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   ├── blog/
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   ├── profile.html
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── django_blog/
│   ├── settings.py
│   ├── urls.py
└── manage.py
```

---

## Future Improvements

1. **Email Verification**: Add email confirmation during registration.
2. **Password Reset**: Enable password reset functionality via email.
3. **Two-Factor Authentication (2FA)**: Enhance security for login.


## Blog Post Management (CRUD)

### Features
- **List All Posts**: View all blog posts with titles and brief snippets.
- **View Individual Post**: Read the full content of a post.
- **Create Post**: Authenticated users can create new posts.
- **Edit Post**: Authors can update their own posts.
- **Delete Post**: Authors can delete their own posts.

### URL Patterns
- `/`: View all posts.
- `/post/new/`: Create a new post.
- `/post/<id>/`: View details of a post.
- `/post/<id>/edit/`: Edit a post (author only).
- `/post/<id>/delete/`: Delete a post (author only).

### Access Control
- **Authenticated Users**: Can create posts.
- **Post Authors**: Can edit or delete their own posts.
- **Guests**: Can only view posts.

### Notes
- CSRF protection is enabled for all forms.
- Passwords are securely hashed using Django's default authentication system.


## Comment System

### Features
- **View Comments**: Users can view all comments under a blog post.
- **Add Comments**: Authenticated users can add comments to posts.
- **Edit Comments**: Authors can edit their own comments.
- **Delete Comments**: Authors can delete their own comments.

### URL Patterns
- `/post/<id>/comment/new/`: Add a new comment to a post.
- `/comment/<id>/edit/`: Edit a comment.
- `/comment/<id>/delete/`: Delete a comment.

### Permissions
- **Authenticated Users**: Can add, edit, or delete their own comments.
- **Guests**: Can view comments but cannot add, edit, or delete.

### Notes
- Comments are displayed in reverse chronological order.
- CSRF protection is enabled for all comment forms.
