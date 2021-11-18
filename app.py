import os
import subprocess
import tempfile
from glob import glob
import shutil
from typing import Iterable, List

import typer
from tqdm import tqdm

from converter.const import FOLDER_EXCEPTIONS

app = typer.Typer()


def _has_blamed_parts(path: str) -> bool:
    parts = {x.lower() for x in path.replace("\\", "/").split("/") if x.strip()}
    return bool(parts.intersection(FOLDER_EXCEPTIONS))


def _ignore_blamed_parts(_: str, paths: List[str]) -> Iterable[str]:
    return [path for path in paths if _has_blamed_parts(path)]


@app.command()
def from2to3(source: str, dest: str, verbose: bool = False) -> None:
    typer.echo(f"Convert {source} to python 3")
    if os.path.isdir(dest):
        shutil.rmtree(dest, ignore_errors=True)
    shutil.copytree(source, dest, ignore=_ignore_blamed_parts)
    result = subprocess.run(
        ["2to3", "-W", "-n", dest],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Conversion error: {result.stderr}")
    if verbose:
        typer.echo(result.stdout)


@app.command()
def coconify(
    source: str,
    dest: str,
    version: str = "3.7",
    verbose: bool = False,
) -> None:
    intermediate_dest = f"{tempfile.mkdtemp()}/coco"
    typer.echo(f"Convert {source} to python 2 and 3")
    shutil.copytree(source, intermediate_dest, ignore=_ignore_blamed_parts)
    files = glob(os.path.join(intermediate_dest, "**", "*.py"), recursive=True)
    for x in tqdm(files, desc="Rename py files to coco"):
        shutil.move(x, f"{x[:-3]}.coco")

    typer.echo(f"Compiling coco from {intermediate_dest} to python")

    result = subprocess.run(
        ["coconut", intermediate_dest, dest, "-d", f"-t{str(version).strip()}"],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(f"Compilation error: {result.stderr}")
    if verbose:
        typer.echo(result.stdout)


if __name__ == "__main__":
    app()
