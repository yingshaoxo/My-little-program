import os

commands = ['cd ', 'cd Downloads/My-little-program/', 'git add .', 'git commit -m "update"', 'git push origin master']
os.system(' && '.join(commands))