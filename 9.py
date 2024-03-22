height_1, height_2, height_3 = map(int, input().split())
summ = height_1 + height_2 + height_3
print(max(height_1, height_2, height_3), summ - max(height_1, height_2, height_3) - min(height_1, height_2, height_3),
      min(height_1, height_2, height_3))
