# cookiecutter-static-flask
Cookiecutter template for static websites with flask

## How to use 

    pip install cookiecutter 
    cookiecutter gh:dayton-dynamic/cookiecutter-static-flask 
    
Edit the content in content/posts and/or content/projects.

Use `python app.py` to view the current contents without freezing.

## Deploying to Github Pages

see https://stevenloria.com/hosting-static-flask-sites-on-github-pages/

    python app.py freeze 
    git init
    git add . --all
    git commit -am "Initial commit"
    git checkout -b gh-pages
    git remote add origin https://github.com/username/flask-ghpages-example.git
    git push origin --all