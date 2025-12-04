# Personal Finance Tracker

A small, client-side Personal Finance Tracker built with HTML, CSS and JavaScript.

Features
- Add an expense with a title and amount.
- Expenses are saved in your browser's Local Storage.
- View list of expenses, delete individual items, or clear all.
- Total expenses displayed with two-decimal precision.

Files
- `index.html` — UI and structure
- `style.css` — basic styling
- `script.js` — logic (localStorage, rendering, event handlers)

How to run
1. Open `KISHAN/index.html` in your browser (double-click or drag into the browser).
2. Add expenses using the form. Data is saved automatically in Local Storage.
3. To reset, use the "Clear All" button or delete items individually.

Notes
- This is a simple single-file app that runs fully in the browser; no server required.
- Local Storage is per-origin; if you open the file using the `file://` protocol some browsers may treat origins differently. Using a simple static server (e.g., `python -m http.server`) will work too.

Enjoy! Feel free to ask for enhancements (categories, dates, charts, export/import).