#!/usr/bin/env python3
"""Generate publications.html from the list below.

Edit PUBS, re-run `python3 build_pubs.py`, done. Or just edit publications.html
directly - it is plain static HTML with no build step required.
"""
import html

# (id, title, authors, venue, year, [(label, url), ...])
PREPRINTS = [
    (37, "A Universal Law of Large Numbers for Extreme Cycles in Random Čech Complexes",
     "*O. Bobrowski* and P. Skraba", "Preprint", "2026",
     [("arXiv", "https://arxiv.org/abs/2609.19474")]),
    (36, "Universal Topological Statistics on Triangulated Singular Spaces",
     "U. Lim, *O. Bobrowski*, and P. Skraba", "Preprint", "2026",
     [("arXiv", "https://arxiv.org/abs/2607.27535")]),
    (35, "A Universal Nearest-Neighbor Estimator for Intrinsic Dimensionality",
     "E.-J. Ong, *O. Bobrowski*, G. Reinert, and P. Skraba", "Preprint", "2026",
     [("arXiv", "https://arxiv.org/abs/2603.10493")]),
    (34, "Sharp Phase Transition for the Formation of Infinite Tubes",
     "S. Kanazawa, *O. Bobrowski*, and P. Skraba", "Preprint", "2026",
     [("arXiv", "https://arxiv.org/abs/2605.14910")]),
    (33, "Sharp Phase Transitions for k-Fold Coverage Using Morse Theory",
     "Y. Reani and *O. Bobrowski*", "Preprint", "2025",
     [("arXiv", "https://arxiv.org/abs/2510.20329")]),
]

