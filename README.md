# AlbertonWWW

Strona internetowa aplikacji Alberton. Statyczny HTML/CSS/JS, bez kroku budowania, hostowany na GitHub Pages.

## Struktura

- `index.html` — strona główna
- `404.html` — strona błędu
- `assets/styles.css` — style (paleta, typografia, układ)
- `assets/main.js` — przełącznik przykładu anonimizacji i rok w stopce
- `assets/fonts/` — fonty Inter, Manrope i IBM Plex Mono hostowane lokalnie (licencja SIL OFL)
- `CNAME` — własna domena dla GitHub Pages

## Zasady projektu

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

- Wersja 2 (od 16.11.2026): nowa identyfikacja, gałąź `main`.
- Wersja 1 (8.11.2026, granat i turkus): zamrożona na gałęzi `archiwum/wersja-1`. Nie zmieniaj tej gałęzi.

Żeby przywrócić wersję 1 na stronie, bez kasowania historii:

```
git checkout main
git checkout archiwum/wersja-1 -- .
git commit -m "Przywróć wersję 1 strony"
git push
```

Wersja 2 zostaje wtedy w historii `main`, więc można do niej wrócić tak samo (np. z commita „Strona w nowej identyfikacji”). Nowe pliki fontów zostaną w repozytorium, ale wersja 1 ich nie używa.
