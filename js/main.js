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
