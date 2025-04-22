from rich.console import Console
from rich.progress import track
import time
import os
import database_commands as dc
def isvalid_username(username):
    invalid_chars = "!@#$%^&*/|,:'"
    for i in username:
        if(i in invalid_chars):
            return False
    return True

def isvalid_password(password):
    invalid_chars = "!@#$%^&*/|,:'"
    for i in password:
        if(i in invalid_chars):
            return False
    return True

def user_found(username):
    data = dc.load_data()
    for user in data["users"]:
        if user["username"] == username:
            return True
    return False

def show_profile_menu():
    console = Console()
    console.print("[green]1. [yellow]edit Profile")
    console.print("[green]2. [yellow]view Posts")
    console.print("[green]3. [yellow]view savedposts")
    console.print("[green]4. [yellow]blocked user settings")
    console.print("[green]5. [yellow]back")
    console.print("[cyan]enter your choice: [/cyan]")
    choice = str(input())
    while choice not in ["1", "2", "3", "4", "5"]:
        console.print("[bold red]enter a valid choice: [/bold red]")
        choice = str(input())
    return choice

def edit_profile(username):
    os.system("cls")
    data = dc.load_data()
    if data == "error":
        console = Console()
        console.print("[bold red]error: there is a problem opening dadtabase file.[/bold red]")
        return "error"
    console = Console()
    console.print("[cyan]what would you like to edit?[/cyan]")
    console.print("[green]1. [yellow]username")
    console.print("[green]2. [yellow]password")
    console.print("[green]3. [yellow]bio")
    console.print("[green]4. [yellow]account privacy (Public/Private)")
    console.print("[red]5. Cancel[/red]")
    console.print("[cyan]enter your choice: [/cyan]")
    choice = str(input())
    while choice not in ["1","2","3","4","5"]:
        console.print("[bold red]invalid option! try again.[/bold red]")
        choice = str(input())

    if choice == "1":
        os.system("cls")
        console.print("[cyan]enter your new username: [/cyan]")
        new_username = str(input())
        while new_username == "" or new_username == username or isvalid_username(new_username) == False or user_found(new_username) == True:
            console.print("[cyan]enter a valid username: [/cyan]")
            new_username = str(input())
        for user in data["users"]:
            if user["username"] == username:
                user["username"] = new_username
        dc.save_data(data)
        for step in track(range(10), description="[cyan]you updated profile...[/cyan]", style="blue"):
            time.sleep(0.5)
    elif choice == "2":
        os.system("cls")
        console.print("[cyan]enter your new password : [/cyan]")
        new_password = str(input())
        while new_password == "" or isvalid_password(new_password) == False:
            console.print("[bold red]enter a valid password: [/bold red]")
            new_password = str(input())
        for user in data["users"]:
            if user["username"] == username:
                user["password"] = new_password
        dc.save_data(data)
        for step in track(range(10), description="[cyan]you updated profile...[/cyan]", style="blue"):
            time.sleep(0.5)
    elif choice == "3":
        os.system("cls")
        console.print("[cyan]enter your new bio: [/cyan]")
        new_bio = str(input())
        for user in data["users"]:
            if user["username"] == username:
                user["bio"] = new_bio
        dc.save_data(data)
        for step in track(range(10), description="[cyan]you updated profile...[/cyan]", style="blue"):
            time.sleep(0.5)
    elif choice == "4":
        os.system("cls")
        console.print("[cyan]set account privacy:\n[green]1. [yellow]public\n[green]2. [yellow]private[/yellow]")
        choice = str(input())
        while choice != "1" and choice != "2":
            console.print("[bold red]Please enter a valid number: [/bold red]")
            choice = str(input())
        for user in data["users"]:
            if user["username"] == username:
                if choice == "1":
                    user["account stat"] = "public"
                else:
                    user["account stat"] = "private"
        dc.save_data(data)
        for step in track(range(10), description="[cyan]you updated profile...[/cyan]", style="blue"):
            time.sleep(0.5)
    else:
        return "canceled"


