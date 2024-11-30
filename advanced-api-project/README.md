# Advanced API Project: Book Views

## Overview
This project demonstrates how to configure CRUD operations for a `Book` model using Django REST Framework’s generic views.

## Endpoints
| Method | Endpoint               | Description                  | Permission        |
|--------|-------------------------|------------------------------|-------------------|
| GET    | `/books/`              | List all books               | Public            |
| GET    | `/books/<int:pk>/`     | Retrieve a book by ID        | Public            |
| POST   | `/books/create/`       | Add a new book               | Authenticated     |
| PUT    | `/books/<int:pk>/update/` | Update an existing book   | Authenticated     |
| DELETE | `/books/<int:pk>/delete/` | Delete a book             | Authenticated     |

## Custom Features
- **Validation**: Prevents future publication dates.
- **Permissions**: Authenticated users can perform write operations; unauthenticated users have read-only access.
- **Nested URLs**: Each view is mapped to a unique endpoint.

## Testing
Use tools like Postman to test each endpoint and ensure that permissions and validations work as expected.
