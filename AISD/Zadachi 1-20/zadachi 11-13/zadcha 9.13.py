alf = 'а, е, ё, и, о, у, ы, э, ю, я'
a = set('съешь ещё этих мягких французских булок, да выпей чаю')
for i in range(len(a)):
    if alf[i] in a:
        print(alf[i], end=' ')