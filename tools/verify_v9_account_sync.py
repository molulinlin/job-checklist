"""Minimal static guard for the v9 account-sync integration."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
html = (root / "index.html").read_text(encoding="utf-8")
rules = (root / "firestore.rules").read_text(encoding="utf-8")

required_html = [
    "v9 独立账户同步",
    "accounts:signUp",
    "accounts:signInWithPassword",
    "securetoken.googleapis.com",
    "syncToV9Account",
    "users/' + encodeURIComponent(v9Account.uid) + '/private/state",
    "v9Account ? 'none' : 'block'",
    "2026.09.16 · v9 独立账户同步",
]
for marker in required_html:
    assert marker in html, f"Missing v9 integration marker: {marker}"

assert "request.auth != null && request.auth.uid == userId" in rules
assert "match /users/{userId}/private/state" in rules
print("v9 account-sync static check passed")
