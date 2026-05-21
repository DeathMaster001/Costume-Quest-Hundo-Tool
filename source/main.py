# imports
import os
import tkinter as tk
from tkinter import ttk
from constants import (
    COSTUME_NAMES,
    BATTLE_STAMP_NAMES,
    CARD_NAMES,
    QUEST_NAMES,
    LEVELS
)

# ----------------------------
# progress calculation
# ----------------------------

def calc_progress(vars_list):
    done = sum(v.get() for v in vars_list)
    total = len(vars_list)
    pct = (done / total * 100) if total else 0
    return done, total, pct


def update_progress(parent, stamp, card, quest, costume, level):
    s_done, s_total, s_pct = calc_progress(stamp)
    c_done, c_total, c_pct = calc_progress(card)
    q_done, q_total, q_pct = calc_progress(quest)
    co_done, co_total, co_pct = calc_progress(costume)
    l_done, l_total, l_pct = calc_progress(level)

    all_vars = stamp + card + quest + costume + level
    t_done, t_total, t_pct = calc_progress(all_vars)

    # update bars
    stamp_bar["value"] = s_pct
    card_bar["value"] = c_pct
    quest_bar["value"] = q_pct
    costume_bar["value"] = co_pct
    level_bar["value"] = l_pct
    progress_bar["value"] = t_pct

    # update text
    progress_label.config(text=f"Overall {t_done}/{t_total} ({t_pct:.1f}%)")
    stamp_label.config(text=f"{s_done}/{s_total} ({s_pct:.1f}%)")
    card_label.config(text=f"{c_done}/{c_total} ({c_pct:.1f}%)")
    quest_label.config(text=f"{q_done}/{q_total} ({q_pct:.1f}%)")
    costume_label.config(text=f"{co_done}/{co_total} ({co_pct:.1f}%)")
    level_label.config(text=f"{l_done}/{l_total} ({l_pct:.1f}%)")

    parent.after(300, lambda: update_progress(parent, stamp, card, quest, costume, level))


# ----------------------------
# checkbox helper
# ----------------------------

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
    global progress_bar, progress_label
    global stamp_bar, card_bar, quest_bar, costume_bar, level_bar
    global stamp_label, card_label, quest_label, costume_label, level_label

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
    card_bar, card_label = make_row("Creepy Treat Cards")
    quest_bar, quest_label = make_row("Quests")
    costume_bar, costume_label = make_row("Costumes")
    level_bar, level_label = make_row("Levels")


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
    vars_list = []
    for lv in LEVELS:
        v = tk.BooleanVar()
        tk.Checkbutton(tab, text=f"Level {lv}", variable=v).pack(anchor="w", padx=10)
        vars_list.append(v)
    return vars_list


# ----------------------------
# main
# ----------------------------

def main():
    root = tk.Tk()
    root.title("Costume Quest Tracker")
    root.geometry("800x725")
    root.minsize(800, 725)

    notebook = ttk.Notebook(root)

    t1 = ttk.Frame(notebook)
    t2 = ttk.Frame(notebook)
    t3 = ttk.Frame(notebook)
    t4 = ttk.Frame(notebook)
    t5 = ttk.Frame(notebook)
    t6 = ttk.Frame(notebook)

    notebook.add(t1, text="Summary")
    notebook.add(t2, text="Stamps")
    notebook.add(t3, text="Costumes")
    notebook.add(t4, text="Cards")
    notebook.add(t5, text="Levels")
    notebook.add(t6, text="Quests")

    create_summary(t1)

    stamps = create_stamps(t2)
    costumes = create_costumes(t3)
    cards = create_cards(t4)
    levels = create_levels(t5)
    quests = create_quests(t6)

    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # icon
    icon = os.path.join(os.getcwd(), "icon.ico")
    if os.path.exists(icon):
        root.iconbitmap(icon)

    update_progress(root, stamps, cards, quests, costumes, levels)

    root.mainloop()


if __name__ == "__main__":
    main()