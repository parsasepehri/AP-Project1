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
    console.print("[green]1. [yellow]Edit Profile")
    console.print("[green]2. [yellow]View Posts")
    console.print("[green]3. [yellow]Manage Blocked Users")
    console.print("[green]4. [yellow]Back")
    console.print("[cyan]Please enter your choice: [/cyan]")
    choice = str(input())
    while choice not in ["1", "2", "3", "4"]:
        console.print("[bold red]Please enter a valid choice: [/bold red]")
        choice = str(input())
    return choice

def edit_profile(username):
    data = dc.load_data()
    if data == "error":
        Console().print("[bold red]Error: Having error with opening database file.[/bold red]")
        return "error"
    
    console = Console()
    console.print("[cyan]Enter new username (leave blank to keep current): [/cyan]")
    new_username = str(input())
    if new_username and new_username != username:
        while not isvalid_username(new_username) or user_found(new_username):
            console.print("[bold red]Please enter a valid and unique username: [/bold red]")
            new_username = str(input())
    
    console.print("[cyan]Enter new password (leave blank to keep current): [/cyan]")
    new_password = str(input())
    if new_password:
        while not isvalid_password(new_password):
            console.print("[bold red]Please enter a valid password: [/bold red]")
            new_password = str(input())
    
    console.print("[cyan]Enter new bio (leave blank to keep current): [/cyan]")
    new_bio = str(input())
    
    console.print("[cyan]Set account status ([green]public[/green]/[red]private[/red], leave blank to keep current): [/cyan]")
    new_status = str(input()).lower()
    while new_status and new_status not in ["public", "private"]:
        console.print("[bold red]Please enter 'public' or 'private': [/bold red]")
        new_status = str(input()).lower()
    
    for user in data["users"]:
        if user["username"] == username:
            if new_username and new_username != username:
                user["username"] = new_username
            if new_password:
                user["password"] = new_password
            if new_bio:
                user["bio"] = new_bio
            if new_status:
                user["account stat"] = new_status
            break
    
    dc.save_data(data)
    for step in track(range(10), description="[cyan]Profile updated...[/cyan]", style="blue"):
        time.sleep(0.5)
    
    return new_username if new_username else username

def view_posts(username):
    data = dc.load_data()
    if data == "error":
        Console().print("[bold red]Error: Having error with opening database file.[/bold red]")
        return
    
    console = Console()
    user_posts = [post for post in data["posts"] if post["user_id"] == next((u["username"] for u in data["users"] if u["username"] == username), None)]
    
    if not user_posts:
        console.print("[yellow]You have no posts yet![/yellow]")
    else:
        for post in user_posts:
            console.print(f"[cyan]Post ID: {post['id']} | Caption: {post['caption']}")
            console.print(f"[white]Tags: {', '.join(post['tags'])} | Likes: {len(post['likes'])} | Comments: {len(post['comments'])}")
            console.print(f"[gray]Posted at: {post['created_at']}[/gray]\n")
    
    console.print("[cyan]Press Enter to continue...[/cyan]")
    input()

def manage_blocked_users(username):
    data = dc.load_data()
    if data == "error":
        Console().print("[bold red“Go ahead and create something amazing!”]Error: Having error with opening database file.[/bold red]")
        return
    
    console = Console()
    for user in data["users"]:
        if user["username"] == username:
            blocked_users = user["blocked users"]
            if not blocked_users:
                console.print("[yellow]You have no blocked users![/yellow]")
                console.print("[cyan]Press Enter to continue...[/cyan]")
                input()
                return
            
            console.print("[cyan]Blocked Users:[/cyan]")
            for i, blocked_user in enumerate(blocked_users, 1):
                console.print(f"[green]{i}. [yellow]{blocked_user}")
            
            console.print("[cyan]Enter the number of the user to unblock (or 0 to go back): [/cyan]")
            choice = str(input())
            while choice != "0" and not (choice.isdigit() and 1 <= int(choice) <= len(blocked_users)):
                console.print("[bold red]Please enter a valid choice: [/bold red]")
                choice = str(input())
            
            if choice == "0":
                return
            
            unblock_user = blocked_users[int(choice) - 1]
            user["blocked users"].remove(unblock_user)
            dc.save_data(data)
            for step in track(range(10), description=f"[cyan]Unblocked {unblock_user}...[/cyan]", style="blue"):
                time.sleep(0.5)
            return

def main(username):
    os.system("cls")
    while True:
        choice = show_profile_menu()
        if choice == "1":
            username = edit_profile(username)
            if username == "error":
                return "error"
        elif choice == "2":
            view_posts(username)
        elif choice == "3":
            manage_blocked_users(username)
        else:
            return username
