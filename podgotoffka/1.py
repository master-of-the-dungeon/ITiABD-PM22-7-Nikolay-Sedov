a = 'SIX,SEVEN,EIGHT,NINE,TEN'
a = a.split(',')
b = ''
for i in range(0,len(a),2):
    b+=a[i]
    b+=', '
print(b)