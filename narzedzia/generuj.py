"""Generator wspólnych elementów stron Albertona (wersja 3). Uruchom: python3 narzedzia/generuj.py .  (z katalogu repozytorium)"""
import sys, pathlib, re

REPO = pathlib.Path(sys.argv[1])

# Znak z programu Alberton: szare „A” i niebieska poprzeczka.
LOGO = ('<svg width="30" height="30" viewBox="3 2 38 38" fill="none" aria-hidden="true">'
        '<path d="M4.75 37L16.25 5H24.75L30.75 22.25H24.25L20.5 12L10.75 37Z" fill="{g}"/><path d="M27.25 30H33.75L36 37H29.5Z" fill="{g}"/><rect x="18" y="24" width="22" height="4.75" fill="#5AB0F5"/></svg>')

NAV = [("Jak działa", "/#jak-dziala", "home"), ("Dlaczego my?", "/dlaczego-my/", "why"),
       ("Cennik", "/#cennik", "home"), ("Poradnik", "/poradnik/", "blog"), ("FAQ", "/#faq", "home")]

def ph(t):
    return f'<span class="ph">[{t}]</span>'

def head(title, desc, path, extra="", noindex=False):
    url = "https://alberton.pl" + path
    robots = '\n<meta name="robots" content="noindex">' if noindex else ""
    return f'''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">{robots}
<meta name="theme-color" content="#13233F">
<link rel="canonical" href="{url}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">

<meta property="og:type" content="website">
<meta property="og:locale" content="pl_PL">
<meta property="og:site_name" content="Alberton">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://alberton.pl/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Alberton — wklejaj umowy do AI bez danych klientów">
<meta name="twitter:card" content="summary_large_image">

<link rel="preload" href="/assets/fonts/ibm-plex-sans-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/ibm-plex-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/styles.css">
{extra}</head>
<body>
<a class="skip-link" href="#tresc">Przejdź do treści</a>
'''

def header(active):
    links = "\n".join(
        f'      <a class="nav-link" href="{h}"{" aria-current=\"page\"" if a == active and a != "home" else ""}>{t}</a>'
        for t, h, a in NAV)
    return f'''
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="/" aria-label="Alberton — strona główna">
      {LOGO.format(g="#B2B9C2")}
      <span>Alberton</span>
    </a>
    <nav class="main-nav" aria-label="Główna nawigacja">
{links}
    </nav>
    <div class="nav-actions">
      <a class="btn btn-primary btn-sm" href="/prezentacja/">Umów prezentację</a>
    </div>
  </div>
</header>
'''

FAQ_BAR = '''
<section class="faq-bar" aria-label="Najczęstsze pytania">
  <div class="wrap">
    <span class="label">Najczęstsze pytania</span>
    <a href="/#q-internet">Czy dokumenty trafiają do internetu?</a>
    <a href="/#q-rodo">Anonimizacja czy pseudonimizacja?</a>
    <a href="/#q-dane">Jakie dane rozpoznaje?</a>
    <a href="/#q-cena">Ile kosztuje?</a>
    <a href="/#q-wymagania">Wymagania systemowe</a>
    <a href="/#faq">Wszystkie pytania →</a>
  </div>
</section>
'''

FOOTER = f'''
<footer class="site-footer">
  <div class="wrap footer-cols">
    <div class="footer-col footer-company">
      <span class="footer-logo">{LOGO.format(g="#B2B9C2")}Alberton</span>
      <span>{ph("Nazwa spółki")} sp. z o.o., {ph("adres siedziby")}<br>
      Sąd rejestrowy: {ph("nazwa sądu")}, KRS {ph("numer")}<br>
      NIP {ph("numer")}, REGON {ph("numer")}, kapitał zakładowy {ph("kwota")}&nbsp;zł</span>
    </div>
    <nav class="footer-col footer-nav" aria-label="Stopka">
      <a href="/dlaczego-my/">Dlaczego my?</a>
      <a href="/prezentacja/">Umów prezentację</a>
      <a href="/poradnik/">Poradnik</a>
      <a href="/#cennik">Cennik</a>
    </nav>
    <nav class="footer-col footer-nav" aria-label="Dokumenty">
      <a href="#">Polityka prywatności</a>
      <a href="#">Regulamin</a>
      <a href="/dlaczego-my/#zgloszenia">Zgłaszanie podatności</a>
    </nav>
    <div class="footer-col footer-nav">
      <a href="#">Kontakt: {ph("adres e-mail")}</a>
      <a href="#">LinkedIn</a>
      <span>© <span data-year>2026</span> Alberton</span>
    </div>
  </div>
</footer>

<script src="/assets/main.js" defer></script>
</body>
</html>
'''

