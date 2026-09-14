/* Paste into the DevTools console on https://leetcode.com while logged in.
 *
 * csrftoken is readable from document.cookie.
 * LEETCODE_SESSION is HttpOnly — copy it from Application → Cookies.
 */
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
