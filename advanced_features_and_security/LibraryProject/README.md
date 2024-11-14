"# LibraryProject" 


## Permissions and Groups Configuration

This project uses custom permissions and groups to manage access:

### Permissions Defined
- `can_view`: Allows viewing of MyModel instances.
- `can_create`: Allows creation of new MyModel instances.
- `can_edit`: Allows editing of MyModel instances.
- `can_delete`: Allows deletion of MyModel instances.

### Groups and Permissions
- **Editors**: Has `can_edit` and `can_create`.
- **Viewers**: Has `can_view` only.
- **Admins**: Has all permissions (`can_view`, `can_create`, `can_edit`, and `can_delete`).

### Usage in Views
Each view checks the user’s permissions before allowing access. Unauthorized users will see an error or be redirected.

