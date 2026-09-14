from generate_active_daily.leetcode_http import (
    is_cloudflare_challenge,
    session_cookies,
)


def test_is_cloudflare_challenge_detects_interstitial():
    assert is_cloudflare_challenge("<title>Just a moment...</title>")
    assert is_cloudflare_challenge("https://challenges.cloudflare.com/turnstile")
    assert not is_cloudflare_challenge("Forbidden")


def test_session_cookies_include_optional_clearance(monkeypatch):
    monkeypatch.delenv("LEETCODE_CF_CLEARANCE", raising=False)
    cookies = session_cookies("sess", "csrf")
    assert cookies == {"LEETCODE_SESSION": "sess", "csrftoken": "csrf"}
    monkeypatch.setenv("LEETCODE_CF_CLEARANCE", "clear-me")
    cookies = session_cookies("sess", "csrf")
    assert cookies["cf_clearance"] == "clear-me"
