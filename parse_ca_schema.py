
# coding: utf-8

# In[27]:

import csv
from string import find


# In[28]:

# parse descriptor rows, simple convention, hard coded positions 1-4, 6-9, 11-end

def parse_descriptors(x):
    return {'schema':x[:4], 'class':x[5:9],'title':x[10:]}    

# parse_descriptors("JL26 4546 ACCOUNTING OFFICER (SPECIALIST)")


# In[29]:

test={'entry':'$3,247.00 - $3,689.00 01 19 21 206 1 12 2 R01'}

def parse_range(x):
    if x[1]==' ':
        return {'range':x[0], 'entry':x[2:]}
    else:
        return {'range': None, 'entry':x}

#test.update(parse_range(test['entry']))
#prev feeding it a string, now a dictionary


# In[30]:

test={'entry':'$7,156.00 - $8,960.00 01 19 1 12 E S09'}

def parse_pay(x):
    first_space=find(x,' ')
    low=x[:first_space]
    second_dollar=find(x,'$',1)
    third_space=find(x,' ',second_dollar)
    high=x[second_dollar:third_space]

    '''
    print "first space is at position", first_space
    print "the parsed low income is", low
    print "the second dollar sign is at position", second_dollar
    print "the third space is at position", third_space    
    print "the parsed high income is", high
    '''
    return {'low':low, 'high':high,'entry':x[third_space+1:]}
    
test.update(parse_pay(test['entry']))


# In[31]:

test={'entry':'1 6 2 R04'}

#print test['entry'][:4]
#string comparisons are case sensitive

def parse_special(x):
    if x[:7]=='HR SISA':
        special='HR SISA'
        return {'special':special, 'entry':x[8:]}
    elif x[:4]=='SISA':
        special='SISA'
        return {'special':special, 'entry':x[5:]}
    elif x[:3]=='DAY':
        special='DAY'
        return {'special':special, 'entry':x[4:]}
    elif x[:2]=='HR':
        special='HR'
        return {'special':special, 'entry':x[3:]}
    else:
        return {'special':None, 'entry':x} #i.e. i have no specials

parse_special(test['entry'])


# In[32]:

#test={'entry': '01 12 19 014 1 12 E S10'}
test={'entry':'0 6 2 R01'}

def parse_footnotes(x):
    pointer=2 #init pointer to start looking for spaces
    footnotes=[] #init empty string to hold footnotes
    
    if x[pointer]!=' ':
        return {'entry':x, 'footnotes':None}
    
    while x[pointer]==' ':
        #print "found a space at position",pointer
        footnotes.append(x[pointer-2:pointer])
        pointer=pointer+3
    #print footnotes
    #print x[pointer-2:]
    return {'entry':x[pointer-2:],'footnotes':footnotes}


parse_footnotes(test['entry'])


# In[33]:

#parse AR CRIT, repurposing of footnotes code

#problem, pointer +4 will sometimes inadverdantly run into a space
#exiting too early

#1 6 2 R04

test={'entry': '1 6 2 R04'}

#logic,if there is a space in the string, return nothing

#                         111111111
#               0123456789012345678

def parse_arcrit(x):
    pointer=3 #init pointer to start looking for spaces
    arcrit=[] #init empty string to hold footnotes
    
    if x[pointer]!=' ':
        return {'entry':x, 'arcrit':None}
    
    while x[pointer]==' ':
        #print "found a space at position",pointer
        if ' ' in x[pointer-3:pointer]:
            #return {'entry':x[pointer-3:],'arcrit':arcrit}
            return {'entry':x[pointer-3:],'arcrit':None}
        arcrit.append(x[pointer-3:pointer])
        pointer=pointer+4
        
    #print footnotes
    #print x[pointer-2:]
    #print pointer
    
    return {'entry':x[pointer-3:],'arcrit':arcrit}


parse_arcrit(test['entry'])


# In[34]:

test={'entry':"1 6 2 NT R12"}

def parse_mcr_prob(x):
    if x[3]==' ': #one digit prob
        return {'mcr':x[0],'prob':x[2],'entry':x[4:]}
    else: #two digit prob
        return {'mcr':x[0],'prob':x[2:4],'entry':x[5:]}
    
parse_mcr_prob(test['entry'])


# In[35]:

test={'entry':'2E NT R12'}

def parse_wwg(x):
    space=find(x,' ')
    #print x[:space]
    #print x[space+1:]
    return {'wwg':x[:space], 'entry':x[space+1:]}

parse_wwg(test['entry'])


# In[36]:

test={'entry':'R18'}

def parse_nt_cbid(x):
    space=find(x,' ')
    #print space
    if space != -1: #there is a space
        return {'nt':x[:space], 'cbid':x[space+1:]}
    else: #no space
        return {'nt':None, 'cbid':x}
    
parse_nt_cbid(test['entry'])


# In[37]:

input_file  = open('schema_alphabetic_cleaned', 'rU') #Open data file

data = [line.rstrip('\n') for line in input_file] #data is a list of strings, each containing one line

#turn it into a dict with a kvp for type, classify as either title or pay line
#print type(data) #iam list

schema=[]

for line in data:
    if '$' in line:
        schema.append({"entry":line,"type":"pay","raw":line})
    else:
        schema.append({"entry":line,"type":"descriptor", "raw":line})


# In[38]:

for line in schema:
    if line['type']=='descriptor':
        line.update(parse_descriptors(line['entry']))
        #print line
        #print "\n"
    elif line['type']=='pay':
        line.update(parse_range(line['entry']))
        line.update(parse_pay(line['entry']))
        line.update(parse_special(line['entry']))
        line.update(parse_footnotes(line['entry']))
        line.update(parse_arcrit(line['entry']))
        line.update(parse_mcr_prob(line['entry']))
        line.update(parse_wwg(line['entry']))
        line.update(parse_nt_cbid(line['entry']))
        #cannot update something that doesn't exist
        #print line
        #print "\n"


# In[39]:

#need to design something to "copy over" class/schem/title from previous record 
#print type(schema) #iamlist

# .update() methods adds dict2 kvps to dict1 on dict1.update(dict2)

prev={} #iam global dictionary

for idx, val in enumerate(schema):
    if val['type']=='descriptor':
        prev['class']=val['class']
        prev['schema']=val['schema']
        prev['title']=val['title']
        #print prev
    
    if val['type']=='pay':
        val.update(prev)
        print val
        print "\n"


# In[40]:

#new version

with open('schema_alphabetic_final.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(['class','schema','title','range','low','high','special','footnotes','arcrit','mcr','prob',
                     'wwg','nt','cbid'])
    for line in schema:
        if line['type']=='pay':
            writer.writerow([line['class'],line['schema'],line['title'],
                             line['range'],line['low'],line['high'],line['special'],
                             line['footnotes'],line['arcrit'],line['mcr'],line['prob'],line['wwg'],
                             line['nt'],line['cbid']
                            ])


# In[ ]:



