import os
import tkinter as tk
from tkinter import ttk
from ui import (create_summary, create_stamps, create_costumes, create_cards, create_quests,create_levels)
from logic import calc_progress, summarize_missing

def main():
    root = tk.Tk()
    root.title("Costume Quest Tracker")
    root.geometry("800x300")
    root.minsize(800, 300)

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
    notebook.add(t5, text="Quests")
    notebook.add(t6, text="Level")

    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    ui = create_summary(t1)
    stamps = create_stamps(t2)
    costumes = create_costumes(t3)
    cards = create_cards(t4)
    quests = create_quests(t5)
    levels = create_levels(t6)

    categories = {
        "Stamps": stamps,
        "Costumes": costumes,
        "Cards": cards,
        "Quests": quests,
        "Level 10": levels,
    }

    def update():
        ui_map = {
            "Stamps": (ui["stamp_bar"], ui["stamp_label"]),
            "Costumes": (ui["costume_bar"], ui["costume_label"]),
            "Cards": (ui["card_bar"], ui["card_label"]),
            "Quests": (ui["quest_bar"], ui["quest_label"]),
            "Level 10": (ui["level_bar"], ui["level_label"]),
        }

        total_done = total_items = 0

        for name, vars_list in categories.items():
            done, total, pct = calc_progress(vars_list)
            total_done += done
            total_items += total

            bar, label = ui_map[name]
            bar["value"] = pct
            label.config(text=f"{done}/{total} ({pct:.1f}%)")

        overall = (total_done / total_items * 100) if total_items else 0

        ui["progress_bar"]["value"] = overall
        ui["progress_label"].config(
            text=f"{total_done}/{total_items} ({overall:.1f}%)"
        )

        ui["missing_summary_label"].config(
            text=summarize_missing(categories)
        )

        root.after(300, update)

    update()

    # set icon if available
    import constants
    icon_path = os.path.join(constants.BASE_DIR, "icon.ico")
    if os.path.exists(icon_path):
        try:
            root.iconbitmap(icon_path)
        except Exception:
            pass

    root.mainloop()


if __name__ == "__main__":
    main()