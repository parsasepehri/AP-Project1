from rich.console import Console
from rich.progress import track
import time
import os
import database_commands as dc
def isvalid_username(username):
    invalid_chars = "!@#$%\^&*/|,:'"
    for i in username:
        if(i in invalid_chars):
            return False
    return True

def user_found(username):
    data = dc.load_data()
    for user in data["users"]:
        if user["username"] == username:
            return True
    return False
def main(username):
    os.system("cls")
    console = Console()
    console.print("[cyan]Please enter the username to search: [/cyan]")
    choic = str(input(""))
    while(isvalid_username(choic) == False or user_found(choic) == False):
        Console().print("[bold red]Please enter a valid username: [/bold red]")
        choic = str(input())
    data = dc.load_data()
    for user in data["users"]:
        if user["username"] == choic:
            for blocked_user in user["blocked users"]:
                if blocked_user == username:
                    console.print("[red]Oops,the user has been blocked you![/red]")
                    time.sleep(3)
                    return "error"
    for user in data["users"]:
        if user["username"] == choic:
            console.print(f"[cyan]Posts: [white]{user['post counts']} | [cyan]Followers: [white]{len(user['followers'])} | [cyan]Following: [white]{len(user['following'])}[/white]")
            console.print(f"[medium_purple]{user['bio']}[/medium_purple]")
            follow = False
            for followers in user["followers"]:
                if followers == username:
                    follow = True
            if follow == True:
                console.print("[green]1. [yellow]unfollow")
            else:
                console.print("[green]1. [yellow]follow")
            console.print("[green]2. [yellow]block")
            choice2 = str(input(""))
            while(choice2 != "1" and choice2 != "2"):
                Console().print("[bold red]Please enter a valid choice: [/bold red]")
                choice2 = str(input())
            if choice2 == "1":
                if follow == True:
                    for user in data["users"]:
                        if user["username"] == username:
                            user["following"].remove(choic)
                        if user["username"] == choic:
                            user["followers"].remove(username)
                    for step in track(range(10), description=f"[cyan]You unfollowed {choic}...[/cyan]",style="blue"):
                        time.sleep(0.5)
                else:
                    private = False
                    for user in data["users"]:
                        if user["username"] == choic:
                            if user["account stat"] == "private":
                                private = True
                    if private == True:
                        for user in data["users"]:
                            if user["username"] == choic:
                                user["follow requests"].append(username)
                        for step in track(range(10), description=f"[cyan]You requested {choic} to follow...[/cyan]",style="blue"):
                            time.sleep(0.5)
                    else:
                        for user in data["users"]:
                            if user["username"] == username:
                                user["following"].append(choic)
                            if user["username"] == choic:
                                user["followers"].append(username)
                        for step in track(range(10), description=f"[cyan]You followed {choic}...[/cyan]",style="blue"):
                            time.sleep(0.5)
            else:
                for user in data["users"]:
                    if user["username"] == username:
                        blocked = False
                        for blocked_users in user["blocked users"]:
                            if blocked_users == choic:
                                blocked = True
                        if blocked == False:
                            user["blocked users"].append(choic)
                            for step in track(range(10), description=f"[cyan]You blocked {choic}...[/cyan]",style="blue"):
                                time.sleep(0.5)
                        else:
                            console.print("[red]You already blocked this user!")
                            time.sleep(3)
    dc.save_data(data)