from database_commands import load_data, save_data
from rich.progress import track
import time
import login
import search
from rich.console import Console
import os

def wait(description,color):
    for step in track(range(10), description=f"[{color}]{description}[/{color}]",style="blue"):
        time.sleep(0.5)

def show_menu():
    console = Console()
    console.print("[green]1. [yellow]Home")
    console.print("[green]2. [yellow]Search")
    console.print("[green]3. [yellow]Profile[/yellow]")
    console.print("[bold red]4. Exit[/bold red]")
    console.print("[cyan]Please enter your choice: [/cyan]")
    choice = str(input())
    while(choice != "1" and choice != "2" and choice != "3" and choice != "4"):
        Console().print("[bold red]Please enter a valid choice: [/bold red]")
        choice = str(input())
    return choice

log_stat = login.main()
while True:
    if(log_stat != "error"):
        os.system("cls")
        choice = show_menu()
        if(choice == "1"):
            wait("wait a second...","blue")
            #your function should be here
        elif(choice == "2"):
            wait("wait a second...","blue")
            search.main(log_stat)
        elif(choice == "3"):
            wait("wait a second...","blue")
            #your function should be here
        else:
            Console().print("[bold cyan]We are happy to see you,take care![/bold cyan]")
            break