PAPERS = [
    (32, "Universality in Random Persistent Homology and Scale-Invariant Functionals",
     "*O. Bobrowski* and P. Skraba",
     "Communications of the AMS 6, 378–423", "2026",
     [("Journal", "https://pubs.ams.org/CAMS/2026-06-11/S2692-3688-2026-00069-0"),
      ("arXiv", "https://arxiv.org/abs/2406.05553")]),
    (31, "Functional Limit Theorems for Local Functionals of Dynamic Point Processes",
     "E. Onaran, *O. Bobrowski*, and R. Adler",
     "Electronic Journal of Probability 31, 1–31", "2026",
     [("Journal", "https://projecteuclid.org/journals/electronic-journal-of-probability/volume-31/issue-none/Central-limit-theorems-for-local-functionals-of-dynamic-point-processes/10.1214/26-EJP1496.full"),
      ("arXiv", "https://arxiv.org/abs/2310.17775")]),
    (30, "Morse Theory for the k-NN Distance Function",
     "Y. Reani and *O. Bobrowski*",
     "Discrete &amp; Computational Geometry 75(2), 491–510", "2025",
     [("Journal", "https://link.springer.com/article/10.1007/s00454-025-00795-6"),
      ("arXiv", "https://arxiv.org/abs/2403.12792")]),
    (29, "Morse Theory for the k-NN Distance Function",
     "Y. Reani and *O. Bobrowski*",
     "40th International Symposium on Computational Geometry (SoCG)", "2024",
     [("Proceedings", "https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2024.75"),
      ("arXiv", "https://arxiv.org/abs/2403.12792")]),
    (28, "Cluster-Persistence for Weighted Graphs",
     "*O. Bobrowski* and P. Skraba",
     "Entropy 25(12), 1587", "2023",
     [("Journal", "https://www.mdpi.com/1099-4300/25/12/1587"),
      ("arXiv", "https://arxiv.org/abs/2310.00350")]),
    (27, "A Coupled Alpha Complex",
     "Y. Reani and *O. Bobrowski*",
     "Journal of Computational Geometry 14(1), 221–256", "2023",
     [("Journal", "https://jocg.org/index.php/jocg/article/view/4100/3371"),
      ("arXiv", "https://arxiv.org/abs/2105.08113")]),
    (26, "A Universal Null-Distribution for Topological Data Analysis",
     "*O. Bobrowski* and P. Skraba",
     "Scientific Reports 13(1), 12274", "2023",
     [("Journal", "https://www.nature.com/articles/s41598-023-37842-2"),
      ("arXiv", "https://arxiv.org/abs/2207.03926")]),
    (25, "Functional Central Limit Theorems for Local Statistics of Spatial Birth–Death "
         "Processes in the Thermodynamic Regime",
     "E. Onaran, *O. Bobrowski*, and R. Adler",
     "The Annals of Applied Probability 33(5), 3958–3986", "2023",
     [("Journal", "https://doi.org/10.1214/22-AAP1912"),
      ("arXiv", "https://arxiv.org/abs/2202.02766")]),
    (24, "Cycle Registration in Persistent Homology with Applications in Topological Bootstrap",
     "Y. Reani and *O. Bobrowski*",
     "IEEE Transactions on Pattern Analysis and Machine Intelligence 45(5), 5579–5593", "2023",
     [("Journal", "https://ieeexplore.ieee.org/abstract/document/9931659"),
      ("arXiv", "https://arxiv.org/abs/2101.00698")]),
    (23, "Poisson Process Approximation Under Stabilization and Palm Coupling",
     "*O. Bobrowski*, M. Schulte, and D. Yogeshwaran",
     "Annales Henri Lebesgue 5, 1489–1534", "2022",
     [("Journal", "https://ahl.centre-mersenne.org/articles/10.5802/ahl.156/"),
      ("arXiv", "https://arxiv.org/abs/2104.13261")]),
    (22, "Homological Connectivity in Random Čech Complexes",
     "*O. Bobrowski*",
     "Probability Theory and Related Fields 183(3–4), 715–788", "2022",
     [("Journal", "https://link.springer.com/article/10.1007/s00440-022-01149-6"),
      ("arXiv", "https://arxiv.org/abs/1906.04861")]),
    (21, "Unsupervised Geometric and Topological Approaches for Cross-Lingual Sentence "
         "Representation and Comparison",
     "S. H. Meirom and *O. Bobrowski*",
     "Proceedings of the 7th Workshop on Representation Learning for NLP, 173–183", "2022",
     [("Proceedings", "https://aclanthology.org/2022.repl4nlp-1.18/")]),
    (20, "Alarm Sound Detection Using Topological Signal Processing",
     "T. Fireaizen, S. Ron, and *O. Bobrowski*",
     "IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)", "2022",
     [("Proceedings", "https://ieeexplore.ieee.org/abstract/document/9747228")]),
    (19, "On the Spectrum of Dense Random Geometric Graphs",
     "K. Adhikari, R. Adler, *O. Bobrowski*, and R. Rosenthal",
     "The Annals of Applied Probability 32(3), 1734–1773", "2022",
     [("Journal", "https://projecteuclid.org/journals/annals-of-applied-probability/volume-32/issue-3/On-the-spectrum-of-dense-random-geometric-graphs/10.1214/21-AAP1720.short"),
      ("arXiv", "https://arxiv.org/abs/2004.04967")]),
    (18, "Random Simplicial Complexes: Models and Phenomena",
     "*O. Bobrowski* and D. Krioukov",
     "Book chapter, Higher-Order Systems, 59–96, Springer", "2022",
     [("Chapter", "https://link.springer.com/chapter/10.1007/978-3-030-91374-8_2"),
      ("arXiv", "https://arxiv.org/abs/2105.12914")]),
    (17, "Homological Percolation: The Formation of Giant k-Cycles",
     "*O. Bobrowski* and P. Skraba",
     "International Mathematics Research Notices 2022(8), 6186–6213", "2022",
     [("Journal", "https://doi.org/10.1093/imrn/rnaa305"),
      ("arXiv", "https://arxiv.org/abs/2005.14011")]),
    (16, "Joint Geometric and Topological Analysis of Hierarchical Datasets",
     "L. Aloni, *O. Bobrowski*, and R. Talmon",
     "Joint European Conference on Machine Learning and Knowledge Discovery in Databases "
     "(ECML PKDD), 478–493", "2021",
     [("Proceedings", "https://link.springer.com/chapter/10.1007/978-3-030-86523-8_29"),
      ("arXiv", "https://arxiv.org/abs/2104.01395")]),
    (15, "Probabilistic Convergence and Stability of Random Mapper Graphs",
     "A. Brown, *O. Bobrowski*, E. Munch, and B. Wang",
     "Journal of Applied and Computational Topology 5, 99–140", "2021",
     [("Journal", "https://link.springer.com/article/10.1007/s41468-020-00063-x"),
      ("arXiv", "https://arxiv.org/abs/1909.03488")]),
    (14, "Convergence of Persistence Diagrams for Topological Crackle",
     "T. Owada and *O. Bobrowski*",
     "Bernoulli 26(3), 2275–2310", "2020",
     [("Journal", "https://doi.org/10.3150/20-BEJ1193"),
      ("arXiv", "https://arxiv.org/abs/1810.01602")]),
    (13, "Homological Percolation and the Euler Characteristic",
     "*O. Bobrowski* and P. Skraba",
     "Physical Review E 101, 032404:1–16", "2020",
     [("Journal", "https://journals.aps.org/pre/abstract/10.1103/PhysRevE.101.032304"),
      ("arXiv", "https://arxiv.org/abs/1910.10146")]),
    (12, "Random Čech Complexes on Riemannian Manifolds",
     "*O. Bobrowski* and G. Oliveira",
     "Random Structures &amp; Algorithms 54(3), 373–412", "2019",
     [("Journal", "https://onlinelibrary.wiley.com/doi/10.1002/rsa.20800"),
      ("arXiv", "https://arxiv.org/abs/1704.07204")]),
    (11, "Topology of Random Geometric Complexes: A Survey",
     "*O. Bobrowski* and M. Kahle",
     "Journal of Applied and Computational Topology 1(3–4), 331–364", "2018",
     [("Journal", "https://link.springer.com/article/10.1007/s41468-017-0010-0"),
      ("arXiv", "https://arxiv.org/abs/1409.4734")]),
    (10, "Maximally Persistent Cycles in Random Geometric Complexes",
     "*O. Bobrowski*, M. Kahle, and P. Skraba",
     "The Annals of Applied Probability 27(4), 2032–2060", "2017",
     [("Journal", "https://projecteuclid.org/euclid.aoap/1504080025"),
      ("arXiv", "https://arxiv.org/abs/1509.04347")]),
    (9, "On the Vanishing of Homology in Random Čech Complexes",
     "*O. Bobrowski* and S. Weinberger",
     "Random Structures &amp; Algorithms 51(1), 14–51", "2017",
     [("Journal", "https://onlinelibrary.wiley.com/doi/10.1002/rsa.20697"),
      ("arXiv", "https://arxiv.org/abs/1507.06945")]),
    (8, "Topological Consistency via Kernel Estimation",
     "*O. Bobrowski*, S. Mukherjee, and J. Taylor",
     "Bernoulli 23(1), 288–328", "2017",
     [("Journal", "https://projecteuclid.org/euclid.bj/1475001356"),
      ("arXiv", "https://arxiv.org/abs/1407.5272")]),
    (7, "The Topology of Probability Distributions on Manifolds",
     "*O. Bobrowski* and S. Mukherjee",
     "Probability Theory and Related Fields 161(3–4), 651–686", "2015",
     [("Journal", "https://link.springer.com/article/10.1007/s00440-014-0556-x"),
      ("arXiv", "https://arxiv.org/abs/1307.1123")]),
    (6, "Crackle: The Homology of Noise",
     "R. J. Adler, *O. Bobrowski*, and S. Weinberger",
     "Discrete &amp; Computational Geometry 52(4), 680–704", "2014",
     [("Journal", "https://link.springer.com/article/10.1007/s00454-014-9621-6"),
      ("arXiv", "https://arxiv.org/abs/1301.1466")]),
    (5, "Distance Functions, Critical Points and the Topology of Random Čech Complexes",
     "*O. Bobrowski* and R. J. Adler",
     "Homology, Homotopy and Applications 16(2), 311–344", "2014",
     [("Journal", "https://intlpress.com/site/pub/files/_fulltext/journals/hha/2014/0016/0002/HHA-2014-0016-0002-a018.pdf"),
      ("arXiv", "https://arxiv.org/abs/1107.4775")]),
    (4, "Euler Integration of Gaussian Random Fields and Persistent Homology",
     "*O. Bobrowski* and M. S. Borman",
     "Journal of Topology and Analysis 4(01), 49–70", "2012",
     [("Journal", "https://www.worldscientific.com/doi/abs/10.1142/S1793525312500057"),
      ("arXiv", "https://arxiv.org/abs/1003.5175")]),
    (3, "Persistent Homology for Random Fields and Complexes",
     "R. J. Adler, *O. Bobrowski*, M. S. Borman, E. Subag, and S. Weinberger",
     "IMS Collections 6, 124–143", "2010",
     [("Journal", "https://projecteuclid.org/euclid.imsc/1288099016"),
      ("arXiv", "https://arxiv.org/abs/1003.1001")]),
    (2, "Bayesian Filtering in Spiking Neural Networks: Noise, Adaptation and "
        "Multisensory Integration",
     "*O. Bobrowski*, R. Meir, and Y. C. Eldar",
     "Neural Computation 21(5), 1277–1320", "2009",
     [("Journal", "https://doi.org/10.1162/neco.2008.01-08-692")]),
    (1, "A Neural Network Implementing Optimal State Estimation Based on Dynamic "
        "Spike Train Decoding",
     "*O. Bobrowski*, R. Meir, S. Shoham, and Y. C. Eldar",
     "Advances in Neural Information Processing Systems (NIPS) 20, 145–152", "2007",
     [("Proceedings", "http://papers.nips.cc/paper/3299-a-neural-network-implementing-optimal-state-estimation-based-on-dynamic-spike-train-decoding.pdf")]),
]


