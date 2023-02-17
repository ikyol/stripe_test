
# Django API + Stripe
## Installation
Clone the project

```bash
$ git clone git@github.com:ikyol/stripe_test.git
$ cd stripe_test
```

Next, create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

Then, install the required packages:

```bash
(venv)$ pip install -r requirements.txt
```

Now you should make `env` file
```bash
(venv)$ touch .env
```
then, fill the fields in the `.env`
```txt
SECRET_KEY=
DEBUG=
ALLOWED_HOSTS=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
STRIPE_PUBLIC_KEY=
STRIPE_SECRET_KEY=

```

## Usage
To start the Django development server, run the following command:

```bash
(venv)$ python manage.py runserver
```

This will start the development server at http://localhost:8000/.

To create the database tables, run the following command:

```bash
(venv)$ python manage.py migrate
```

You can access the Django admin panel at http://localhost:8000/admin/. To create a superuser account, run the following command and follow the prompts:

```bash
(venv)$ python manage.py createsuperuser
```