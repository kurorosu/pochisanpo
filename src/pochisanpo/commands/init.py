"""initコマンド - 新規CLIプロジェクトを生成."""

from pathlib import Path

import click

from pochisanpo.generators import ProjectGenerator


@click.command()
@click.argument("name")
def init(name: str) -> None:
    """新規CLIプロジェクトを生成する.

    NAMEはプロジェクト名.
    """
    project_dir = Path(name)

    if project_dir.exists():
        click.echo(f"Error: '{name}' already exists.", err=True)
        raise SystemExit(1)

    generator = ProjectGenerator(name)
    generator.generate()

    click.echo(f"Created project '{name}'")
    click.echo(f"  cd {name}")
    click.echo("  uv sync")
    click.echo(f"  uv run {name}")