def authors_html(s):
    """*Name* -> bold 'me' span."""
    out, bold = [], False
    for part in s.split("*"):
        out.append(f'<span class="me">{part}</span>' if bold else part)
        bold = not bold
    return "".join(out)


def entry(p):
    pid, title, authors, venue, year, links = p
    plain = html.unescape(f"{title} {authors.replace('*', '')} {venue} {year}")
    link_html = "".join(
        f'\n            <a href="{u}">{l}</a>' for l, u in links)
    return f"""        <article class="pub" data-year="{year}" data-search="{html.escape(plain, quote=True)}">
          <div class="pub-id">[{pid}]</div>
          <div>
            <h3 class="pub-title">{title}</h3>
            <div class="pub-authors">{authors_html(authors)}</div>
            <div class="pub-venue">{venue}, <span class="year">{year}</span></div>
            <div class="pub-links">{link_html}
            </div>
          </div>
        </article>
"""


HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Publications · Omer Bobrowski</title>
<meta name="description" content="Publications and preprints of Omer Bobrowski on stochastic topology, applied topology and probability.">
<link rel="icon" href="images/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;450;500;550;600;650;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html">Omer Bobrowski <span>· <bdi>עומר בוברובסקי</bdi></span></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Menu">☰</button>
    <nav class="nav" id="nav">
      <a href="index.html">Home</a>
      <a href="publications.html" aria-current="page">Publications</a>
      <a href="teaching.html">Teaching</a>
      <a href="talks.html">Talks</a>
      <a href="group.html">Group</a>
      <a href="contact.html">Contact</a>
    </nav>
  </div>
