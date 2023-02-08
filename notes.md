### Git and GitHub

https://www.geeksforgeeks.org/difference-between-git-and-github/

## Workflow

![workflow](https://user-images.githubusercontent.com/70502261/217616087-016423ea-081f-4eca-8e74-58e72fdcd10d.png)


## Commands


1. start the process in a specific folder
`` git init ``

2. add files
`` git add filename ``
or
`` git add . ``

3. commit 
`` git commit -m "message of your choice" ``

4. rename branch 
`` git branch -M main ``

5. add origin
`` git remote add origin link-your-repo-on-github ``

6. push 
`` git push origin main ``


## Possible errors

1. Adding individual filenames 

Say your file was named **new file.txt** meaning there is a gap between the names. doing `` git add new file.txt `` will result into an error called ``fatal pathspec not found`` 
What happens is bash terminal is sensitive to commands and interprets one word at a time. 

Fix: ensure all your file names don't have a space between them e.g. **new-file.txt** or **new_file.txt**

2. Your first commit 
you type git commit  and git says ``Please tell me who you are`` 
You are supposed to do a one-time setting for git which is where you set up your credentials i.e. username and useremail

Fix : type these commands

`` git config --global user.email "Email-you-used-to-sign-up-to github" ``


`` git config --global user.name "Github-username" ``

