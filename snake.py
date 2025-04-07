import tkinter
import random

ROWS = 25
COLS = 25
TILE_SIZE = 25
WINDOW_WIDTH = TILE_SIZE * COLS
WINDOW_HEIGHT = TILE_SIZE * ROWS

# Clasa Tile pentru pozitionare
class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Initializare fereastra
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg="pink", width=WINDOW_WIDTH, height=WINDOW_HEIGHT, borderwidth=0, highlightthickness=0)
canvas.pack()
window.update()

# Centrare fereastra
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Initializare elemente de joc
snake = Tile(5 * TILE_SIZE, 5 * TILE_SIZE)
food = Tile(10 * TILE_SIZE, 10 * TILE_SIZE)
snakebody = []
obstacles = []  # obstacole

velocityx = 0
velocityy = 0

game_over = False
pause = False
score = 0
base_speed = 150  # Delay

# Functie pentru generarea obstacolelor
def generate_obstacles(n):
    obs = []
    for _ in range(n):
        # Asigura că obstacolul nu este plasat pe poziția sarpelui sau a hranei
        while True:
            obs_tile = Tile(random.randint(0, COLS-1) * TILE_SIZE, random.randint(0, ROWS-1) * TILE_SIZE)
            if (obs_tile.x, obs_tile.y) != (snake.x, snake.y) and (obs_tile.x, obs_tile.y) != (food.x, food.y):
                break
        obs.append(obs_tile)
    return obs

# Generam cateva obstacole initiale
obstacles = generate_obstacles(10)

# Funcție pentru schimbarea direcției
def change_direction(e):
    global velocityx, velocityy, game_over, pause
    if game_over:
        return
    if e.keysym == "p":  # Tasta de pauza si resume
        toggle_pause()
        return
    if pause:
        return
    if e.keysym == "Up" and velocityy != 1:
        velocityx = 0
        velocityy = -1
    elif e.keysym == "Down" and velocityy != -1:
        velocityx = 0
        velocityy = 1
    elif e.keysym == "Left" and velocityx != 1:
        velocityx = -1
        velocityy = 0
    elif e.keysym == "Right" and velocityx != -1:
        velocityx = 1
        velocityy = 0

# Functie pentru a întrerupe/reporni jocul
def toggle_pause():
    global pause
    pause = not pause

# Functie de reset pentru a relua jocul dupa game over
def reset_game():
    global snake, food, snakebody, obstacles, velocityx, velocityy, game_over, score, pause
    snake = Tile(5 * TILE_SIZE, 5 * TILE_SIZE)
    food = Tile(10 * TILE_SIZE, 10 * TILE_SIZE)
    snakebody = []
    obstacles = generate_obstacles(10)
    velocityx = 0
    velocityy = 0
    game_over = False
    pause = False
    score = 0

# Funcție de miscare
def move():
    global snake, food, snakebody, game_over, score
    if game_over or pause:
        return
    # Verificare coliziune cu margini
    if snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT:
        game_over = True
        return
    # Verificare coliziune cu corpul șarpelui
    for tile in snakebody:
        if snake.x == tile.x and snake.y == tile.y:
            game_over = True
            return
    # Verificare coliziune cu obstacolele
    for obs in obstacles:
        if snake.x == obs.x and snake.y == obs.y:
            game_over = True
            return
    # Verificare coliziune cu mâncarea
    if snake.x == food.x and snake.y == food.y:
        snakebody.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS-1) * TILE_SIZE
        food.y = random.randint(0, ROWS-1) * TILE_SIZE
        score += 1
        # La fiecare marire cu 3 a scorului adaugam obstacol nou
        if score % 3 == 0:
            obstacles.extend(generate_obstacles(1))
    # Actualizare pozitie corp sarpe
    for i in range(len(snakebody)-1, -1, -1):
        tile = snakebody[i]
        if i == 0:
            tile.x = snake.x
            tile.y = snake.y
        else:
            prevtile = snakebody[i-1]
            tile.x = prevtile.x
            tile.y = prevtile.y

    snake.x += velocityx * TILE_SIZE
    snake.y += velocityy * TILE_SIZE

# Functia de desenare
def draw():
    global snake, food, snakebody, game_over, score
    move()
    canvas.delete("all")

    # Desenare mancare
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill="purple")
    
    # Desenare obstacole
    for obs in obstacles:
        canvas.create_rectangle(obs.x, obs.y, obs.x + TILE_SIZE, obs.y + TILE_SIZE, fill="gray")
    
    # Desenare sarpe
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill="lime green")
    for tile in snakebody:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill="lime green")
    
    # Afisare scor
    canvas.create_text(40, 10, font="Arial 10", text=f"Score: {score}", fill="black")
    
    # Afisare mesaj de pauză
    if pause and not game_over:
        canvas.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, font=("Comic Sans MS", 40, "bold"), text="Pauza", fill="blue")
    
    # Afisare mesaj game over
    if game_over:
        canvas.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, font=("Arial",35,"bold"), text=f"GAME OVER: {score}", fill="red")
        canvas.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 30, font=("Comic Sans MS", 20), text="Apasă R pentru restart", fill="black")
    
    # Viteza se ajusteaza in functie de scor pentru a creste dificultatea
    delay = max(50, base_speed - score * 5)
    window.after(delay, draw)

# Functie pentru restart joc
def restart_game(e):
    if game_over:
        reset_game()

# Legarea tastelor
window.bind("<KeyRelease>", change_direction)
window.bind("r", restart_game)

draw()
window.mainloop()
