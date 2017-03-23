import os


commands = '''
chmod 400 ../.ssh/id_rsa
eval "$(ssh-agent -s)"
ssh-add ../.ssh/id_rsa
git add .
git commit -m "update"
git push origin master
'''
commands = [c for c in commands.split('\n') if c != '']
os.system(' && '.join(commands))

print('OK')
