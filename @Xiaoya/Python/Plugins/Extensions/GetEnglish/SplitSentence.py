import re


def list_to_text(_list, num_of_line):
    text = ''
    for num, i in enumerate(_list, start=1):
        if num % num_of_line != 0:
            text += i + '\n'
        else:
            text += i + '\n\n'
    return text

def OT(text):
    while (text[0:1] == '\n' or text[0:1] == ' ' or text[0:1] == '　'):#left
        text = text[1:]
    while (text[-1:] == '\n' or text[-1:] == ' ' or text[-1:] == '　'):#right
        text = text[:-1]
    return text

def handle(obj):
    text = obj.group(0)
    text = OT(text)
    return text + '\n'*2

def split_sentence(text):
    text = re.sub(r'((.*?)(?<!B|A)([!?.] ) ?)', handle, text)
    
    a_list = text.split('\n')
    a_list = [OT(i) for i in a_list if re.match(r'^\s*$', i) == None]
 
    text = list_to_text(a_list, 1)
    return text.strip('  　\n ')

def main(text):
    text = re.sub(r'[(（]\s*\w*\d*\s*[)）]', '', text)
    return split_sentence(text)



text = '''
Good News Beats Bad on Social Networks.


Bad news sells.

If it bleeds, it leads.

No news is good news, and good news is no news.

Those are the classic rules for the evening broadcasts and the morning papers.

But now that information is being spread and monitored in different ways, researchers are discovering new rules.

By tracking people's e-mails and online posts, scientists have found that good news can spread faster and farther than disasters and sob stories.

"The 'if it bleeds' rule works for mass media," says Jonah Berger, a scholar at the University of Pennsylvania.

"They want your eyeballs and don't care how you're feeling. But when you share a story with your friends, you care a lot more how they react. You don't want them to think of you as a Debbie Downer."

Researchers analyzing word-of-mouth communication — e-mails, Web posts and reviews, face-to-face conversations — found that it tended to be more positive than negative, but that didn't necessarily mean people preferred positive news.

Was positive news shared more often simply because people experienced more good things than bad things?

To test for that possibility, Dr.Berger looked at how people spread a particular set of news stories: thousands of articles on The New York Times' website.

He and a Penn colleague analyzed the "most e-mailed" list for six months.

One of his first findings was that articles in the science section were much more likely to make the list than non-science articles.

He found that science amazed Times' readers and made them want to share this positive feeling with others.

Readers also tended to share articles that were exciting or funny, or that inspired negative feelings like anger or anxiety, but not articles that left them merely sad.

They needed to be aroused one way or the other, and they preferred good news to bad.

The more positive an article, the more likely it was to be shared, as Dr.Berger explains in his new book, "Contagious: Why Things Catch On."

'''
print(main(text))
