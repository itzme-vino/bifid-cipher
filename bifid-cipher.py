
def getInput(lines = []):
  """ 
    Gets input from file input. Returns list of lines from input file
  """
  import fileinput

  for line in fileinput.input():
    lines.append(line.strip('\n'))
  return lines

class BifidCipher:
  searchInTableau = lambda self, letter : next( (col, row.index(letter)) for col, row in enumerate(self.tableau) if letter in row )

  def __init__(self, tableau = None):
    self.tableau = tableau

  def encrypt(self, message):
    tuples = []
    message = message.replace(" ", "")

    # searches letter in matrix
    for letter in message: 
      tuples.append( self.searchInTableau(letter) )

    row1, row2 = [], []
    index = 0 # index of coordinate in pair
    # Order new pairs in two lists, list of rows & list of cols
    for coordinate in tuples:
      row1.append(coordinate[0])
      row2.append(coordinate[1])
    
    pairs = row1 + row2 # concatenate lists
      
    string = '' # map pairs to new letter and append to string
    for i in range(0, len(pairs)-1, 2):
      newPair = pairs[i:i+2]
      string += self.tableau[newPair[0]][newPair[1]]

    return string

  def decrypt(self, cypherText):
    tuples = []
    flatten = lambda l: [item for sublist in l for item in sublist]

    # searches letter in matrix
    for letter in cypherText: 
      tuples.append( list(self.searchInTableau(letter)) )
    tuples = flatten(tuples)

    half = len(tuples)//2
    row1, row2 = tuples[:half], tuples[half:]

    message = ''
    for tupleNumber in range(half):
      message += self.tableau[row1[tupleNumber]][row2[tupleNumber]]
    
    return message

def main():

  TABLEAU = [
    ['E', 'N', 'C', 'R', 'Y'],
    ['P', 'T', 'A', 'B', 'D'],
    ['F', 'G', 'H', 'I', 'K'],
    ['L', 'M', 'O', 'Q', 'S'],
    ['U', 'V', 'W', 'X', 'Z'],
  ]

  bifid = BifidCipher(TABLEAU)

  inputLines = getInput()

  if inputLines[0] == 'ENCRYPT':
    res = bifid.encrypt(inputLines[1])

  elif inputLines[0] == 'DECRYPT':
    res = bifid.decrypt(inputLines[1])
    
  else:
    print('COMMAND ERROR')

  print(res)
  return 

if __name__ == "__main__":
  main()
