
# 2to3 --output-dir=python3-version/mycode -W -n python2-version/mycode
import typer

app = typer.Typer()


@app.command()
def from2_to3(input_dir: str, output_dir: str) -> None:
    typer.echo(f"Convert {input_dir} to python 3")
    pass


@app.command()
def spread_coconut(input_dir: str, output_dir: str) -> None:
    typer.echo(f"Convert {input_dir} to python 2 and 3")
    pass


if __name__ == '__main__':
    app()
