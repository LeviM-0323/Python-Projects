import tkinter as tk
import colorsys
import math

CELL_SIZE = 20
GRID_WIDTH = 15
GRID_HEIGHT = 15

cells = []
last_cell = [-1,-1]
spin = 0

root = tk.Tk()
canvas = tk.Canvas(root, width=GRID_WIDTH * CELL_SIZE, height=GRID_HEIGHT * CELL_SIZE)
root.title("Colour Thing")
canvas.grid(row=1, column=0)

for row in range(GRID_HEIGHT):
    row_cells = []
    for col in range(GRID_WIDTH):
        x1 = col * CELL_SIZE
        y1 = row * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        rect = canvas.create_rectangle(x1, y1, x2, y2, fill="gray", outline="white")
        row_cells.append(rect)
    cells.append(row_cells)

highlight = None

def hsv_to_hex(h, s, v):
    """Convert HSV (0-1 floats) to #RRGGBB hex string."""
    r,g,b = colorsys.hsv_to_rgb(h,s,v)
    return f'#{int(r *255):02x}{int(g * 255):02x}{int(b * 255):02x}'

def on_mouse_move(event):
    global last_cell
    col = event.x // CELL_SIZE
    row = event.y // CELL_SIZE
    if [row, col] != last_cell:
        last_cell = [row, col]

def update_spiral():
    global spin, highlight
    try:
        col = root.winfo_pointerx() - root.winfo_rootx()
        row = root.winfo_pointery() - root.winfo_rooty()
        col = col // CELL_SIZE
        row = row // CELL_SIZE
    except:
        col = GRID_WIDTH // 2
        row = GRID_HEIGHT // 2

    for r in range(GRID_HEIGHT):
        for c in range(GRID_WIDTH):
            dx = c - col
            dy = r - row
            dist = (dx ** 2 + dy ** 2) ** 0.5
            angle = (math.atan2(dy, dx) + math.pi) / (2 * math.pi)
            hue = (angle + dist * 0.07 + spin) % 1.0
            color = hsv_to_hex(hue, 1, 1)
            canvas.itemconfig(cells[r][c], fill=color)

    # Draw highlight rectangle on top
    if highlight is not None:
        canvas.delete(highlight)
    if 0 <= last_cell[0] < GRID_HEIGHT and 0 <= last_cell[1] < GRID_WIDTH:
        x1 = last_cell[1] * CELL_SIZE
        y1 = last_cell[0] * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        highlight = canvas.create_rectangle(x1, y1, x2, y2, outline="red", width=2)

    spin += 0.01
    root.after(30, update_spiral)
update_spiral()
canvas.bind("<Motion>", on_mouse_move)
root.mainloop()