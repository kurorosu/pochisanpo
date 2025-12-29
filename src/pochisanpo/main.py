"""pochisanpoのCLIエントリーポイント."""

import click

from pochisanpo import __version__
from pochisanpo.commands.init import init


@click.group()
@click.version_option(version=__version__)
def cli() -> None:
    """Pochisanpo - Python用CLIアプリケーションフレームワーク生成ツール."""
    pass


cli.add_command(init)


def main() -> None:
    """エントリーポイント."""
    cli()


if __name__ == "__main__":
    main()
