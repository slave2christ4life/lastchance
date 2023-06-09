

# LastChance

LastChance is a web application built with Django that allows users to register and interact with listings.

## Features

- User registration and authentication
- Create, update, and delete listings
- View and search for listings
- User profiles

## Installation

1. Clone the repository:

   ```shell
   git clone <repository-url>
   ```

2. Create a virtual environment:

   ```shell
   python -m venv env
   ```

3. Activate the virtual environment:

   - For Windows:

     ```shell
     .\env\Scripts\activate
     ```

   - For macOS/Linux:

     ```shell
     source env/bin/activate
     ```

4. Install the dependencies:

   ```shell
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```shell
   python manage.py migrate
   ```

6. Create a superuser:

   ```shell
   python manage.py createsuperuser
   ```

7. Run the development server:

   ```shell
   python manage.py runserver
   ```

   The application will be accessible at http://localhost:8000/.

## Usage

- Access the admin interface:

  You can access the Django admin interface by visiting http://localhost:8000/admin/. Use the superuser credentials created during the installation process.

- Register a user:

  - Visit http://localhost:8000/users/register to register a new user.

- Create a listing:

  - After registering or logging in, you can create a new listing by visiting http://localhost:8000/listings/create/.

- View and search listings:

  - The homepage displays a list of all available listings. You can search for specific listings using the search bar.

- Update and delete listings:

  - If you are the owner of a listing, you can update or delete it by visiting the listing's detail page and selecting the appropriate options.

- User profiles:

  - Each user has a profile page that displays their information and the listings they have created. You can access your own profile by clicking on your username in the navigation bar.

## Configuration

The project's configuration can be found in the `LastChance/settings.py` file. You can modify various settings such as the database configuration, static files, and installed apps according to your needs.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make the necessary changes and commit them.
4. Push your branch to your forked repository.
5. Open a pull request with a detailed description of your changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The LastChance project was developed using Django, an open-source web framework for Python.
- Thanks to the Django community for their excellent documentation and support.

Feel free to update and customize the README file according to your project's specific requirements and additional information.