def page(path, title, desc, active, main, extra="", noindex=False):
    out = REPO / path.strip("/") / "index.html" if path != "/" else REPO / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(head(title, desc, path, extra, noindex) + header(active)
                   + '\n<main id="tresc">\n' + main + '\n</main>\n' + FAQ_BAR + FOOTER, encoding="utf-8")

# ---------------------------------------------------------------- Strona główna
HOME_LD = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Alberton",
  "url": "https://alberton.pl/",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Windows, macOS",
  "description": "Aplikacja desktopowa do anonimizacji umów i dokumentów przed wklejeniem ich do narzędzi AI. Działa offline.",
  "inLanguage": ["pl", "en"]
}
</script>
'''

home = f'''
  <section class="hero-bg" aria-labelledby="hero-title">
  <div class="wrap hero">
    <div class="hero-copy">
      <p class="eyebrow">Dla kancelarii i działów prawnych</p>
      <h1 id="hero-title">Wklejaj umowy do AI bez danych klientów</h1>
      <p class="lead">Alberton zamienia nazwiska, numery PESEL, adresy i numery rachunków na znaczniki, zanim tekst opuści Twój komputer. Działa offline, z dokumentami po polsku i angielsku.</p>
      <div class="actions">
        <a class="btn btn-primary" href="/prezentacja/">Umów bezpłatną prezentację (20 min)</a>
      </div>
      <p class="hero-note">Windows i macOS</p>
    </div>

    <div class="hero-demo">
      <img class="hero-shot" src="/assets/aplikacja.webp" width="2000" height="1231" alt="Okno aplikacji Alberton z zanonimizowaną umową o roboty budowlane: dane w tekście zastąpione kolorowymi znacznikami, takimi jak [FIRMA_1], [ADRES_1] i [OSOBA_1]">
    </div>
  </div>
  </section>

  <section class="strip" aria-label="W skrócie">
    <ul class="wrap">
      <li>Działa w pełni offline</li>
      <li>Dokumenty nie trafiają na żadne serwery</li>
      <li>Windows i macOS</li>
      <li>Polski i angielski</li>
    </ul>
  </section>

  <section id="jak-dziala" class="wrap section" aria-labelledby="how-title">
    <div class="section-head">
      <h2 id="how-title" class="h2">Trzy kroki, zanim tekst trafi do czatu</h2>
      <p class="muted">Alberton nie łączy się z żadnym czatem AI. Przygotowuje tekst, a Ty decydujesz, gdzie go wkleić.</p>
    </div>
    <ol class="steps">
      <li>
        <span class="num" aria-hidden="true">[01]</span>
        <h3>Otwierasz dokument</h3>
        <p>Wklejasz tekst albo otwierasz plik umowy, pisma lub notatki ({ph("FORMATY: .docx, .pdf…")}). Alberton obsługuje dokumenty po polsku i angielsku.</p>
      </li>
      <li>
        <span class="num" aria-hidden="true">[02]</span>
        <h3>Sprawdzasz znaczniki</h3>
        <p>Dane osobowe i identyfikatory zmieniają się w znaczniki, takie jak <span class="tag">[OSOBA_1]</span> czy <span class="tag">[PESEL_1]</span>. Wątpliwe fragmenty są oznaczone do sprawdzenia, resztę zakryjesz ręcznie.</p>
      </li>
      <li>
        <span class="num" aria-hidden="true">[03]</span>
        <h3>Kopiujesz tekst do AI</h3>
        <p>Wklejasz zanonimizowany tekst do narzędzia, z którego korzysta Twoja kancelaria. Analiza umowy działa tak samo, tylko bez danych klientów.</p>
      </li>
    </ol>
    <div class="video-ph">{ph("Nagranie ekranu 30–45 s: otwarcie umowy, przegląd znaczników, kopiowanie")}</div>
  </section>

  <section class="band" aria-labelledby="rule-title">
    <div class="wrap section split">
      <div class="rule-copy">
        <h2 id="rule-title" class="h2">Lepiej zakryć za dużo niż za mało</h2>
        <p class="measure muted">Kiedy Alberton nie jest pewien, czy fragment to dana osobowa, zakrywa go i oznacza do sprawdzenia. Odznaczenie zbędnego znacznika zajmuje chwilę. Przeoczony numer PESEL w czacie AI to już problem.</p>
        <p class="measure muted">Masz też ręczne narzędzie do zaznaczania: nazwę spółki, sygnaturę akt czy szczegół sprawy zakryjesz sam, zanim skopiujesz tekst.</p>
      </div>
      <div class="panel">
        <p class="panel-title">Wykryte w dokumencie</p>
        <ul class="found">
          <li><span>Jan Kowalski <span class="kind">· osoba</span></span><span class="status status-done">Zakryte</span></li>
          <li><span>44051401359 <span class="kind">· PESEL</span></span><span class="status status-done">Zakryte</span></li>
          <li><span>ul. Lipowa 7/12 <span class="kind">· adres</span></span><span class="status status-done">Zakryte</span></li>
          <li><span>Wynajmujący <span class="kind">· możliwa osoba</span></span><span class="status status-check">Do sprawdzenia</span></li>
        </ul>
        <button type="button" class="btn btn-outline btn-sm">Zaznacz fragment ręcznie</button>
      </div>
    </div>
  </section>

  <section id="test-jakosci" class="wrap section" aria-labelledby="test-title">
    <div class="section-head">
      <h2 id="test-title" class="h2">Sprawdziliśmy to na polskich umowach</h2>
      <p class="muted">Publikujemy wynik testu i metodę, żeby kancelaria mogła ocenić ryzyko sama, a nie na słowo.</p>
    </div>
    <div class="grid center">
      <div class="card"><div class="stat">{ph("X")}%</div><div class="stat-label">danych osobowych wykrytych automatycznie</div></div>
      <div class="card"><div class="stat">{ph("N")}</div><div class="stat-label">dokumentów testowych: umowy, pisma, pozwy</div></div>
      <div class="card"><div class="stat">{ph("K")}</div><div class="stat-label">rozpoznawanych kategorii danych</div></div>
    </div>
    <p class="center" style="margin-top:24px"><a href="#">Zobacz metodę testu →</a> {ph("link do /test-jakosci")}</p>
  </section>

  <section id="bezpieczenstwo" class="security" aria-labelledby="sec-title">
    <div class="wrap section security-grid">
      <div class="security-copy">
        <h2 id="sec-title" class="h2">Dokumenty nie opuszczają Twojego komputera</h2>
        <p>Anonimizacja odbywa się w całości na Twoim urządzeniu. Alberton nie potrzebuje internetu, żeby działać, i nie przesyła plików na żadne serwery.</p>
        <p><a class="btn btn-primary" href="/dlaczego-my/">Bezpieczeństwo i dokumentacja</a></p>
      </div>
      <ul class="facts">
        <li>Działa w pełni offline</li>
        <li>Bez konta w chmurze i bez wysyłania dokumentów</li>
        <li>Tekst do AI wklejasz sam, więc zawsze widzisz, co wysyłasz</li>
        <li>Dokumentacja dla działu IT i inspektora ochrony danych</li>
      </ul>
    </div>
  </section>

  <section id="kancelarie" class="wrap section law" aria-labelledby="law-title">
    <h2 id="law-title" class="h2">AI w kancelarii i dziale prawnym, tajemnica na miejscu</h2>
    <div class="law-cols">
      <p>Wewnętrzna polityka zabrania wklejania danych klientów do zewnętrznych narzędzi? Alberton pozwala korzystać z AI przy przeglądzie umów, pism i korespondencji z zachowaniem tej zasady, zarówno w kancelarii, jak i w dziale prawnym firmy.</p>
      <p>Samorządy zawodowe publikują rekomendacje dotyczące korzystania z narzędzi AI. Alberton nie zastępuje ich lektury, ale ułatwia stosowanie zasady, by nie przekazywać danych klientów zewnętrznym narzędziom. {ph("odnośnik do rekomendacji KIRP")}</p>
      <p>Nie wymaga wiedzy technicznej ani własnych serwerów. Instalujesz program na komputerze i od razu pracujesz na swoich dokumentach.</p>
    </div>
  </section>

  <section id="cennik" class="band" aria-labelledby="price-title">
    <div class="wrap section">
      <div class="section-head">
        <h2 id="price-title" class="h2">Cennik</h2>
        <p class="muted">Ceny netto. Faktura VAT. {ph("okres rozliczenia")}</p>
      </div>
      <div class="grid">
        <div class="card"><h3>Stanowisko</h3><div class="price">{ph("CENA")} zł <small>netto / mies.</small></div><p>Dla prawnika, który pracuje sam.</p><a class="btn btn-outline btn-sm" href="/prezentacja/">Umów prezentację</a></div>
        <div class="card card-featured"><div class="meta">Dla zespołów</div><h3>Zespół</h3><div class="price">{ph("CENA")} zł <small>netto / stanowisko</small></div><p>Wspólne reguły zakrywania i centralne licencje. {ph("funkcje do potwierdzenia")}</p><a class="btn btn-primary btn-sm" href="/prezentacja/">Umów prezentację</a></div>
        <div class="card"><h3>Kancelaria lub firma</h3><div class="price">Wycena</div><p>Wdrożenie przez dział IT, faktura roczna, umowa licencyjna.</p><a class="btn btn-outline btn-sm" href="/prezentacja/">Umów prezentację</a></div>
      </div>
    </div>
  </section>

  <section id="faq" class="wrap section" aria-labelledby="faq-title">
    <div class="faq">
      <h2 id="faq-title" class="h2">Częste pytania</h2>
      <div class="faq-list">
        <details id="q-internet"><summary>Czy Alberton wysyła moje dokumenty do internetu?</summary>
          <p>Nie. Program działa offline, a dokument przetwarzany jest wyłącznie na Twoim komputerze. {ph("Opisać, z czym program łączy się poza tym, np. aktywacja licencji, aktualizacje")}</p></details>
        <details id="q-rodo"><summary>Czy to anonimizacja, czy pseudonimizacja w rozumieniu RODO?</summary>
          <p>Zastąpienie danych znacznikami to zwykle pseudonimizacja, a nie anonimizacja w rozumieniu RODO. Tekst może nadal zawierać szczegóły sprawy, które pozwalają kogoś rozpoznać, dlatego przed wklejeniem warto przejrzeć znaczniki i zakryć ręcznie to, czego program nie wykrył. {ph("Doprecyzować z prawnikiem")}</p></details>
        <details id="q-dane"><summary>Jakie dane rozpoznaje i czego nie wykryje?</summary>
          <p>Między innymi imiona i nazwiska, numery PESEL, adresy i numery rachunków. Wszystko, czego nie wykryje, możesz zaznaczyć ręcznie. {ph("Pełna lista kategorii i znane ograniczenia, np. skany bez warstwy tekstu")}</p></details>
        <details id="q-przywracanie"><summary>Czy mogę przywrócić dane w odpowiedzi z AI?</summary>
          <p>{ph("Odpowiedź zależna od funkcji produktu")}</p></details>
        <details id="q-metadane"><summary>Czy program usuwa metadane i ukrytą treść pliku?</summary>
          <p>{ph("Komentarze, śledzenie zmian, właściwości dokumentu: odpowiedź zależna od funkcji produktu")}</p></details>
        <details id="q-narzedzia"><summary>Z jakimi narzędziami AI to działa?</summary>
          <p>Z każdym, do którego można wkleić tekst. Alberton nie integruje się z żadnym czatem, tylko przygotowuje bezpieczną wersję dokumentu.</p></details>
        <details id="q-jezyki"><summary>W jakich językach działa?</summary>
          <p>Obsługuje dokumenty po polsku i angielsku.</p></details>
        <details id="q-wymagania"><summary>Jakie są wymagania systemowe i czy potrzebuję administratora?</summary>
          <p>Alberton działa na Windows i macOS. {ph("Wersje systemu, uprawnienia potrzebne do instalacji")}</p></details>
        <details id="q-cena"><summary>Ile kosztuje i jak wygląda faktura?</summary>
          <p>Ceny podajemy netto, wystawiamy fakturę VAT. {ph("Ceny planów, płatność miesięczna lub roczna")} Szczegóły w <a href="#cennik">cenniku</a>.</p></details>
      </div>
    </div>
  </section>

  <section class="cta" aria-labelledby="cta-title">
    <div class="wrap">
      <div class="cta-copy">
        <h2 id="cta-title" class="h2">Sprawdź Albertona na własnej umowie</h2>
        <p>Umów bezpłatną, 20-minutową prezentację.</p>
      </div>
      <div class="actions">
        <a class="btn btn-primary" href="/prezentacja/">Umów bezpłatną prezentację</a>
      </div>
    </div>
  </section>
