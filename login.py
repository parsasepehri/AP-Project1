from rich.console import Console
from rich.progress import track
import time
import os
import database_commands as dc
def show_menu():
    console = Console()
    console.print("[bold cyan]******WELCOME TO OUR PROJECT******\n")
    console.print("[green]1. [yellow]Login[/yellow]\n[green]2. [yellow]Sign up")
    console.print("[cyan]Please enter your choice: [/cyan]")
    choice = str(input(""))
    while(choice != "1" and choice != "2"):
        Console().print("[bold red]Please enter a valid choice: [/bold red]")
        choice = str(input())
    return choice

def isvalid_username(username):
    invalid_chars = "!@#$%\^&*/|,:'"
    for i in username:
        if(i in invalid_chars):
            return False
    return True

def user_found(username):
    data = dc.load_data()
    for user in data["users"]:
        if user == username:
            return True
    return False

def isvalid_password(password):
    invalid_chars = "!@#$%\^&*/|,:'"
    for i in password:
        if(i in invalid_chars):
            return False
    return True

def password_found(password:str):
    data = dc.load_data()
    if password in [user["password"] for user in data["users"].values()]:
        return True
    return False

def login():
    data = dc.load_data()
    if(data == "error"):
        Console().print("[bold red]Error:Having error with opening data base file.[/bold red]")
        return "error"
    Console().print("[cyan]Please enter your username: [/cyan]")
    username = str(input())
    while(isvalid_username(username) == False or user_found(username) == False):
        Console().print("[bold red]Please enter a valid username or turn back:\n[green]1. [yellow]enter a username\n[green]2. [yellow]turn back[/yellow]")
        choice = str(input())
        if(choice == "2"):
            return "error"
        elif choice == "1":
            Console().print("[cyan]Please enter your username: [/cyan]")
            username = str(input())
        else:
            while(choice != "1" and choice != "2"):
                Console().print("[bold red]Please enter a valid choice: [/bold red]")
                choice = str(input())
                if choice == "1":
                    Console().print("[cyan]Please enter your username: [/cyan]")
                    username = str(input())
                elif choice == "2":
                    return "error"
    Console().print("[cyan]Please enter your password: [/cyan]")
    password = str(input())
    while(isvalid_password(password) == False or password_found(password) == False):
        Console().print("[bold red]Please enter a valid password: [/bold red]")
        password = str(input())
    for step in track(range(10), description=f"[green]Logged in,wait a second [/green]",style="blue"):
        time.sleep(0.5)

def sign_up():
    data = dc.load_data()
    if(data == "error"):
        Console().print("[bold red]Error:Having error with opening data base file.[/bold red]")
        return "error"
    Console().print("[cyan]Please enter your username: [/cyan]")
    username = str(input())
    while(isvalid_username(username) == False):
        Console().print("[bold red]Please enter a valid username: [/bold red]")
        username = str(input())
    if user_found(username) == True:
        Console().print("[bold red]The username already exists! [/bold red]")
        return "error"
    Console().print("[cyan]Please enter your password: [/cyan]")
    password = str(input())
    while(isvalid_password(password) == False):
        Console().print("[bold red]Please enter a valid password: [/bold red]")
        password = str(input())
    data["users"][username] = {"password": password, "liked_posts": [],"comments": {}}
    dc.save_data(data)
    for step in track(range(10), description=f"[green]Signed up,wait a second [/green]",style="blue"):
        time.sleep(0.5)

def main():
    os.system("cls")
    choice = show_menu()
    if(choice == "1"):
        return login()
    else:
        return sign_up()