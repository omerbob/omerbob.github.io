# omerbobrowski.github.io

Personal academic website — plain HTML and CSS, no framework, no build step.
Drop it in a GitHub repository, switch on Pages, done.

---

## Publishing it on GitHub Pages

1. Create a repository named **`<your-github-username>.github.io`**
   (e.g. `obobrowski.github.io`). That exact name gives you the URL
   `https://<username>.github.io` with no extra configuration.
2. Upload every file and folder from this directory to the repository root —
   `index.html` must sit at the top level, not inside a subfolder.
   Either drag them into GitHub's web uploader, or:

   ```bash
   git init
   git add .
   git commit -m "New personal website"
   git branch -M main
   git remote add origin https://github.com/<username>/<username>.github.io.git
   git push -u origin main
   ```
3. In the repository: **Settings → Pages → Build and deployment → Source →
   Deploy from a branch**, branch `main`, folder `/ (root)`. Save.
4. Wait a minute or two, then open `https://<username>.github.io`.

A custom domain (e.g. `omerbobrowski.com`) can be added under the same
Settings → Pages screen.

### Previewing before you upload

Open `index.html` in a browser — everything works from the local filesystem.
For a closer match to the hosted version, serve the folder:

```bash
python3 -m http.server 8000     # then visit http://localhost:8000
```

---

## The banner photographs

Every page opens on one of your photographs, the way the old site did. They are
already in `images/`, resized to 2200px wide and compressed for the web (the
originals you sent were 4000–5000px and several megabytes each):

| File | Page | Photograph |
|---|---|---|
| `banner-home.jpg` | Home | the street mural |
| `banner-publications.jpg` | Publications | the coloured pencils |
| `banner-teaching.jpg` | Teaching | hands on the alphabet board |
| `banner-talks.jpg` | Talks | the glow sticks |
| `banner-group.jpg` | Group | the jelly beans |
| `banner-contact.jpg` | Contact | the subway letters |
| `banner-sculpture.jpg` | *unused* | the wire sculpture |

The wire sculpture is in the folder but not on any page — there were seven photographs
and six pages. To use them somewhere, change that page's one banner line:

```html
<div class="banner-base pagebanner" style="background-image:url('images/banner-sculpture.jpg')">
```

Any wide landscape image works; roughly 2200×1000 is the right shape. A scrim
darkens the bottom-left of each banner so white type stays legible over a busy
picture — if a new photograph fights the text, adjust `.pagebanner::after` in
`css/style.css`.

**One note on paths.** Write the image path directly in `background-image`, as
above, not through a CSS custom property. A `url()` inside a custom property
resolves relative to the stylesheet (`css/`) rather than the page, which makes
the image silently 404.

---

## What still needs your input

| Item | Where | What to do |
|---|---|---|
| **Grants** | `index.html`, section marked `GRANTS` | Fill in the real entries, or delete the whole `<section>`. The placeholders use `⟨angle brackets⟩` so they are impossible to miss. |
| **CV** | `index.html` | Add `cv.pdf` to this folder and uncomment the CV chip in the hero. |
| **Course links** | `teaching.html` | The old site linked each course to its page; those URLs weren't recoverable. Add them back as `<a>` tags if you still have them. |
| **Group links** | `group.html` | Qiquan Wang, Shaked Meirom and Lior Aloni have no page I could find. Yohai Reani links to his ORCID for want of a homepage. |
| **Talks** | `talks.html` | Only one talk carried over from the old site. Copy the `<div class="talk">` block to add more. |
| **ORCID** | `index.html`, `contact.html` | Not on the old site. Add a chip alongside the other profile links if you want it. |
| **Canonical URL** | `index.html` | `<link rel="canonical">` currently guesses `obobrowski.github.io`. Update once you know the real address. |

### Worth checking

- **Publication [25]**, *Functional Central Limit Theorems …* — the old site's
  journal link pointed at a temporary submission file. Replaced with the DOI
  `10.1214/22-AAP1912`; check it resolves to the right article.

---

## Editing

Everything is hand-editable static HTML. The pieces:

```
index.html          home: intro, research areas, selected papers, grants, education
publications.html   full list, with live search and year filter
teaching.html       courses by year
talks.html          talks and slides
group.html          current members and alumni
contact.html        addresses and profile links
css/style.css       all styling; the colour and type tokens live in :root at the top
js/main.js          mobile menu + publication filtering (the site works without it)
images/             the banner photographs, portrait, favicon
tools/              optional helper scripts, not needed to run the site
```

**Adding a publication.** Copy an existing `<article class="pub">` block in
`publications.html` and edit it. Keep the `data-year` attribute accurate — the
year filter is built from it. The `data-search` attribute is what the search box
matches against; if you leave it off, the visible text is used instead.

Alternatively, run `python3 tools/build_pubs.py` from this folder after editing
the `PUBS` lists at the top of that file, and `publications.html` is regenerated.
Using it is entirely optional.

**Changing the colours.** Edit the custom properties in `:root` at the top of
`css/style.css`. The accent colour appears in one place (`--accent`) and
propagates everywhere; `--gold-bright` is the rule that sits over the banners.
There is no dark palette to keep in sync.

**Adding a page.** Copy `talks.html`, change the title, the `aria-current="page"`
attribute in the nav, and the content. Then add a link to the nav on every
other page.

---

## Notes

- Works without JavaScript; the filter and mobile menu are progressive enhancements.
- Light only. The site does not follow the visitor's system theme, so it looks
  the same for everyone whether or not they use dark mode.
- Accessible: skip link, visible focus rings, semantic headings, labelled controls.
- Prints cleanly — the publication list makes a usable PDF straight from the browser.
- `.nojekyll` tells GitHub Pages to serve the files as-is rather than running
  Jekyll over them. Leave it in place.
