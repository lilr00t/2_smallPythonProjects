powerlifter = str(input('Please enter lifters name: '))
# total = int(input('Input your total: '))
s = int(input('Squat: '))
b = int(input('Bench: '))
d = int(input('Deadlift: '))

print(powerlifter.title() + ' is A powerlifter.')
print(powerlifter.title() + ' has A {}lbs squat,'.format(s), 'A {}lbs bench,'.format(b),
      'and A {}lbs deadlift.'.format(d), 'This gives them A {}lbs total.'.format(s + b + d))
