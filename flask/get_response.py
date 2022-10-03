import request_generation
import pandas as pd

column_names = ['command','email']
df = pd.read_csv('examples.csv',names=column_names)
preset = "This email writing program can generate full email templates from commands. Here are some examples:\n"
counter = 0
threshold = 15
email = ''
#seperator = '--SEPARATOR--\n'
seperator = '--\n'
for index, row in df.iterrows():
    counter += 1
    if counter > threshold:
        break
    preset +=  seperator
    preset += 'Command: '+row['command'] + '\n'
    preset += 'Email:' + row['email'].replace('\n',' ') + '\n'

q = 'how can I apply for a work permit'
p = "Command: A letter to the government asking " + q + '\n'
prompt = preset+'--\n'+p