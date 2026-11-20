import re

def sanitize_string(val, max_length=1000):
    if not isinstance(val, str):
        return ""
    # Strip dangerous HTML or script tags, and trim
    cleaned = re.sub(r"<[^>]*?>", "", val).strip()
    return cleaned[:max_length]

def validate_language(lang):
    if not lang or not isinstance(lang, str):
        return "te"
    lang_clean = lang.lower().strip()
    return lang_clean if lang_clean in ["te", "en"] else "te"

def validate_session_id(session_id):
    if not session_id or not isinstance(session_id, str):
        return None
    cleaned = re.sub(r"[^a-zA-Z0-9_\-]", "", session_id)
    return cleaned[:100] if cleaned else None
