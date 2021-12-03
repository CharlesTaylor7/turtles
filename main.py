from turtles.chase import TurtleChase


turtle_chase = TurtleChase()

test_phrases = [
    'WAVMN',
    'PBR'
    'CD',
    'EFHILT'
    'KXYZ'
    'OGQJSU'
]


for phrase in test_phrases:
    turtle_chase.draw(phrase)


turtle_chase.start()
