# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "jinja2",
#     "requests",
# ]
# ///
from pathlib import Path
import jinja2
import requests

TEMPLATE_FILE = Path(".") / "README.md.j2"
OUTPUT_FILE = Path(".") / "README.md"

def get_posts() -> list[dict]:
    response = requests.get(
        "https://saktidwicahyono.name/api/blogs/",
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"
        },
    )
    response.raise_for_status()
    return response.json()["results"]

def main() -> int:
    print("generating...")
    template = jinja2.Template(TEMPLATE_FILE.read_text())

    new_readme = template.render(posts=get_posts())

    OUTPUT_FILE.write_text(new_readme)

    return 0

if __name__ == "__main__":
    main()
