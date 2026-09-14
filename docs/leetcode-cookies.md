# Refresh LeetCode submit cookies

The Submit to LeetCode workflow reads two repository secrets:

- `LEETCODE_SESSION`
- `LEETCODE_CSRF_TOKEN`

Those come from a logged-in [leetcode.com](https://leetcode.com) browser session.
They last on the order of days, not months. When submit returns HTTP 401/403,
refresh both secrets and re-run the workflow.

Do not commit cookie values. Do not use `leetcode.cn`.

## Console snippet

Open https://leetcode.com while logged in, then paste
[`copy-leetcode-cookies.js`](copy-leetcode-cookies.js) into the DevTools
console:

```javascript
(() => {
  const cookies = Object.fromEntries(
    document.cookie.split(";").filter(Boolean).map((part) => {
      const [name, ...rest] = part.trim().split("=");
      return [name, rest.join("=")];
    }),
  );
  const csrf = cookies.csrftoken || "";
  console.log(
    "LEETCODE_CSRF_TOKEN:",
    csrf || "(missing — logged in on leetcode.com?)",
  );
  console.log(
    "LEETCODE_SESSION:",
    cookies.LEETCODE_SESSION ||
      "(HttpOnly — copy from DevTools → Application → Cookies → https://leetcode.com → LEETCODE_SESSION)",
  );
  if (csrf && typeof copy === "function") {
    copy(csrf);
    console.log("Copied csrftoken to clipboard.");
  }
})();
```

`csrftoken` is copied to the clipboard when `copy()` exists.

## `LEETCODE_SESSION` is HttpOnly

Page JavaScript cannot read it. Copy the value from:

DevTools → Application → Cookies → `https://leetcode.com` → `LEETCODE_SESSION`

## Update GitHub secrets

1. Repo → Settings → Secrets and variables → Actions
2. Set `LEETCODE_CSRF_TOKEN` to the console `csrftoken` value
3. Set `LEETCODE_SESSION` to the Application-panel cookie value
4. Re-run **Submit to LeetCode** on the open daily PR
