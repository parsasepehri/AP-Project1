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
    console.print("[purple]1. [yellow]edit Profile")
    console.print("[purple]2. [yellow]view Posts")
    console.print("[purple]3. [yellow]blocked user settings")
    console.print("[purple]4. [yellow]back")
    console.print("[cyan]enter your choice: [/cyan]")
    choice = str(input())
    while choice not in ["1", "2", "3", "4"]:
        console.print("[bold red] enter a valid choice: [/bold red]")
        choice = str(input())
    return choice



def edit_profile(username):
    data = dc.load_data()
    if data == "error":
        console = Console()
        console.print("[bold red]error: there is a problem opening dadtabase file.[/bold red]")
        return "error"
    
    console = Console()
    print("[cyan]what would you like to edit?[/cyan]")
    print("[lightgreen]1.[/green] username")
    print("[lightgreen]2.[/green] password")
    print("[lightgreen]3.[/green] bio")
    print("[lightgreen]4.[/green] account privacy (Public/Private)")
    print("[red]5.[/red] Cancel")
    
    choice = input("[cyan]enter your choice: [/cyan]")

    if choice == "1":
        print("[cyan]enter new username: [/cyan]")
        new_username = input()
        
        
        for a in range(int('inf')):  
            if new_username != "" and new_username != username and isvalid_username(new_username) and not user_found(new_username):
                break
            else:
                console.print("[bold red]enter a valid and unique username: [/bold red]")
                new_username = input("[cyan]enter new username : [/cyan]")
        
        for user in data["users"]:
            if user["username"] == username:
                if new_username != "":
                    user["username"] = new_username
                break

    elif choice == "2":
        print("[cyan]enter new password : [/cyan]")
        new_password = input()
        
        for b in range(int('inf')): 
            if new_password != "" and isvalid_password(new_password):
                break
            else:
                console.print("[bold red]enter a valid password: [/bold red]")
                new_password = input("[cyan]enter new password : [/cyan]")
        
        for user in data["users"]:
            if user["username"] == username:
                if new_password != "":
                    user["password"] = new_password
                break

    elif choice == "3":
        print("[cyan]enter new bio : [/cyan]")
        new_bio = input()
        
        for user in data["users"]:
            if user["username"] == username:
                if new_bio != "":
                    user["bio"] = new_bio
                break

    elif choice == "4":
        print("[cyan]set account privacy([green]public[/green]/[red]private[/red]: [/cyan]")
        new_privacy = input()

        while True:
         console.print("[cyan]choose the new account privacy:[/cyan]")
         console.print("1. [green]Public[/green]")
         console.print("2. [red]Private[/red]")
         choice = input("[bold yellow]your choice (1 or 2): [/bold yellow]")
         if choice == "1":
             new_privacy = "public"
             break
         elif choice == "2":
          new_privacy = "private"
          break
         else:
           console.print("[bold red]invalid input. enter 1 or 2 .[/bold red]")

         for user in data["users"]:
          if user["username"] == username:
           if new_privacy!= "":
             user["account stat"] = new_privacy
           break

    elif choice == "5":
        console.print("[bold yellow]back.[/bold yellow]")
        return "canceled"
    else:
        console.print("[bold red]invalid option! try again.[/bold red]")
    dc.save_data(data)
    for step in track(range(10), description="[cyan]you updated profile...[/cyan]", style="blue"):
        time.sleep(0.5)
    return new_username if new_username else username

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
            console.print(f"[gray]Posted at: {post['created_at']}[/gray]\n")
    console.print("[cyan]Press Enter to continue...[/cyan]")
    input()

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
                console.print(f"[yellow]{blocked_user}")
            console.print("[cyan]enter the username of the user to unblock (or type '0' to go back): [/cyan]")
            choice = input()
            while choice != "0":
                if choice in blocked_users: 
                    break
                else:
                    console.print("[bold red]please enter a valid username from the blocked list.[/bold red]")
                choice = input("[cyan]enter the username of the user to unblock (or type '0' to go back): [/cyan]").strip()
            
            if choice == "0":
                return
            
            unblock_user = choice 
            user["blocked users"].remove(unblock_user)
            dc.save_data(data)
            console.print(f"[cyan]unblocking {unblock_user}...[/cyan]")
            for _ in range(10):
                time.sleep(0.5)
                console.print(f"[blue]unblocked {unblock_user}... Step {_+1}/10[/blue]")
            console.print(f"[lightgreen]successfully unblocked {unblock_user}![/bold green]")
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
            blocked_user_settings(username)
        else:
            return username