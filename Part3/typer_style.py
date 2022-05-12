import typer

def main():
    # prenom = typer.style("Syl20", bold=True)
    # prenom = typer.style("Syl20", bg=typer.colors.BRIGHT_RED)
    prenom = typer.style("Syl20", fg=typer.colors.BRIGHT_RED,  bg=typer.colors.BLUE)
    typer.echo(f"Bonjour {prenom}")

    # typer.secho("Hello World !", bold=True,fg=typer.colors.BLUE,  bg=typer.colors.BRIGHT_RED)

main()