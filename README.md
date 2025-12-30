# pochisanpo

Python用CLIアプリケーションフレームワーク生成ツール — ポチがコマンドラインをお散歩！

## インストール

```bash
uv sync
```

## 使い方

```bash
# 新規CLIプロジェクトを生成
uv run pochisanpo init myapp

# 生成されたプロジェクトで開発開始
cd myapp
uv sync
uv run myapp
```

## 生成されるプロジェクト構成

```
myapp/
├── src/myapp/
│   ├── main.py          # エントリーポイント
│   ├── commands/        # コマンド定義
│   │   └── hello.py     # サンプルコマンド
│   ├── core/            # ビジネスロジック
│   │   └── greeter.py   # サンプルロジック
│   ├── prompts/         # 対話型入力
│   ├── utils/           # ユーティリティ
│   └── exceptions.py    # カスタム例外
├── tests/
├── pyproject.toml
└── README.md
```

## アーキテクチャ

各層の責務:

| 層 | 責務 |
|----|------|
| `commands/` | CLIオプション/引数の定義、coreの呼び出し、出力 |
| `core/` | ビジネスロジック（CLIに依存しない） |
| `prompts/` | click.prompt()を使った対話型入力 |
| `utils/` | ヘルパー関数 |
| `exceptions.py` | カスタム例外 |

## 開発

```bash
# テスト実行
uv run pytest

# コードフォーマット
uv run black .
uv run isort .

# 型チェック
uv run mypy .
```
