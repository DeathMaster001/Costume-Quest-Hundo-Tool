def calc_progress(vars_list):
    done = sum(v.get() for v in vars_list)
    total = len(vars_list)
    pct = (done / total * 100) if total else 0
    return done, total, pct

def summarize_missing(groups):
    parts = []

    for name, vars_list in groups.items():
        missing = sum(not v.get() for v in vars_list)

        if missing > 0:
            if name == "Level 10":
                parts.append("Level 10")
            else:
                parts.append(f"{missing} {name}")

    if not parts:
        return "Everything completed 🎉"

    return "Missing: " + ", ".join(parts)