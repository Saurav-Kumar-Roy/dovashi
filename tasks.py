from invoke import task

@task
def run(c):
    c.run("python dovashi.py")

@task
def build_debug(c):
    c.run("pyinstaller --onedir --hidden-import=pyautogui --hidden-import=mouse " \
        "--hidden-import=keyboard --hidden-import=pyperclip --hidden-import=plyer " \
        "--hidden-import=googletrans --hidden-import=plyer.platforms.win.notification " \
        "dovashi.py")

@task
def build(c):
    c.run("pyinstaller --onefile --noconsole --hidden-import=pyautogui --hidden-import=mouse --hidden-import=keyboard " \
        "--hidden-import=pyperclip --hidden-import=plyer --hidden-import=googletrans " \
        "--hidden-import=plyer.platforms.win.notification dovashi.py")

@task
def clean(c):
    c.run("echo: Cleaning build files and folders")
    c.run("rmdir /s /q build")
    c.run("rmdir /s /q dist")
    c.run("del /f /q dovashi.spec")
    c.run("echo: Cleaning complete")


