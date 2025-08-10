class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
      a = [[0 for j in range(n)] for i in range(n)]
      direction = 'r'
      i,j,x,n_sq = 0,0,1,n * n
      while x <= n_sq: 
        print(direction,i,j)
        if direction == 'r' and (j + 1 >= n or a[i][j + 1] != 0):
          a[i][j] = x
          direction = 'd'
          i += 1
        elif direction == 'l' and (j - 1 < 0 or a[i][j - 1] != 0):
          a[i][j] = x
          direction = 'u'
          i -= 1
        elif direction == 'd' and (i + 1 >= n or a[i + 1][j] != 0):
          a[i][j] = x
          direction = 'l'
          j -= 1
        elif direction == 'u' and (i - 1 < 0 or a[i - 1][j] != 0):
          a[i][j] = x
          direction = 'r'
          j += 1
        else:
          a[i][j] = x
          match direction:
            case 'r': j += 1
            case 'l': j -= 1
            case 'u': i -= 1
            case 'd': i += 1
        x += 1
      return a
