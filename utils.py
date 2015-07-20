"""This is my awesome utility kitchen sink"""

import colors as c

def ask(question,color=c.yellow,lower=True,strip=True,end='\n> '):
    print(color + question + c.reset, end=end)
    answer =  input(c.white)
    if lower: answer = answer.lower()
    if strip: answer = answer.strip()
    print(c.reset, end="")
    return answer

if __name__ == '__main__':
    print(c.clear)
    answer = ask("What is your name?")
    print(answer)
