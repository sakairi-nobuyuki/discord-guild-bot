#!/bin/bash
cd python_ws

set -e

# 1. pyproject.toml が存在しない、または空の場合は初期化
if [ ! -f pyproject.toml ] || [ ! -s pyproject.toml ]; then
    echo "Initializing new uv project..."
    uv init --lib --no-readme
fi

# 2. 依存関係の同期 (uv.lock に基づいて .venv を作成/更新)
# ホスト側の pyproject.toml が更新されていれば、ここで反映される
echo "Syncing dependencies..."
uv sync

# 3. メインプロセスの実行 (渡された引数を実行、なければ python main.py)
if [ $# -eq 0 ]; then
    exec uv run python main.py
else
    exec "$@"
fi
