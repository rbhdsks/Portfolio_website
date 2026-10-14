"""Generate index.html from portfolio_config.py using only standard Python."""
from html import escape
from pathlib import Path
from string import Template
from urllib.parse import quote, urlparse

from portfolio_config import PROFILE

ROOT = Path(__file__).resolve().parent

TEMPLATE = Template('''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="$name — $intro">
  <meta name="theme-color" content="#f7f6f2">
  <title>$name</title>
  <style>
    :root { color-scheme: light; --paper: #f7f6f2; --ink: #282e29;
      --muted: #626960; --green: #3d5946; --line: #d9dcd3; }
    * { box-sizing: border-box; }
    body { margin: 0; background: var(--paper); color: var(--ink);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      -webkit-font-smoothing: antialiased; }
    main { min-height: 100vh; min-height: 100svh; width: min(100%, 1000px);
      margin: auto; padding: 72px 48px; display: flex;
      flex-direction: column; justify-content: center; }
    .profile { display: grid; grid-template-columns: minmax(0, 1fr) 264px;
      align-items: center; gap: 64px; }
    h1 { font-family: Georgia, "Times New Roman", serif; font-weight: 400;
      font-size: clamp(2.8rem, 6vw, 4.7rem); line-height: 1.07;
      letter-spacing: -0.055em; margin: 0; text-wrap: balance; }
    .intro { color: var(--muted); margin: 24px 0 0;
      font-size: .98rem; line-height: 1.9; max-width: 36ch; }
    .portrait { display: block; width: 100%; height: auto;
      aspect-ratio: 962 / 1306; object-fit: cover; border-radius: 5px; }
    nav { display: flex; flex-wrap: wrap; gap: 12px 28px; margin-top: 30px; }
    a { color: var(--green); text-decoration: none; display: inline-flex;
      align-items: center; gap: 10px; min-height: 44px;
      border-bottom: 1px solid var(--line); font-size: .95rem; font-weight: 500; }
    a:hover { border-bottom-color: var(--green); }
    a:focus-visible { outline: 2px solid var(--green); outline-offset: 5px; }
    a svg { width: 17px; height: 17px; flex-shrink: 0; }
    .arrow { margin-left: 4px; font-weight: 400; }
    footer { border-top: 1px solid var(--line); margin-top: 60px; padding-top: 24px; }
    footer p { margin: 0; color: var(--muted); font-family: Georgia, serif;
      font-size: 1.15rem; font-style: italic; }
    @media (max-width: 680px) {
      main { padding: 40px 26px; }
      .profile { grid-template-columns: 1fr; gap: 30px; }
      .portrait { grid-row: 1; width: 144px; }
      h1 { font-size: clamp(2.8rem, 12vw, 3.7rem); max-width: 11ch; }
      .intro { margin-top: 18px; }
      nav { margin-top: 22px; }
      footer { margin-top: 38px; }
    }
  </style>
</head>
<body>
  <main>
    <section class="profile" aria-labelledby="name">
      <div>
        <h1 id="name">$name</h1>
        <p class="intro">$intro</p>
        <nav aria-label="Social profiles">
          <a href="$github">
            <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 .75a11.25 11.25 0 0 0-3.56 21.92c.56.1.77-.24.77-.54v-2.1c-3.14.68-3.8-1.33-3.8-1.33-.51-1.3-1.25-1.65-1.25-1.65-1.03-.7.08-.69.08-.69 1.14.08 1.73 1.17 1.73 1.17 1.01 1.73 2.65 1.23 3.3.94.1-.73.39-1.23.72-1.51-2.51-.28-5.15-1.26-5.15-5.59 0-1.23.44-2.24 1.16-3.03-.12-.29-.5-1.44.11-3 0 0 .95-.3 3.1 1.16a10.8 10.8 0 0 1 5.64 0c2.15-1.46 3.1-1.16 3.1-1.16.61 1.56.23 2.71.11 3 .72.79 1.16 1.8 1.16 3.03 0 4.34-2.64 5.3-5.16 5.58.4.35.77 1.04.77 2.1v3.08c0 .3.2.65.78.54A11.25 11.25 0 0 0 12 .75Z"/></svg>
            GitHub <span class="arrow" aria-hidden="true">↗</span>
          </a>
          <a href="$linkedin">
            <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.45 2H3.55C2.69 2 2 2.68 2 3.52v16.96c0 .84.69 1.52 1.55 1.52h16.9c.86 0 1.55-.68 1.55-1.52V3.52c0-.84-.69-1.52-1.55-1.52ZM7.93 18.75H4.98V9.2h2.95v9.55ZM6.45 7.9a1.71 1.71 0 1 1 0-3.42 1.71 1.71 0 0 1 0 3.42Zm12.3 10.85H15.8V14.1c0-1.11-.02-2.54-1.55-2.54-1.55 0-1.79 1.21-1.79 2.46v4.73H9.51V9.2h2.83v1.3h.04c.39-.74 1.36-1.52 2.79-1.52 2.99 0 3.58 1.97 3.58 4.53v5.24Z"/></svg>
            LinkedIn <span class="arrow" aria-hidden="true">↗</span>
          </a>
        </nav>
      </div>
      <img class="portrait" src="$photo" alt="$photo_alt" width="962" height="1306">
    </section>
    <footer><p>$quote</p></footer>
  </main>
</body>
</html>
''')


def build():
    for key in ("name", "intro", "quote", "github", "linkedin", "photo", "photo_alt"):
        if not isinstance(PROFILE.get(key), str) or not PROFILE[key].strip():
            raise ValueError(f"Please fill in PROFILE[{key!r}] in portfolio_config.py")
    for key in ("github", "linkedin"):
        url = urlparse(PROFILE[key])
        if url.scheme != "https" or not url.netloc:
            raise ValueError(f"{key} must be a complete https:// URL")
    photo = (ROOT / PROFILE["photo"]).resolve()
    try:
        relative_photo = photo.relative_to(ROOT)
    except ValueError:
        raise ValueError("Keep your photo inside the portfolio folder") from None
    if not photo.is_file():
        raise FileNotFoundError(f"Photo not found: {photo}")
    values = {key: escape(value, quote=True) for key, value in PROFILE.items()}
    values["photo"] = quote(relative_photo.as_posix(), safe="/")
    (ROOT / "index.html").write_text(TEMPLATE.substitute(values), encoding="utf-8")
    # GitHub Pages should serve index.html directly, without the old Jekyll theme.
    (ROOT / ".nojekyll").touch()
    print("Built index.html. Preview: python3 -m http.server 8000 --bind 127.0.0.1")


if __name__ == "__main__":
    build()
