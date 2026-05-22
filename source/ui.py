# imports
import tkinter as tk
from tkinter import ttk
from constants import (
    BATTLE_STAMP_NAMES,
    COSTUME_NAMES,
    CARD_NAMES,
    QUEST_NAMES,
)

def make_checklist(tab, items, per_col, cols):
    frames = []
    vars_list = []

    for _ in range(cols):
        f = tk.Frame(tab)
        f.pack(side="left", anchor="n", padx=10)
        frames.append(f)

    for i, name in enumerate(items):
        col = i // per_col
        if col >= cols:
            break

        v = tk.BooleanVar()
        vars_list.append(v)

        tk.Checkbutton(frames[col], text=name, variable=v).pack(anchor="w")

    return vars_list


# ----------------------------
# summary UI
# ----------------------------

def create_summary(tab):
    # overall row
    row = tk.Frame(tab)
    row.pack(fill="x", padx=10, pady=6)

    tk.Label(row, text="Overall Progress", width=20, anchor="w").pack(side="left")

    progress_bar = ttk.Progressbar(row, mode="determinate")
    progress_bar.pack(side="left", fill="x", expand=True, padx=10)

    progress_label = tk.Label(row, width=18, anchor="e")
    progress_label.pack(side="right")

    def make_row(name):
        r = tk.Frame(tab)
        r.pack(fill="x", padx=10, pady=3)

        tk.Label(r, text=name, width=20, anchor="w").pack(side="left")

        bar = ttk.Progressbar(r, mode="determinate")
        bar.pack(side="left", fill="x", expand=True, padx=10)

        lbl = tk.Label(r, width=18, anchor="e")
        lbl.pack(side="right")

        return bar, lbl

    stamp_bar, stamp_label = make_row("Battle Stamps")
    costume_bar, costume_label = make_row("Costumes")
    card_bar, card_label = make_row("Creepy Treat Cards")
    quest_bar, quest_label = make_row("Quests")
    level_bar, level_label = make_row("Level 10")

    missing_summary_label = tk.Label(tab, text="", anchor="w", justify="left")
    missing_summary_label.pack(fill="x", padx=10, pady=10)

    return {
        "progress_bar": progress_bar,
        "progress_label": progress_label,
        "stamp_bar": stamp_bar,
        "stamp_label": stamp_label,
        "costume_bar": costume_bar,
        "costume_label": costume_label,
        "card_bar": card_bar,
        "card_label": card_label,
        "quest_bar": quest_bar,
        "quest_label": quest_label,
        "level_bar": level_bar,
        "level_label": level_label,
        "missing_summary_label": missing_summary_label,
    }


# ----------------------------
# tabs
# ----------------------------

def create_stamps(tab):
    return make_checklist(tab, BATTLE_STAMP_NAMES, 8, 3)

def create_costumes(tab):
    return make_checklist(tab, COSTUME_NAMES, 3, 4)

def create_cards(tab):
    return make_checklist(tab, CARD_NAMES, 9, 4)

def create_quests(tab):
    return make_checklist(tab, QUEST_NAMES, 9, 4)

def create_levels(tab):
    level10_var = tk.BooleanVar()

    tk.Checkbutton(tab, text="Level 10", variable=level10_var).pack(anchor="w", padx=10)

    return [level10_var]