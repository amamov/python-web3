import subprocess
import sys


def start():
    cmd = ["python", "app/main.py"]
    subprocess.run(cmd)


def dev():
    cmd = ["nodemon", "--exec", "python", "app/main.py"]
    subprocess.run(cmd)


def else_command():
    cmd = ["echo", "python3 scripts.py <command>"]
    subprocess.run(cmd)


if __name__ == "__main__":
    try:
        command = sys.argv[1]
        if command == "start":
            start()
        elif command == "dev":
            dev()
        else:
            else_command()
    except IndexError:
        else_command()
