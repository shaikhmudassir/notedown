from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from github import BadCredentialsException , Github
import requests, datetime

# Form for 'new.html' to write content for creating new file
class ContentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={"id":"TextArea1"}))

# Form for 'edit.html' to write content for updating a file
class UpdateForm(forms.Form):
    file_name = forms.CharField()
    content = forms.CharField(widget=forms.Textarea(attrs={"id":"TextArea1"}))

'''
*** Help ***
https://docs.github.com/en/developers/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps#web-application-flow
https://docs.github.com/en/developers/apps/managing-github-apps/installing-github-apps#authorizing-users-during-installation
https://pygithub.readthedocs.io/en/latest/
'''

def index(request):
    # Check token is available or not.If not then redirect to authentication page
    if "token" not in request.session:
        return HttpResponseRedirect("oauth")

    # If token is not set or token is get expired then redirect to '/oauth'
    try:
        g = Github(request.session["token"])
        user = g.get_user()
        username = user.login
    except (BadCredentialsException , KeyError):
        return HttpResponseRedirect("oauth")

    # If repository is not available (means repo is not created yet) then create new repository
    # Note: It will execute only one time while user install the app first time
    reponame = "notedown-" + username
    try:
        repo = g.get_repo(username + "/" + reponame)
    except:
        user.create_repo(reponame,private=True)
        repo = g.get_repo(username + "/" + reponame)
        with open('/static/gitdown/docs.md') as f:
            docs = f.read()
            repo.create_file("000docs.md", "Documentation is created", docs)

    request.session["user_repo_name"] = username + "/" + reponame

    # Get the files of a repository as a object (This is not just a content of a file it is complete object with all properties)
    files = repo.get_contents("")

    # Get the content of a file
    # Apply some Decoding and formating opration to get proper markdown content
    # Append dict in list, dict contain two things first-> path/filename second-> actal markdown content
    decoded_content , tags = [], set()
    for content_file in files:
        data = str(content_file.decoded_content.decode())

        # Find tags in markdown content and apply text formaring to get proper tags
        for i in data.split():
            if i.startswith('`@'):
                tags.add(i[2:-1])

        decoded_content.append({"name" :content_file.path, "data":g.render_markdown(data)})
        decoded_content.reverse()
    return render(request, "gitdown/index.html", {
        "content" : decoded_content,
        "tags":tags
    })


def oauth(request):
    # Redirect to github authentication
    return HttpResponseRedirect("https://github.com/login/oauth/authorize?client_id=Iv1.36ee32ab30bbb309")

def callback(request):
    # When user get authorize then he/she will be redirect to this route
    # After authorization application will make POST request to get access_token
    code = request.GET.get("code")
    url = 'https://github.com/login/oauth/access_token'
    param = {
        "client_id":"Iv1.36ee32ab30bbb309",
        "client_secret":"a949a96806ac6edd6a97d1e6dc00130fef6f13ac",
        "code":code
    }
    x = requests.post(url, data = param)

    # Extracting gho_*** token from POST request responce
    request.session["token"] = x.text.split("&")[0].split("=")[1]
    g = Github(request.session["token"])

    return HttpResponseRedirect("/")

def new(request):
    if "token" not in request.session:
        return HttpResponseRedirect("oauth")

    # If POST request then collect content from textarea to create new file
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]

            # If token is not set or token is get expired then redirect to '/oauth'
            try:
                g = Github(request.session["token"])
            except (BadCredentialsException , KeyError):
                return HttpResponseRedirect("oauth")

            # For creating new file we required username/repositoryName, filename and commit message
            repo = g.get_repo(request.session["user_repo_name"])
            filename = datetime.datetime.now().strftime("%Y%m%d_%H_%M_%S") + ".md"
            commit_msg =  filename + " is created"

            repo.create_file(filename, commit_msg, content)

        # After successfully creating new file redirect to home page
        return HttpResponseRedirect("/")

    # If get request (request come from home page 'Create New')
    return render(request, "gitdown/new.html")

def edit(request):
    if "token" not in request.session:
        return HttpResponseRedirect("oauth")

    # If POST request then collect content from textarea to Edit/Update a file
    if request.method == "POST":
        form = UpdateForm(request.POST)
        if form.is_valid():
            file_name = form.cleaned_data["file_name"]
            content = form.cleaned_data["content"]

            # If token is not set or token is get expired then redirect to '/oauth'
            try:
                g = Github(request.session["token"])
            except (BadCredentialsException , KeyError):
                return HttpResponseRedirect("oauth")

            # Get repository object by using this object get file object (by providing filename)
            repo = g.get_repo(request.session["user_repo_name"])
            contents = repo.get_contents(file_name)

            # Four parameters are [path/filename, commit message, markdown content, file SHA
            repo.update_file(contents.path, file_name + "Updated", content, contents.sha)

        # After successfully Updating a file redirect to home page
        return HttpResponseRedirect("/")

    # If it is not a POST request then get the filenaname and continue..
    file_name = request.GET.get("file_name")

    # If token is not set or token is get expired then redirect to '/oauth'
    try:
        g = Github(request.session["token"])
    except (BadCredentialsException , KeyError):
        return HttpResponseRedirect("oauth")

    # Get the repository then get file object and return markdown content of a file after decoding
    # content is writen into to textarea to edit it
    repo = g.get_repo(request.session["user_repo_name"])
    contents = repo.get_contents(file_name)
    return render(request, "gitdown/edit.html", {
        "content" : contents.decoded_content.decode(),
        "name":file_name
    })

def delete(request):
    if "token" not in request.session:
        return HttpResponseRedirect("oauth")

    file_name = request.GET.get("file_name")

    # If token is not set or token is get expired then redirect to '/oauth'
    try:
        g = Github(request.session["token"])
    except (BadCredentialsException , KeyError):
        return HttpResponseRedirect("oauth")

    # Get the repository then get file object use this object to get path and SHA
    repo = g.get_repo(request.session["user_repo_name"])
    contents = repo.get_contents(file_name)

    # Three paremeters [path/filename, commit message, file SHA]
    repo.delete_file(contents.path, contents.path + " Deleted.", contents.sha)
    return HttpResponseRedirect("/")

def logout(request):
    # Delete session of a token and redirect to home page
    try:
        del request.session["token"]
        return HttpResponseRedirect("https://github.com/logout")
    except KeyError:
        pass
    return HttpResponseRedirect("/")