'''
page("/", "Alberton — anonimizacja umów przed wklejeniem do AI",
     "Alberton zamienia nazwiska, numery PESEL, adresy i numery rachunków na znaczniki, zanim tekst opuści Twój komputer. Działa offline, dla dokumentów po polsku i angielsku.",
     "home", home, HOME_LD)

# ---------------------------------------------------------------- Dlaczego my?
docs = [
    ("Opis bezpieczeństwa i architektury", "Jak działa program, gdzie przetwarzane są dokumenty, co zapisuje na dysku.", "Dział IT"),
    ("Lista połączeń sieciowych", "Z czym i kiedy program łączy się z internetem, np. aktywacja licencji, aktualizacje.", "Dział IT"),
    ("Dokument dotyczący przetwarzania danych osobowych", "Np. umowa powierzenia albo wyjaśnienie, dlaczego nie jest potrzebna.", "Inspektor ochrony danych"),
    ("Polityka prywatności", "Kto przetwarza dane z formularzy i pobrań, w jakim celu i jak długo.", "Inspektor ochrony danych"),
    ("Regulamin i umowa licencyjna", "Warunki korzystania z programu i zakres licencji.", "Zarząd kancelarii"),
    ("Wykaz komponentów oprogramowania (SBOM)", "Biblioteki użyte w programie i ich wersje.", "Dział IT"),
    ("Wynik i metoda testu jakości", "Jak sprawdzaliśmy wykrywanie danych na polskich dokumentach.", "Partnerzy, dyrektor prawny"),
]
docs_html = "\n".join(
    f'          <li><div class="doc-what"><strong>{ph(n)}</strong><span>{d}</span></div><span class="doc-for">{w}</span></li>'
    for n, d, w in docs)

why = f'''
  <section class="wrap page-head" aria-labelledby="why-title">
    <p class="eyebrow">Dlaczego my?</p>
    <h1 id="why-title">Bezpieczeństwo, które możesz sprawdzić</h1>
    <p class="lead">Alberton powstał dla kancelarii i działów prawnych, w których tajemnica zawodowa nie podlega negocjacjom. Dokumenty klientów nie opuszczają komputera, a na to, co piszemy o bezpieczeństwie, mamy dokumentację, którą dział IT i inspektor ochrony danych mogą przejrzeć przed wdrożeniem.</p>
    <div class="actions" style="justify-content:center">
      <a class="btn btn-primary" href="#dokumentacja">Zobacz dokumentację</a>
      <a class="btn btn-outline" href="/prezentacja/">Umów prezentację (20 min)</a>
    </div>
  </section>

  <section class="band" aria-labelledby="safe-title">
    <div class="wrap section">
      <div class="section-head">
        <h2 id="safe-title" class="h2">Bezpieczni z założenia</h2>
        <p class="muted">Najbezpieczniejsze dane to te, które nigdzie nie wyjeżdżają. Dlatego Alberton działa w całości na Twoim komputerze.</p>
      </div>
      <div class="grid">
        <div class="card"><span class="meta">[OFFLINE]</span><h3>Przetwarzanie na Twoim komputerze</h3><p>Anonimizacja działa bez internetu. Dokumenty nie trafiają na nasze ani niczyje serwery.</p></div>
        <div class="card"><span class="meta">[KONTROLA]</span><h3>Ty decydujesz, co wysyłasz</h3><p>Alberton nie łączy się z żadnym czatem AI. Tekst wklejasz sam, po przejrzeniu znaczników.</p></div>
        <div class="card"><span class="meta">[LOGI]</span><h3>Bez treści dokumentów w logach</h3><p>Treść dokumentów nie trafia do telemetrii ani raportów błędów. {ph("potwierdzić z zespołem produktu")}</p></div>
        <div class="card"><span class="meta">[OSTROŻNOŚĆ]</span><h3>Lepiej zakryć za dużo</h3><p>Wątpliwe fragmenty program zakrywa i oznacza do sprawdzenia, zamiast je przepuszczać.</p></div>
      </div>
    </div>
  </section>

  <section id="dokumentacja" class="wrap section" aria-labelledby="docs-title">
    <div class="section-head">
      <h2 id="docs-title" class="h2">Pełna dokumentacja bezpieczeństwa</h2>
      <p class="muted">Mamy dokumenty, o które pyta dział IT, inspektor ochrony danych i zarząd kancelarii przed wdrożeniem nowego narzędzia. Udostępniamy je przed zakupem.</p>
    </div>
    <ul class="docs">
{docs_html}
    </ul>
    <p class="center" style="margin-top:28px"><a class="btn btn-primary" href="/prezentacja/">Poproś o dokumentację</a></p>
  </section>

  <section class="band" aria-labelledby="diff-title">
    <div class="wrap section">
      <div class="section-head">
        <h2 id="diff-title" class="h2">Co nas wyróżnia</h2>
      </div>
      <div class="grid">
        <div class="card"><h3>Zrobione dla polskich dokumentów</h3><p>Rozpoznajemy polskie identyfikatory, takie jak PESEL, i polską odmianę imion i nazwisk w umowach, pismach i pozwach.</p></div>
        <div class="card"><h3>Pokazujemy wynik, nie obietnicę</h3><p>Publikujemy wynik testu jakości na polskich dokumentach i metodę, którą go zmierzyliśmy. {ph("link do testu")}</p></div>
        <div class="card"><h3>Mówimy precyzyjnie</h3><p>Zamiana danych na znaczniki to zwykle pseudonimizacja, nie anonimizacja w rozumieniu RODO. Nie obiecujemy pełnej anonimowości, tylko pokazujemy, co zostało zakryte.</p></div>
      </div>
    </div>
  </section>

  <section id="zgloszenia" class="wrap section" aria-labelledby="vuln-title">
    <div class="prose">
      <h2 id="vuln-title" class="h2">Zgłaszanie podatności</h2>
      <p>Jeśli znajdziesz lukę w zabezpieczeniach programu lub strony, napisz na {ph("adres do zgłoszeń, np. security@…")}. Odpowiadamy w ciągu {ph("czas odpowiedzi")}. Zasady zgłoszeń opisuje {ph("plik security.txt")}.</p>
    </div>
  </section>

  <section class="cta" aria-labelledby="why-cta">
    <div class="wrap">
      <div class="cta-copy">
        <h2 id="why-cta" class="h2">Pokażemy to na Twoim przykładzie</h2>
        <p>20 minut online, bezpłatnie i bez zobowiązań. Odpowiemy też na pytania działu IT.</p>
      </div>
      <a class="btn btn-primary" href="/prezentacja/">Umów prezentację</a>
    </div>
  </section>
