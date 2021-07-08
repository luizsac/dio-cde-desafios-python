def scores_mean(x, y):
  mean = (x + y) / 2
  print(f"media = {mean:.2f}")


def valid_scores():
  x = float(input())
  if 0 <= x <= 10:
    return x
  else:
    print("nota invalida")
    return valid_scores()
 

choice = 1
while choice == 1:
  i = -1
  j = -1
  while i == -1:
    i = valid_scores()
  while j == -1:
    j = valid_scores()
  scores_mean(i, j)
  choice = 3
  while choice != 1 and choice != 2:
    choice = eval(input('novo calculo (1-sim 2-nao)\n'))
    