</header>

<div class="banner-base pagebanner" style="background-image:url('images/banner-publications.jpg')">
  <div class="wrap">
    <div class="banner-rule"></div>
    <h1>Publications</h1>
    <p>Preprints and published work, also listed on Google Scholar, arXiv and MathSciNet.</p>
  </div>
</div>

<main id="main">
  <section>
    <div class="wrap">
      <p class="muted" style="margin-bottom:1.5rem">Profiles:
        <a href="https://scholar.google.com/citations?user=RbVVVnQAAAAJ&amp;hl=en">Google Scholar</a> ·
        <a href="https://arxiv.org/a/bobrowski_o_1">arXiv</a> ·
        <a href="https://mathscinet.ams.org/mathscinet/MRAuthorID/869190">MathSciNet</a></p>

      <div class="filters">
        <input type="search" id="pub-search" placeholder="Search title, author or venue…" aria-label="Search publications">
        <select id="pub-year" aria-label="Filter by year"><option value="">All years</option></select>
        <span id="pub-count"></span>
      </div>
"""

FOOT = """
    </div>
  </section>
</main>

<footer class="site-footer">
  <div class="wrap">
    <div>© <span id="year">2026</span> Omer Bobrowski · School of Mathematical Sciences, Queen Mary University of London</div>
    <nav class="footer-links">
      <a href="index.html">Home</a>
      <a href="teaching.html">Teaching</a>
      <a href="group.html">Group</a>
      <a href="contact.html">Contact</a>
    </nav>
  </div>
</footer>

<script src="js/main.js"></script>
<script>document.getElementById('year').textContent = new Date().getFullYear();</script>
</body>
</html>
"""

parts = [HEAD]
parts.append('      <div class="pub-group">\n        <h2>Preprints</h2>\n')
parts += [entry(p) for p in PREPRINTS]
parts.append("      </div>\n\n")
parts.append('      <div class="pub-group">\n        <h2>Published papers</h2>\n')
parts += [entry(p) for p in PAPERS]
parts.append("      </div>\n")
parts.append(FOOT)

with open("publications.html", "w", encoding="utf-8") as f:
    f.write("".join(parts))

print(f"publications.html written — {len(PREPRINTS) + len(PAPERS)} entries")
