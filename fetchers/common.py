from datetime import datetime, timezone
from typing import Dict


def normalize_article(
    title: str,
    content: str,
    source: str,
    url: str,
    fetched_at: str | None = None
) -> Dict[str, str]:

    return {
        "title": title or "",
        "content": content or "",
        "source": source or "",
        "url": url or "N/A",
        "fetched_at": fetched_at
        or datetime.now(timezone.utc).isoformat()
    }

