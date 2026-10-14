# Minimal portfolio — Nitesh Kumar Shah

One page with your existing photo, GitHub, LinkedIn, and “Be kind always.”
The photo, LinkedIn username, custom domain and deployment branch were read from
rbhdsks/Portfolio_website (commit e901ec90590e7c3f1ff9b0bdc4de460c8ffe4b7d).

## Install on your Mac

Download minimal-portfolio.zip to your Downloads folder. In Terminal:

```bash
mkdir -p ~/Documents/portfolio-work
cd ~/Documents/portfolio-work
git clone https://github.com/rbhdsks/Portfolio_website.git
cd Portfolio_website
unzip -o ~/Downloads/minimal-portfolio.zip -d .
python3 build.py
python3 -m http.server 8000 --bind 127.0.0.1
```

Open http://localhost:8000. Stop the server with Control+C.
If you already cloned the repo, enter that folder instead of cloning again;
commit any changes you want to keep before extracting this replacement.
The archive supplies the original photo and CNAME, plus the new page and Python
files. It does not delete the original Jekyll source or research content.

## Edit later

Open portfolio_config.py in your editor, edit PROFILE, save, then run:

```bash
python3 build.py
```

Refresh your browser. No pip packages, Ruby, or Node setup is needed.
For a different photo, put it inside the repo and change PROFILE['photo'].
The design lives in build.py; index.html is generated, so don't edit it by hand.

## Publish to your existing site

After you are happy with the preview, stop the server and run:

```bash
git add build.py portfolio_config.py index.html .nojekyll README_MINIMAL.md CNAME images/profile.png
git commit -m "Simplify portfolio to one Python-editable page"
git push origin master
```

This updates the live site if GitHub Pages uses this branch. In GitHub, confirm:
Settings → Pages → Deploy from a branch → master → /(root).
Keep the custom domain niteshkumarshah.com.np. The CNAME file is preserved.
No DNS change is needed for this replacement if your existing domain already works.

The .nojekyll file makes Pages serve the generated HTML directly. The old Jekyll
pages won't be generated, so previous subpage URLs may stop working. This archive
keeps the homepage/domain, but does not add redirects for historical subpages.

## Roll back

To undo this particular commit, find its hash with git log --oneline and run:

```bash
git revert YOUR_PORTFOLIO_CHANGE_COMMIT_HASH
git push origin master
```

## Validation

Python build, generated HTML structure, configured links, bundled image, and
ZIP extraction/rebuild were checked. Browser rendering and the live deployment
were not tested. Nothing was pushed to your GitHub repository by the assistant.
