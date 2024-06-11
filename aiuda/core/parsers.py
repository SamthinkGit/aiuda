import re
from typing import Optional


def extract_keyword_from_function(function_str: str) -> Optional[str]:
    match = re.search(r"\w+\((.*?)\)", function_str)
    if match:
        return match.group(1)
    return None
