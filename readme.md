<h1 align="center">
    <img src='./screenshots/py-gh.svg'/>
</h1>

<p align="center">
    <br>
    <a href="https://github.com/gh0stfrk/djangoblogs/actions">
        <img src="https://github.com/gh0stfrk/djangoblogs/workflows/Django%20CI/badge.svg" alt="Build Status" />
    </a>
    <a href="https://opensource.org/licenses/BSD-3-Clause">
        <img src="https://img.shields.io/badge/license-BSD-blue.svg" alt="License" />
    </a>
    <a href="https://twitter.com/gh0stfrk">
        <img src="https://img.shields.io/twitter/follow/gh0stfrk?style=social&logo=twitter" alt="follow on Twitter">
    </a>
</p>

Welcome to PyBlog, a feature-rich blogging platform built with Django. PyBlog offers a comprehensive suite of features to create, manage, and share blog posts effortlessly.

### Features
- **Create Blogs**: Easily create and publish blog posts with an intuitive editor.
- **Share Blogs via Email**: Share your blog posts with friends and followers via email.
- **Integrated Comments**: Engage with your readers through integrated comments on posts.
- **Admin Interface**: Manage your blog content efficiently with a robust admin interface.
- **Search Functionality**: Quickly find posts using the powerful search feature.
- **Tag Filtering**: Filter posts by tags to find content relevant to your interests.
- **Markdown Support**: Write posts in Markdown for easy formatting (limited support).


### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/gh0stfrk/pyBlog.git
   cd pyblog
   ```
2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3. **Configure the database**
    
    Update the `.env` file with the database and email server configuration.
    ```bash
    python3 manage.py migrate
    ```
4. **Create a superuser**
    ```bash
    python3 manage.py createsuperuser
    ```
5. **Run the development server**
    ```bash
    python3 manage.py runserver
    ```

### License 
PyBlog is released under the MIT License. See `LICENSE` for more information.

