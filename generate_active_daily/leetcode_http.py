"""HTTP helper for unofficial LeetCode calls.

curl_cffi impersonates Chrome TLS so Cloudflare is less likely to serve
the interstitial that stock requests gets from GitHub Actions.
"""

from __future__ import annotations

import os
from typing import Any


def is_cloudflare_challenge(body: str) -> bool:
    text = (body or "").lower()
    return "just a moment" in text or "challenges.cloudflare.com" in text


def session_cookies(session: str, csrf: str) -> dict[str, str]:
    cookies = {"LEETCODE_SESSION": session, "csrftoken": csrf}
    clearance = os.environ.get("LEETCODE_CF_CLEARANCE", "").strip()
    if clearance:
        cookies["cf_clearance"] = clearance
    return cookies


def request(method: str, url: str, **kwargs: Any) -> Any:
    from curl_cffi import requests as cf_requests

    impersonate = os.environ.get("LEETCODE_IMPERSONATE", "chrome").strip() or "chrome"
    return getattr(cf_requests, method)(url, impersonate=impersonate, **kwargs)
