(function () {
  var slides = Array.prototype.slice.call(document.querySelectorAll('.hs-slide'));
  if (slides.length < 2) return;
  var dotsBox = document.querySelector('.hs-dots'), cur = 0, timer = null, dots = [];
  function mk(txt, cls, label) { var b = document.createElement('button'); b.type = 'button'; b.className = cls; b.textContent = txt; b.setAttribute('aria-label', label); return b; }
  var prevS = mk('\u2039', 'hs-sm', 'Poprzedni slajd');
  dotsBox.appendChild(prevS);
  slides.forEach(function (s, i) {
    var d = mk('', '', 'Slajd ' + (i + 1)); d.setAttribute('role', 'tab');
    d.addEventListener('click', function () { go(i, true); });
    dotsBox.appendChild(d); dots.push(d);
  });
  var nextS = mk('\u203a', 'hs-sm', 'Następny slajd');
  dotsBox.appendChild(nextS);
  function go(i, user) {
    cur = (i + slides.length) % slides.length;
    slides.forEach(function (s, k) { s.classList.toggle('is-active', k === cur); s.setAttribute('aria-hidden', k === cur ? 'false' : 'true'); });
    dots.forEach(function (d, k) { d.setAttribute('aria-selected', k === cur ? 'true' : 'false'); });
    if (user) stop();
  }
  function stop() { clearInterval(timer); timer = null; }
  document.querySelector('.hs-prev').addEventListener('click', function () { go(cur - 1, true); });
  document.querySelector('.hs-next').addEventListener('click', function () { go(cur + 1, true); });
  prevS.addEventListener('click', function () { go(cur - 1, true); });
  nextS.addEventListener('click', function () { go(cur + 1, true); });
  var box = document.querySelector('.hero-slider');
  box.addEventListener('keydown', function (e) { if (e.key === 'ArrowLeft') go(cur - 1, true); else if (e.key === 'ArrowRight') go(cur + 1, true); });
  var tx = null;
  box.addEventListener('touchstart', function (e) { tx = e.touches[0].clientX; }, { passive: true });
  box.addEventListener('touchend', function (e) { if (tx === null) return; var dx = e.changedTouches[0].clientX - tx; tx = null; if (Math.abs(dx) > 50) go(cur + (dx < 0 ? 1 : -1), true); });
  go(0, false);
})();

(function () {
  var box = document.querySelector('.for-slider'); if (!box) return;
  var list = box.querySelector('.for-list'), prev = box.querySelector('.for-prev'), next = box.querySelector('.for-next');
  function upd() { prev.disabled = list.scrollLeft < 4; next.disabled = list.scrollLeft + list.clientWidth >= list.scrollWidth - 4; }
  prev.addEventListener('click', function () { list.scrollBy({ left: -list.clientWidth, behavior: 'smooth' }); });
  next.addEventListener('click', function () { list.scrollBy({ left: list.clientWidth, behavior: 'smooth' }); });
  list.addEventListener('scroll', upd, { passive: true }); window.addEventListener('resize', upd); upd();
})();
