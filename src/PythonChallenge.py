'''
Created on Nov 11, 2009

@author: sjoseph
'''

import string
import re
import urllib.request
import pickle

def ceasar_cipher():
    def subst(x):
        if x in string.punctuation + string.whitespace:
            return x
        else:
            val = ord(x) + 2
            while val > ord('z'):
                val = (val - ord('z')) + ord('a') - 1
            
            return chr(val)
    
    #input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."      
    input = "map"
    print(''.join([_ for _ in map(subst, input)]))

def rare_characters():
    input = '''
    hello dfsdfdsf%$##$#
    '''
    print([_ for _ in filter(lambda x: x in string.ascii_letters, input)])

def bodyguards():
    input = '''
            test
            '''
    
    m = ''.join( [ x[4] for x in re.findall('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', input)] )
    print(m)
    
def chainsaw():
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={0}'
    next = 46059
    for _ in range(400):
        u = urllib.request.urlopen(url.format(next))
        data = str(u.read())
        print(data)
        next = re.search('next nothing is (\d+)', data).group(1)
        print(next)
        u.close()
        
def unpickle():
    f = open('c:/temp/banner.p', 'rb')
    data = pickle.load(f)
    f.close()
    
    for x in data:
        for c, n in x:
            for i in range (n):
                print(c, end='')
            
        print()

    
if __name__ == "__main__":
    #ceasar_cipher()
    #rare_characters()
    #bodyguards()
    #chainsaw()
    unpickle()