def view_posts(username):
    data = dc.load_data()
    if data == "error":
        Console().print("[bold red]there is a problem opening dadtabase file.[/bold red]")
        return
    
    console = Console()
    user_id = None
    for user in data["users"]:
        if user["username"] == username:
            user_id = username
            break
    
    if user_id is None:
        console.print("[bold red]user not found![/bold red]")
        return
    
    user_posts = [post for post in data["posts"] if post["user_id"] == user_id]
    
    if not user_posts:
        console.print("[yellow]you have no posts yet![/yellow]")
    else:
        for post in user_posts:
            console.print(f"[cyan]Post ID: {post['id']} | Caption: {post['caption']}[/cyan]")
            console.print(f"[white]Tags: {', '.join(post['tags'])} | Likes: {len(post['likes'])} | Comments: {len(post['comments'])}[/white]")
            console.print(f"[green]Posted at: {post['created_at']}[/green]\n")
    console.print("[cyan]Press Enter to continue...[/cyan]")
    input()

def view_savedposts(username):
    os.system("cls")
    data = dc.load_data()
    if data == "error":
        Console().print("[bold red]there is a problem opening database file.[/bold red]")
        return

    console = Console()

    for user in data["users"]:
        if user["username"] == username:
            if len(user["saved posts"]) == 0:
                console.print("[yellow]You have no saved posts![/yellow]")
                console.print("[cyan]Press Enter to continue...[/cyan]")
                input()
                return

            saved_posts = []
            for id in user["saved posts"]:
                saved_posts.append(id)
            for saved in saved_posts:
                for posts in data["posts"]:
                    if saved == posts["id"]:
                        console.print(f"[cyan]Post ID: {posts['id']} | Caption: {posts['caption']}")
                        console.print(f"[white]Author: {posts['user_id']} | Tags: {', '.join(posts['tags'])}")
                        console.print(f"[white]Likes: {len(posts['likes'])} | Comments: {len(posts['comments'])}[/white]")
                        console.print(f"[green]Posted at: {posts['created_at']}[/green]")
            console.print("[cyan]Press Enter to continue...[/cyan]")
            input()
            return 

    console.print("[bold red]User not found![/bold red]")


def blocked_user_settings(username):
    data = dc.load_data()
    if data == "error":
        Console().print("[bold red]there is a problem opening dadtabase file.[/bold red]")
        return
    
    console = Console()
    for user in data["users"]:
        if user["username"] == username:
            blocked_users = user["blocked users"]
            if not blocked_users:
                console.print("[yellow]there is no blocked person.[/yellow]")
                console.print("[cyan]press Enter to continue...[/cyan]")
                input()
                return
            
            console.print("[cyan]Blocked Users:[/cyan]")
            for blocked_user in blocked_users:
                console.print(f"[yellow]{blocked_user}[/yellow]")
            console.print("[cyan]enter the username of the user to unblock (or type 0 to go back): [/cyan]")
            choice = input()
            while choice != "0":
                if choice in blocked_users: 
                    break
                else:
                    console.print("[bold red]please enter a valid username from the blocked list (or type 0 to go back): [/bold red]")
                choice = input()
            
            if choice == "0":
                return
            
            unblock_user = choice 
            user["blocked users"].remove(unblock_user)
            dc.save_data(data)
            console.print(f"[cyan]unblocking {unblock_user}...[/cyan]")
            for _ in range(10):
                time.sleep(0.5)
                console.print(f"[blue]unblocked {unblock_user}... Step {_+1}/10[/blue]")
            console.print(f"[bold green]successfully unblocked {unblock_user}![/bold green]")
            time.sleep(3)
            return

def main(username):
    while True:
        os.system("cls")
        choice = show_profile_menu()
        if choice == "1":
            edit_profile(username)
        elif choice == "2":
            view_posts(username)
        elif choice == "3":
            view_savedposts(username)
        elif choice== "4":
            blocked_user_settings(username)
        else:
            
            return username