'''
page("/dlaczego-my/", "Dlaczego Alberton? Bezpieczeństwo i dokumentacja",
     "Alberton działa offline, a dokumenty klientów nie opuszczają komputera. Zobacz dokumentację bezpieczeństwa dla działu IT i inspektora ochrony danych.",
     "why", why)

# ---------------------------------------------------------------- Prezentacja
demo = f'''
  <section class="wrap page-head" aria-labelledby="demo-title">
    <p class="eyebrow">Bezpłatnie · 20 minut · online</p>
    <h1 id="demo-title">Umów bezpłatną prezentację Albertona</h1>
    <p class="lead">Pokażemy, jak Alberton zakrywa dane w umowie, i odpowiemy na pytania o bezpieczeństwo i wdrożenie. Bez zobowiązań.</p>
  </section>

  <section class="wrap" style="padding-bottom:96px">
    <div class="split" style="align-items:flex-start">
      <div class="rule-copy">
        <h2 class="h2">Plan rozmowy</h2>
        <ol class="agenda">
          <li><span class="mono">00–05</span><span>Jak Twój zespół pracuje dziś z dokumentami i AI</span></li>
          <li><span class="mono">05–15</span><span>Pokaz na przykładowej umowie: znaczniki, „do sprawdzenia”, ręczne zakrywanie</span></li>
          <li><span class="mono">15–20</span><span>Pytania o bezpieczeństwo, dokumentację i wdrożenie</span></li>
        </ol>
        <p class="muted">Rozmowa odbywa się w {ph("narzędzie, np. Microsoft Teams lub Google Meet")}. Możesz zaprosić osobę z działu IT lub inspektora ochrony danych.</p>
      </div>
      <form class="form" action="#" method="post" aria-labelledby="form-title">
        <h2 id="form-title" class="h2" style="font-size:1.5rem;text-align:center">Wybierz termin</h2>
        <p class="note">{ph("Podłączyć: kalendarz rezerwacji, np. Cal.com lub Calendly, albo usługę obsługi formularzy")}</p>
        <div class="field"><label for="f-name">Imię i nazwisko</label><input id="f-name" name="imie" autocomplete="name" required></div>
        <div class="field"><label for="f-mail">E-mail służbowy</label><input id="f-mail" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="f-org">Kancelaria lub firma</label><input id="f-org" name="organizacja" autocomplete="organization"></div>
        <div class="field"><label for="f-size">Liczba prawników</label>
          <select id="f-size" name="wielkosc"><option>1</option><option>2–9</option><option>10–49</option><option>50 i więcej</option></select></div>
        <div class="field"><label for="f-when">Preferowany termin</label><input id="f-when" name="termin" placeholder="np. wtorek lub środa po 14:00"></div>
        <div class="field"><label for="f-msg">O czym chcesz porozmawiać? (opcjonalnie)</label><textarea id="f-msg" name="wiadomosc" rows="3"></textarea></div>
        <p class="note">Administratorem danych z formularza jest {ph("nazwa spółki")}. Użyjemy ich tylko do umówienia prezentacji. Szczegóły w <a href="#">polityce prywatności</a>.</p>
        <button class="btn btn-primary" type="submit">Umów prezentację</button>
      </form>
    </div>
  </section>
