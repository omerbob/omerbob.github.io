/* Mobile navigation ------------------------------------------------------- */
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.nav');
  if (!toggle || !nav) return;

  toggle.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  nav.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') {
      nav.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    }
  });
})();

/* Publication filtering ---------------------------------------------------- */
(function () {
  var search = document.getElementById('pub-search');
  var yearSel = document.getElementById('pub-year');
  if (!search && !yearSel) return;

  var pubs = Array.prototype.slice.call(document.querySelectorAll('.pub'));
  var groups = Array.prototype.slice.call(document.querySelectorAll('.pub-group'));
  var counter = document.getElementById('pub-count');
  var total = pubs.length;

  // Populate the year dropdown from the data actually on the page.
  if (yearSel) {
    var years = {};
    pubs.forEach(function (p) {
      var y = p.getAttribute('data-year');
      if (y) years[y] = true;
    });
    Object.keys(years).sort().reverse().forEach(function (y) {
      var opt = document.createElement('option');
      opt.value = y;
      opt.textContent = y;
      yearSel.appendChild(opt);
    });
  }

  function apply() {
    var q = (search ? search.value : '').trim().toLowerCase();
    var year = yearSel ? yearSel.value : '';
    var shown = 0;

    pubs.forEach(function (p) {
      var hay = (p.getAttribute('data-search') || p.textContent).toLowerCase();
      var okText = !q || hay.indexOf(q) !== -1;
      var okYear = !year || p.getAttribute('data-year') === year;
      var visible = okText && okYear;
      p.hidden = !visible;
      if (visible) shown++;
    });

    // Hide a section heading when everything under it is filtered out.
    groups.forEach(function (g) {
      var any = g.querySelector('.pub:not([hidden])');
      g.hidden = !any;
    });

    if (counter) {
      counter.textContent = shown === total
        ? total + ' publications'
        : shown + ' of ' + total;
    }
  }

  if (search) search.addEventListener('input', apply);
  if (yearSel) yearSel.addEventListener('change', apply);
  apply();
})();

/* Shrinking banner --------------------------------------------------------
   The banner starts at its full CSS height and, as the page scrolls, gives
   up height one pixel at a time until it is just tall enough to hold its
   title; from there it holds still and the page scrolls on beneath it. It is
   taken out of the flow and a spacer of the original height put in its place,
   so shrinking never shifts the content below.
   ------------------------------------------------------------------------ */
(function () {
  var banner = document.querySelector('.pagebanner');
  var header = document.querySelector('.site-header');
  if (!banner || !header || !window.requestAnimationFrame) return;

  var wrap = banner.querySelector('.wrap');
  var spacer = document.createElement('div');
  spacer.className = 'banner-spacer';
  banner.parentNode.insertBefore(spacer, banner);

  var maxH, minH, ticking = false;
  // Room left around the title once the banner is fully collapsed. The rule
  // under the title already carries space of its own, so the top is tighter
  // than the bottom.
  var PAD_TOP = 8;
  var PAD_BOTTOM = 18;
  var MAX_VEIL = 0.5;       // how far the photograph lightens once collapsed

  function measure() {
    // Measured with the pinning switched off, so the numbers are the ones the
    // stylesheet asks for: the full height, and a floor of the title plus the
    // padding either side of it.
    var root = document.documentElement;
    root.classList.remove('has-shrink-banner');
    banner.style.height = '';
    banner.style.removeProperty('--veil');
    wrap.style.paddingTop = '';
    wrap.style.paddingBottom = '';
    maxH = banner.offsetHeight;
    var title = banner.querySelector('h1, .banner-title');
    wrap.style.paddingTop = PAD_TOP + 'px';
    wrap.style.paddingBottom = PAD_BOTTOM + 'px';
    minH = Math.ceil((title ? title.offsetHeight : wrap.scrollHeight) + PAD_TOP + PAD_BOTTOM);
    if (minH > maxH) minH = maxH;
    spacer.style.height = maxH + 'px';
    banner.style.top = header.offsetHeight + 'px';
    root.classList.add('has-shrink-banner');
    update();
  }

  function update() {
    var h = maxH - (window.pageYOffset || document.documentElement.scrollTop);
    if (h > maxH) h = maxH;
    if (h < minH) h = minH;
    banner.style.height = h + 'px';
    // Lighten the picture in step with the shrinking; the title is untouched.
    var travel = maxH - minH;
    var done = travel > 0 ? (maxH - h) / travel : 0;
    banner.style.setProperty('--veil', MAX_VEIL * done);
    ticking = false;
  }

  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(update);
  }

  measure();
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', measure);
  window.addEventListener('load', measure);
  // Web fonts change how tall the title is, so measure again once they land.
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(measure);
})();
