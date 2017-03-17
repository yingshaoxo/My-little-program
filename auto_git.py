import os

commands = '''
git add .
git commit -m "update"
git push origin master
'''
os.system(' && '.join([c for c in commands.split('\n') if c.strip(' ') != '']))