'''
page("/prezentacja/", "Umów bezpłatną prezentację Albertona (20 min)",
     "Bezpłatna, 20-minutowa prezentacja Albertona online: pokaz anonimizacji umowy i odpowiedzi na pytania o bezpieczeństwo i wdrożenie.",
     "demo", demo)

# ---------------------------------------------------------------- Poradnik
posts = [
    ("PORADNIK_01", "Czy radca prawny może wkleić umowę do ChatGPT? Co mówią rekomendacje KIRP",
     "Co wynika z rekomendacji samorządu dla codziennej pracy z narzędziami AI i jak przygotować dokument przed wklejeniem.",
     "czy można wkleić umowę do ChatGPT"),
    ("PORADNIK_02", "Anonimizacja a pseudonimizacja w kancelarii: różnica w praktyce",
     "Dlaczego zamiana nazwisk na znaczniki to zwykle pseudonimizacja i co z tego wynika dla kancelarii.",
     "anonimizacja a pseudonimizacja"),
    ("PORADNIK_03", "Polityka korzystania z AI w kancelarii: wzór do pobrania",
     "Gotowy wzór zasad korzystania z AI dla zespołu, z miejscem na narzędzia, które kancelaria dopuszcza.",
     "polityka AI w kancelarii wzór"),
]
cards = "\n".join(f'''        <article class="card">
          <span class="meta">[{k}]</span>
          <h3>{t}</h3>
          <p>{d}</p>
          <p class="stat-label">W przygotowaniu · fraza: „{f}”</p>
        </article>''' for k, t, d, f in posts)

blog = f'''
  <section class="wrap page-head" aria-labelledby="blog-title">
    <p class="eyebrow">Poradnik</p>
    <h1 id="blog-title">AI w kancelarii bez danych klientów</h1>
    <p class="lead">Praktyczne wpisy dla prawników: jak korzystać z narzędzi AI przy umowach i pismach, nie narażając tajemnicy zawodowej.</p>
  </section>

  <section class="wrap" style="padding-bottom:96px">
    <div class="grid">
{cards}
    </div>
  </section>
