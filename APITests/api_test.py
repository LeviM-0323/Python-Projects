import requests
import tkinter as tk
import json

"""
ability-scores: /api/2014/ability-scores,
alignments: /api/2014/alignments,
backgrounds: /api/2014/backgrounds,
classes: /api/2014/classes,
conditions: /api/2014/conditions,
damage-types: /api/2014/damage-types,
equipment: /api/2014/equipment,
equipment-categories: /api/2014/equipment-categories,
feats: /api/2014/feats,
features: /api/2014/features,
languages: /api/2014/languages,
magic-items: /api/2014/magic-items,
magic-schools: /api/2014/magic-schools,
monsters: /api/2014/monsters,
proficiencies: /api/2014/proficiencies,
races: /api/2014/races,
rule-sections": /api/2014/rule-sections,
rules: /api/2014/rules,
skills: /api/2014/skills,
spells: /api/2014/spells,
subclasses: /api/2014/subclasses,
subraces: /api/2014/subraces,
traits: /api/2014/traits,
weapon-properties: /api/2014/weapon-properties
"""

def fetch_data():
    userInput = entry.get()
    newUrl = f"https://www.dnd5eapi.co/api/2014/{userInput}"
    payload = {}
    headers = {
    'Accept': 'application/json'
    }
    try:
        response = requests.request("GET", newUrl, headers=headers, data=payload)
        data = response.json()
        pretty_text = json.dumps(data, indent=2)
    except Exception:
        pertty_text = response.text
    text_box.config(state='normal')
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, pretty_text)
    text_box.config(state='disabled')

root = tk.Tk()
root.title("D&D 5e API Viewer")
frame = tk.Frame(root)
frame.grid()

entry = tk.Button(frame, text="Fetch", command=fetch_data)
entry.grid(row=0, column=0, padx=5, pady=5)

text_box = tk.Text(frame, wrap="word", width=80, height=30, font=("Consolas", 10))
text_box.grid(row=1, column=0, columnspan=2, sticky="nsew")
scrollbar = tk.Scrollbar(frame, command=text_box.yview)
scrollbar.grid(row=1, column=2, sticky="ns")
text_box['yscrollcommand'] = scrollbar.set
text_box.config(state='disabled')

root.mainloop()