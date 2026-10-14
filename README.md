# Nitesh Kumar Shah

A minimal, one-page portfolio with my photo, GitHub, LinkedIn, and **Be kind always.**

[Website](https://niteshkumarshah.com.np) · [GitHub](https://github.com/rbhdsks) · [LinkedIn](https://www.linkedin.com/in/niteshkumarshah)

## Files

| Path | Purpose |
| --- | --- |
| `portfolio_config.py` | Edit the name, intro, photo path, and social links |
| `build.py` | Generate the page; includes the HTML and CSS design |
| `index.html` | Generated homepage, committed for GitHub Pages |
| `images/profile.png` | Current profile photo |
| `CNAME` | Existing custom domain |
| `.nojekyll` | Serve the generated page without Jekyll |
| `archive/previous-site/` | Previous theme, pages, assets, CV files, scripts, and documentation |
| `LICENSE` | Existing repository license |

## Run locally

Python 3 is enough. No additional packages are required.

```bash
git clone https://github.com/rbhdsks/Portfolio_website.git
cd Portfolio_website
python3 build.py
python3 -m http.server 8000 --bind 127.0.0.1
```

Open http://localhost:8000. Stop the server with **Control+C**.

## Change the content

1. Edit `PROFILE` in `portfolio_config.py` and save.
2. Run `python3 build.py`.
3. Refresh the browser.

To change the photo, put the image inside this repository and update `photo`.
To change the layout or colors, edit the template in `build.py`.
`index.html` is generated; direct edits to it will be overwritten by the next build.

## Publish

After checking the local preview:

```bash
python3 build.py
git add portfolio_config.py build.py index.html images
git commit -m "Update portfolio"
git push origin master
```

GitHub Settings → Pages: **Deploy from a branch → master → /(root)**.
The `CNAME` file retains `niteshkumarshah.com.np`.

## Previous site

The previous source is kept in [`archive/previous-site/`](archive/previous-site/).
It is no longer used to build the homepage. Reuse its text, CV, publications,
and assets when expanding this portfolio. Old subpage URLs are not restored by
archiving their sources. The archive is in this public repository; it is not
private storage. See [`archive/README.md`](archive/README.md) for details.
