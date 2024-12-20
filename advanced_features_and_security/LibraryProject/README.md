# Alx_DjangoLearnLab
## Tasks
make a git repo named ***Alx_DjangoLearnLab***.<br>using this git command
```
git init
```
then make a directory name ***Introduction_to_Django***.<br>
using this cli
```
mkdir Introduction_to_Django
```

Create a new Django project by running: 
```
django-admin startproject LibraryProject.
```
Run the Development Server:
<ul>
<li>Navigate into your project directory (cd LibraryProject).
<li>Create a README.md file inside the LibraryProject.
<li>Start the development server using: 
    ```
    python manage.py runserver.
    ```
<li>Open a web browser and go to http://127.0.0.1:8000/ to view the default Django welcome page.
</ul>


# Permissions and Groups Setup

In this application, access to posts is controlled through custom permissions and groups.

### Custom Permissions:
- `can_view`: Allows users to view posts.
- `can_create`: Allows users to create new posts.
- `can_edit`: Allows users to edit existing posts.
- `can_delete`: Allows users to delete posts.

### Groups:
- **Viewers**: Assigned only the `can_view` permission.
- **Editors**: Assigned `can_view` and `can_edit` permissions.
- **Admins**: Assigned all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`).

### Views Protection:
- Views such as `create_post`, `edit_post`, and `delete_post` are protected by the respective permissions using the `@permission_required` decorator.

