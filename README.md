# Introduction

This project was developed during Alura's "Django: Creating applications using Python" course.

![](./__screenshots/project_screenshot.png)

# Course goals

During the course and the development of the application, the following topics were covered:

- How Django works and how use it;
- Protect sensitive data using environment variables;
- Use templates and render pages in Django;
- Create models and relations between them;
- Configure and use Django Admin;
- Manage static and media files in Django;
- Create forms using Django's tools;
- Create form data validations;
- Create dynamic alert messages;
- Use partials to minimize code repetitions;
- Refactor and organize a project;
- Configure AWS S3 and use it to persist data.

# Running the project

### 1. clone the repository from Github.

To clone using `ssh`, you can use the following command:

```sh
$ git clone git@github.com:PedroLRA/alura_space.git
```

Or, if you prefer to use `HTTPS`:

```sh
$ git clone https://github.com/PedroLRA/alura_space.git
```    

### 2. Change to the new directory where the project was cloned:

```sh
$ cd alura_space
```

### 3. Install project dependencies:

```sh
$ pip install -r requirements/local.txt
```

### 4. Configure the `.env` file.

In this step, you will need to change the values `<YOUR_SECRET_KEY>`, `<YOUR_AWS_ACCESS_KEY_ID>`, `<YOUR_AWS_SECRET_ACCESS_KEY>`, `<YOUR_AWS_STORAGE_BUCKET_NAME>` to yours and remove the `.example` from the file name.

To obtain a django secret key, you can run the following code using python:
```py
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
```

To get the AWS configuration varibales you will need to create a new S3 bucket. here are some guides that might be helpful:

- [How to configure a Django App with S3 buckets | Blog DevGenius](https://blog.devgenius.io/how-to-configure-a-django-application-with-s3-buckets-for-file-storage-9cea315316a4)

- [File storage with AWS S3 Buckets Upload — for the Django project | Medium](https://medium.com/@hrushi669/file-storage-with-aws-s3-buckets-upload-for-the-django-project-50ea7208c4b1)

### 4. Then simply apply the migrations:

```sh
$ python manage.py migrate
```    

### 5. Collect the static files:

```sh
$ python manage.py collectstatic
```

This step might be a bit slow because the static files will be uploaded to the AWS bucket.

### 6. Finally, run the development server:

```sh
$ python manage.py runserver
```

Now the project is already running in your localhost and you can access the app in the following address: http://localhost:8000/.

---
---

<div style="text-align: right;">
  This project was developed for learning purposes.
  
  If you have any tips to improve the code, feel free to submit them as issues. I would ❤️ to see it.
</div>
