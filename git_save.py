import os

commit_message = input("\033[94mCommit Message > \033[0m")

os.system("pip freeze > requirements.txt")
os.system("git add .")
os.system(f'git commit -m "{commit_message}"')
os.system("git push origin main")