'''
page("/poradnik/", "Poradnik: AI w kancelarii bez danych klientów — Alberton",
     "Wpisy dla prawników o korzystaniu z AI przy umowach i pismach: rekomendacje KIRP, anonimizacja a pseudonimizacja, polityka AI w kancelarii.",
     "blog", blog)

# Szablon wpisu: niewidoczny dla wyszukiwarek, do kopiowania przy nowych artykułach.
ART_LD = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[Tytuł wpisu, do 60 znaków, z frazą]",
  "datePublished": "[RRRR-MM-DD]",
  "author": {"@type": "Person", "name": "[Autor]"},
  "publisher": {"@type": "Organization", "name": "Alberton", "url": "https://alberton.pl/"}
}
</script>
'''
tmpl = f'''
  <article class="wrap section">
    <div class="prose">
      <p class="breadcrumb center"><a href="/">Alberton</a> / <a href="/poradnik/">Poradnik</a> / {ph("tytuł wpisu")}</p>
      <p class="eyebrow center">[PORADNIK_NN]</p>
      <h1 class="center" style="font-size:clamp(2rem,4vw,2.6rem);line-height:1.1">{ph("Tytuł wpisu z frazą, na którą celujemy")}</h1>
      <p class="center stat-label">{ph("autor")} · {ph("data")} · {ph("czas czytania")}</p>
      <p class="lead">{ph("Lead: 2–3 zdania z odpowiedzią na pytanie z tytułu")}</p>
      <h2>{ph("Śródtytuł 1: pytanie, które zadaje prawnik")}</h2>
      <p>{ph("Treść sekcji")}</p>
      <h2>{ph("Śródtytuł 2")}</h2>
      <p>{ph("Treść sekcji")}</p>
      <h2>Najważniejsze w skrócie</h2>
      <p>{ph("3–5 zdań podsumowania")}</p>
      <div class="card center"><h3>Sprawdź Albertona na własnej umowie</h3><p class="center">Umów bezpłatną prezentację.</p><p><a class="btn btn-primary btn-sm" href="/prezentacja/">Umów prezentację</a></p></div>
    </div>
  </article>
'''
page("/poradnik/szablon-wpisu/", "[Tytuł wpisu] — Poradnik Alberton", "[Opis meta, do 155 znaków]",
     "blog", tmpl, ART_LD, noindex=True)

# Mapa strony
urls = ["/", "/dlaczego-my/", "/prezentacja/", "/poradnik/"]
(REPO / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>https://alberton.pl{u}</loc></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
print("ok")
