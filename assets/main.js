// Przełącznik "Oryginał / Po anonimizacji" w przykładzie umowy
(function () {
  var buttons = document.querySelectorAll('.toggle button[data-view]');
  var panels = document.querySelectorAll('[data-panel]');
  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var view = btn.getAttribute('data-view');
      buttons.forEach(function (b) {
        b.setAttribute('aria-pressed', b === btn ? 'true' : 'false');
      });
      panels.forEach(function (p) {
        p.hidden = p.getAttribute('data-panel') !== view;
      });
    });
  });

  // Aktualny rok w stopce
  var year = document.querySelector('[data-year]');
  if (year) year.textContent = new Date().getFullYear();
})();
