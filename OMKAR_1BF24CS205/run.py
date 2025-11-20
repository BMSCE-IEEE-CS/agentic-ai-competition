import random
import customtkinter as ctk

# --------------------------------------------------
# Modern clean UI setup
# --------------------------------------------------
ctk.set_appearance_mode("light")   # light mode but not pure white
ctk.set_default_color_theme("blue")


# --------------------------------------------------
# DATA
# --------------------------------------------------
categories = {
    "Fruits": {
        "apple": "A red or green fruit.",
        "banana": "A long yellow fruit.",
        "orange": "A citrus fruit.",
        "mango": "The king of fruits.",
        "grapes": "Small round fruits in bunches."
    },
    "Animals": {
        "tiger": "A big wild cat with stripes.",
        "elephant": "Largest land animal.",
        "rabbit": "Small animal with long ears.",
        "dolphin": "A smart sea mammal.",
        "penguin": "A bird that swims well."
    },
    "Countries": {
        "india": "A large country in South Asia.",
        "japan": "Island nation known for tech.",
        "brazil": "Largest country in South America.",
        "canada": "Cold and very large country.",
        "egypt": "Land of pyramids."
    },
    "Tech": {
        "python": "A popular programming language.",
        "server": "Provides services to computers.",
        "router": "Device that forwards packets.",
        "driver": "Software controlling hardware.",
        "memory": "Stores data for CPU."
    }
}

secret = ""
hint_text = ""
guess_word = []
tries = 5
game_over = False


# --------------------------------------------------
# GAME LOGIC
# --------------------------------------------------
def pick_new_secret(cat):
    global secret, hint_text
    items = categories[cat]
    secret = random.choice(list(items.keys()))
    hint_text = items[secret]


def start_new_game():
    global guess_word, tries, game_over

    pick_new_secret(category_var.get())
    guess_word = ["_"] * len(secret)
    tries = 5
    game_over = False

    word_label.configure(text=" ".join(guess_word))
    result_label.configure(text="")
    hint_label.configure(text=f"Category: {category_var.get()}  •  Letters: {len(secret)}")

    entry.configure(state="normal")
    submit_btn.configure(state="normal")
    hint_btn.configure(state="normal")
    play_again_btn.place_forget()

    entry.focus()


def submit_letter():
    global tries, game_over

    if game_over:
        return

    letter = entry.get().lower().strip()
    entry.delete(0, "end")

    if not letter or len(letter) != 1 or not letter.isalpha():
        result_label.configure(text="Enter ONE letter", text_color="#d9534f")
        return

    if letter in secret:
        for i, ch in enumerate(secret):
            if ch == letter:
                guess_word[i] = letter
        result_label.configure(text="Correct ✓", text_color="#28a745")
    else:
        tries -= 1
        result_label.configure(text=f"Wrong! Tries left: {tries}", text_color="#d9534f")

    word_label.configure(text=" ".join(guess_word))

    if "_" not in guess_word:
        result_label.configure(text=f"🎉 You Win! Word: {secret}", text_color="#28a745")
        end_game()
    elif tries == 0:
        result_label.configure(text=f"❌ You Lost! Word: {secret}", text_color="#d9534f")
        word_label.configure(text=" ".join(secret))
        end_game()


def end_game():
    global game_over
    game_over = True

    entry.configure(state="disabled")
    submit_btn.configure(state="disabled")
    hint_btn.configure(state="disabled")

    play_again_btn.place(relx=0.5, rely=1, anchor="s", y=-10)


def show_hint():
    hint_label.configure(text=f"Hint: {hint_text}\nStarts with: {secret[0]}", text_color="#555")


def on_category_change(_):
    start_new_game()


# --------------------------------------------------
# UI BUILD
# --------------------------------------------------
app = ctk.CTk()
app.geometry("700x540")
app.title("Guess The Word — Clear Stylish Edition")
app.resizable(False, False)

# 👉 Soft Color Background
app.configure(fg_color="#dde7f2")   # soft blue-gray background


# Title
title = ctk.CTkLabel(
    app,
    text="✨ GUESS THE WORD ✨",
    font=ctk.CTkFont(size=32, weight="bold"),
    text_color="#1f3b5c"
)
title.pack(pady=(20, 10))


# ---------- Stylish Card (rounded + border) ----------
card = ctk.CTkFrame(
    app,
    width=640,
    height=360,
    corner_radius=20,
    fg_color="#f7f9fc",     # clean light color
    border_width=2,
    border_color="#a4b4c8", # soft border
)
card.pack(pady=10)
card.pack_propagate(False)


# Category select
category_var = ctk.StringVar(value="Fruits")
category_menu = ctk.CTkOptionMenu(
    card,
    width=200,
    values=list(categories.keys()),
    variable=category_var,
    command=on_category_change,
    fg_color="#1f3b5c",
    button_hover_color="#2d4e79",
)
category_menu.pack(pady=(15, 10))


# Word Display Box
word_frame = ctk.CTkFrame(
    card,
    fg_color="#e4ecf5",
    height=90,
    corner_radius=12,
)
word_frame.pack(pady=15, padx=50, fill="x")
word_frame.pack_propagate(False)

word_label = ctk.CTkLabel(
    word_frame,
    text="",
    font=ctk.CTkFont(size=34, weight="bold"),
    text_color="#1f3b5c"
)
word_label.pack(expand=True)


# Entry Box
entry = ctk.CTkEntry(
    card,
    width=80,
    height=45,
    justify="center",
    font=ctk.CTkFont(size=24),
)
entry.pack(pady=10)


# Submit / Hint Buttons
btn_container = ctk.CTkFrame(card, fg_color="transparent")
btn_container.pack()

submit_btn = ctk.CTkButton(
    btn_container,
    text="Submit Letter",
    width=170,
    height=42,
    fg_color="#1f3b5c",
    hover_color="#2d4e79",
    command=submit_letter,
)
submit_btn.grid(row=0, column=0, padx=10, pady=5)

hint_btn = ctk.CTkButton(
    btn_container,
    text="Hint",
    width=110,
    height=42,
    fg_color="#f0ae39",
    hover_color="#ffc865",
    text_color="black",
    command=show_hint,
)
hint_btn.grid(row=0, column=1, padx=10, pady=5)


# Labels
hint_label = ctk.CTkLabel(card, text="", font=ctk.CTkFont(size=14))
hint_label.pack(pady=8)

result_label = ctk.CTkLabel(card, text="", font=ctk.CTkFont(size=16, weight="bold"))
result_label.pack(pady=5)


# Play again button (hidden until needed)
play_again_btn = ctk.CTkButton(
    card,
    text="Play Again",
    width=180,
    height=45,
    fg_color="#22a96f",
    hover_color="#26c07d",
    corner_radius=18,
    command=start_new_game,
)


# Footer
footer = ctk.CTkLabel(app, text="Tip: Choose category → type a letter → Submit", font=ctk.CTkFont(size=12))
footer.pack(pady=12)


# Start
start_new_game()
app.mainloop()
