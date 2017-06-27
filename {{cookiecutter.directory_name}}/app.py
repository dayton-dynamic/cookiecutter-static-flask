import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer


DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = ['.html', '.md']
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'
PROJECTS_DIR = 'projects'
FREEZER_DESTINATION = "{{cookiecutter.website_name}}"
FREEZER_DESTINATION_IGNORE = ['.git*', 'CNAME*'] # keep the repository files.

app = Flask(__name__)
app.config.from_object (__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)

#Homepage
@app.route('/')
def index():
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    projects = [project for project in flatpages if project.path.startswith(PROJECTS_DIR)]
    return render_template('index.html', posts=posts, projects=projects)

# posts
@app.route('/posts/')
def posts():
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    return render_template('posts.html', posts=posts)


#posts links
@app.route('/posts/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('page.html', post=post)


# projects
@app.route('/projects/')
def projects():
    projects= [project for project in flatpages if project.path.startswith(PROJECTS_DIR)]
    return render_template('projects.html', projects=projects)


# project directory. 
@app.route('/projects/<name>/')
def project(name):
    proj_path = '{}/{}'.format(PROJECTS_DIR, name)
    project = flatpages.get_or_404(proj_path)
    return render_template('page.html', project=project)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(debug=True)
