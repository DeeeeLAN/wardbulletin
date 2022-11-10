#!/usr/bin/env python
import os, re, shutil
from pathlib import Path

source_path = Path('wardbulletin/main/templates/main/')
workspace_path = Path('tmp')
dist_path = Path('wardbulletin/main/static/main')
colors = [
  'slate',
  'gray',
  'zinc',
  'neutral',
  'stone',
  'brown',
  'red',
  'orange',
  'amber',
  'yellow',
  'lime',
  'green',
  'emerald',
  'teal',
  'cyan',
  'sky',
  'blue',
  'indigo',
  'violet',
  'purple',
  'fuchsia',
  'pink',
  'rose',
]
theme_color_sub = re.compile(r'{{\s*theme_color\s*}}')

os.mkdir(workspace_path)
for color in colors:
  os.mkdir(workspace_path / color)
  for file in source_path.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
      with open(workspace_path / color / file.name, 'w') as w:
        filedata = f.read()
        w.write(theme_color_sub.sub(color, filedata))

  with open('tailwind.config.js', 'r', encoding='utf-8') as f:
    with open(workspace_path / f'tailwind-{color}.config.js', 'w') as w:
      lines = f.readlines()
      lines[2] = f'  content: ["./{workspace_path / color}/*.html"],\n'
      del lines[3:17]  # Adjust any time tailwind.config.js is updated
      w.writelines(lines)

  os.system(f'./tailwindcss -i source.css -o {dist_path / f"css/dist-{color}.css"} -c {workspace_path / f"tailwind-{color}.config.js"}')

shutil.rmtree(workspace_path)
