temporary = list()
for key, value in dictionary.items():
    temporary.append( (value, key) ) #reorders the values and key

print temporary
temporary.sort(reverse=True) #sorts list largest to smallest
for value, key in temporary[:10]: #prints top 10 values sorted largest to smallest
    print key, value
    
#print sorted( [ (v,k) for k,v in c.items() ] )