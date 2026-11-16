# AlbertonWWW

Strona internetowa aplikacji Alberton. Statyczny HTML/CSS/JS, bez kroku budowania, hostowany na GitHub Pages.

## Struktura

- `index.html` — strona główna
- `dlaczego-my/` — zakładka „Dlaczego my?”: bezpieczeństwo i dokumentacja
- `prezentacja/` — umawianie bezpłatnej, 20-minutowej prezentacji
- `poradnik/` — wpisy pod SEO; `poradnik/szablon-wpisu/` to wzór nowego wpisu (noindex, poza mapą strony)
- `narzedzia/generuj.py` — opcjonalny skrypt, który odtwarza wszystkie strony ze wspólnym nagłówkiem, paskiem FAQ i stopką; zmiany w menu lub stopce rób w nim i uruchom `python3 narzedzia/generuj.py .`
- `404.html` — strona błędu
- `assets/styles.css` — style (paleta, typografia, układ)
- `assets/main.js` — przełącznik przykładu anonimizacji i rok w stopce
- `assets/fonts/` — fonty Inter, Manrope i IBM Plex Mono hostowane lokalnie (licencja SIL OFL)
- `CNAME` — własna domena dla GitHub Pages

## Zasady projektu

- Logo (znak i nazwa) bez zmian: nawiasy #0F4C81, pasek #38B2AC, na ciemnym tle nawiasy białe.
- Teksty wyśrodkowane (nagłówki, wstępy), tekst ciągły justowany; w wąskich kolumnach (karty, kroki) do lewej.
- `[…]` w ramce (klasa `.ph`) oznacza treść do uzupełnienia przed publikacją.
- Idea marki: „znacznik zamiast danych”.
- Paleta: Atrament #13233F (tekst, ciemne sekcje), Papier #F7F5F0 (tło), Znacznik #2FB39A (tylko grafika), Znacznik ciemny #11766A (przyciski, linki), Sygnał #E9A23B (tylko „do sprawdzenia”), Grafit #4A5568 (tekst drugorzędny).
- Kontrast tekstu min. 4.5:1 (WCAG AA).
- Fonty: Manrope 700/800 (nagłówki), Inter 400/600 (tekst), IBM Plex Mono 600 (znaczniki typu [OSOBA_1]). Bez Google Fonts.
- Bez wzorców „vibe-coded”: fioletowych gradientów, poświat, glassmorphismu, emoji jako ikon, pigułki nad H1, trzech identycznych kart z ikonami, kolorowych pasków na krawędziach kart, zmyślonych statystyk i opinii.

## Podgląd lokalny

```
python3 -m http.server 8000
```

i otwórz http://localhost:8000

## Wersje i przywracanie

- Wersja 3 (od 16.11.2026): zakładki Dlaczego my?, Prezentacja, Poradnik; zmiany wg audytu. Gałąź `main`.
- Wersja 2 (16.11.2026, nowa identyfikacja, jedna strona): zamrożona na gałęzi `archiwum/wersja-2`.
- Wersja 1 (8.11.2026, granat i turkus): zamrożona na gałęzi `archiwum/wersja-1`.

Gałęzi `archiwum/*` nie zmieniaj. Żeby przywrócić wybraną wersję na stronie, bez kasowania historii (przykład dla wersji 2):

```
git checkout main
git rm -r -q .
git checkout archiwum/wersja-2 -- .
git commit -m "Przywróć wersję 2 strony"
git push
```

`git rm` usuwa najpierw pliki, których starsza wersja nie miała (np. podstrony wersji 3), żeby nie zostały na stronie. Nowsza wersja zostaje w historii `main` i można do niej wrócić tak samo.
