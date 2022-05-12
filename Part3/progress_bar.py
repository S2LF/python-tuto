import time
import typer

def main():
    prenoms = range(100)
    with typer.progressbar(prenoms) as progress:
        for prenom in progress:
            time.sleep(0.05)
    
    typer.echo("fin du script")

main()