# AlbertonWWW

Strona internetowa aplikacji Alberton. Statyczny HTML/CSS/JS, bez kroku budowania, hostowany na GitHub Pages.

## Struktura

- `index.html` — strona główna
- `404.html` — strona błędu
- `assets/styles.css` — style (paleta, typografia, układ)
- `assets/main.js` — przełącznik przykładu anonimizacji i rok w stopce
- `assets/fonts/` — fonty Inter i Manrope hostowane lokalnie (licencja SIL OFL)
- `CNAME` — własna domena dla GitHub Pages

## Zasady projektu

- Paleta: #0F4C81 (granat), #2B6CB0 (niebieski), #38B2AC (turkus, tylko akcenty graficzne), #E6FFFA (mięta), #FFFFFF. Tekst #1E293B.
- Proporcja 60-30-10, kontrast tekstu min. 4.5:1 (WCAG AA).
- Fonty: Manrope 700 (nagłówki), Inter 400/600 (tekst). Bez Google Fonts.
- Bez wzorców „vibe-coded”: fioletowych gradientów, poświat, glassmorphismu, emoji jako ikon, pigułki nad H1, trzech identycznych kart z ikonami, kolorowych pasków na krawędziach kart, zmyślonych statystyk i opinii.

## Podgląd lokalny

```
python3 -m http.server 8000
```

i otwórz http://localhost:8000
