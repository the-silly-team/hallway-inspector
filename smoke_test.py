import os
import sys
import tkinter as tk

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import doorsoft_inspector as d

base = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "fixtures"))
files = [
    os.path.join(base, "menu.drtx"),
    os.path.join(base, "tone.drau"),
    os.path.join(base, "collision.drcl"),
    os.path.join(base, "level.drlv"),
    os.path.join(base, "scene.drsc"),
    os.path.join(base, "manifest.drmf"),
]

root = tk.Tk()
app = d.InspectorApp(root)
for f in files:
    app.open_file(f)
    for tab in range(4):
        app.nb.select(tab)
        root.update()
root.after(150, root.destroy)
root.mainloop()
print("GUI SMOKE OK", len(app.files), "files")
