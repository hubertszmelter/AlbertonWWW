// Rok w stopce
(function () {
  var year = document.querySelector('[data-year]');
  if (year) year.textContent = new Date().getFullYear();
})();

// Otwórz pytanie z FAQ, gdy adres wskazuje na nie (#q-…)
(function () {
  function openFromHash() {
    var id = decodeURIComponent(location.hash.slice(1));
    var el = id && document.getElementById(id);
    if (el && el.tagName === 'DETAILS') { el.open = true; el.scrollIntoView(); }
  }
  window.addEventListener('hashchange', openFromHash);
  openFromHash();
})();
