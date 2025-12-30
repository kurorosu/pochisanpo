"""プロジェクト生成ロジック."""

from pathlib import Path

from pochisanpo import __version__
from pochisanpo.templates import default as templates


class ProjectGenerator:
    """CLIプロジェクトを生成するクラス."""

    def __init__(self, name: str, target_dir: Path | None = None) -> None:
        """初期化.

        Args:
            name: プロジェクト名.
            target_dir: 生成先ディレクトリ（省略時はカレント）.
        """
        self.name = name
        self.version = __version__
        self.project_dir = (target_dir or Path.cwd()) / name

    def generate(self) -> None:
        """プロジェクトを生成する."""
        self._create_directories()
        self._create_source_files()
        self._create_test_files()
        self._create_config_files()

    def _create_directories(self) -> None:
        """ディレクトリ構成を作成する."""
        src_dir = self.project_dir / "src" / self.name
        dirs = [
            src_dir / "commands",
            src_dir / "core",
            src_dir / "prompts",
            src_dir / "utils",
            self.project_dir / "tests",
        ]
        for d in dirs:
            d.mkdir(parents=True, exist_ok=True)

    def _create_source_files(self) -> None:
        """ソースファイルを作成する."""
        src_dir = self.project_dir / "src" / self.name

        # パッケージ __init__.py
        self._write(
            src_dir / "__init__.py",
            templates.package_init(self.name, self.version),
        )

        # main.py
        self._write(
            src_dir / "main.py",
            templates.main_py(self.name),
        )

        # commands/
        self._write(
            src_dir / "commands" / "__init__.py",
            templates.commands_init(),
        )
        self._write(
            src_dir / "commands" / "hello.py",
            templates.hello_py(self.name),
        )

        # core/
        self._write(
            src_dir / "core" / "__init__.py",
            templates.core_init(),
        )
        self._write(
            src_dir / "core" / "greeter.py",
            templates.greeter_py(),
        )

        # prompts/
        self._write(
            src_dir / "prompts" / "__init__.py",
            templates.prompts_init(self.name),
        )

        # utils/
        self._write(
            src_dir / "utils" / "__init__.py",
            templates.utils_init(self.name),
        )

        # exceptions.py
        self._write(
            src_dir / "exceptions.py",
            templates.exceptions_py(self.name),
        )

    def _create_test_files(self) -> None:
        """テストファイルを作成する."""
        tests_dir = self.project_dir / "tests"

        self._write(
            tests_dir / "__init__.py",
            templates.tests_init(self.name),
        )
        self._write(
            tests_dir / "test_cli.py",
            templates.test_cli_py(self.name),
        )

    def _create_config_files(self) -> None:
        """設定ファイルを作成する."""
        self._write(
            self.project_dir / "pyproject.toml",
            templates.pyproject_toml(self.name, self.version),
        )
        self._write(
            self.project_dir / "README.md",
            templates.readme_md(self.name),
        )

    def _write(self, path: Path, content: str) -> None:
        """ファイルを書き込む."""
        path.write_text(content, encoding="utf-8")
