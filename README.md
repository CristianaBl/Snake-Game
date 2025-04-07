# 🐍 Snake Game - Tkinter Edition

Un joc clasic Snake, dezvoltat în Python folosind biblioteca `tkinter`. Am adăugat obstacole, controlul vitezei, pauză, restart și coliziune cu margini – pentru o experiență mai interesantă și provocatoare!

## 🎮 Funcționalități

✅ **Gameplay de bază**  
- Șarpele se mișcă în toate cele 4 direcții (↑ ↓ ← →)  
- Crește în lungime de fiecare dată când mănâncă mâncarea (🍇)  
- Jocul se termină dacă șarpele se lovește de margine, de sine sau de obstacole  

✅ **Obstacole dinamice**  
- La fiecare 3 puncte marcate, apare un nou obstacol (🧱)  
- Obstacolele sunt generate aleatoriu și evită zona șarpelui și mâncării  

✅ **Scor live**  
- Scorul curent este afișat pe ecran, actualizat în timp real  

✅ **Controlul jocului**  
- `← ↑ → ↓` – Controlează direcția șarpelui  
- `P` – Pauză / Reia jocul  
- `R` – Repornește jocul dacă este în starea "Game Over"  

✅ **Dificultate dinamică**  
- Viteza jocului crește pe măsură ce scorul crește  
- Delay-ul scade gradual până la un minim, crescând intensitatea jocului  

## 🖼️ Interfață

- Interfața este creată cu `tkinter.Canvas`  
- Culori distincte pentru șarpe (verde), mâncare (mov), obstacole (gri)  
- Textul este afișat cu fonturi stilizate   
