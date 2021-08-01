from sys import argv
from shutil import rmtree
from os import system

git_mode = False
if "git" in argv:
    git_mode = True
    print("Cloning in git mode...")

projects = open("projects").readlines()
print(projects)

for project in projects:
    project = project.strip("\n")
    try:
        rmtree(project)
    except FileNotFoundError:
        print("Old files not found... ignoring")
    if git_mode:
        project_uri = "git@github.com:bluemediaapp/%s.git" % project
    else:
        project_uri = "https://github.com/bluemediaapp/%s" % project
    system("git clone %s" % project_uri)

