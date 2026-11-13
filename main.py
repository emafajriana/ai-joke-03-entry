import os
from pathlib import Path


JOKE = "My coding agent stood by its fix through the entire code review. Then I typed 'are you sure?' and it apologised and put the bug back."

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")
