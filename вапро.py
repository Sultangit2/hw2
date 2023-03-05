def triangle_area(x1, y1, x2, y2, x3, y3):
    """Функция нахождения площади треугольника"""
    area = abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2)
    return area

def is_right_triangle(x1, y1, x2, y2, x3, y3):
    """Функция проверки, является ли треугольник прямоугольным"""
    sides = sorted([((x1-x2)**2 + (y1-y2)**2)**0.5, ((x2-x3)**2 + (y2-y3)**2)**0.5, ((x1-x3)**2 + (y1-y3)**2)**0.5])
    return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-6

# пример вызова функций:
x1, y1, x2, y2, x3, y3 = 0, 0, 3, 0, 0, 4
area = triangle_area(x1, y1, x2, y2, x3, y3)
is_right = is_right_triangle(x1, y1, x2, y2, x3, y3)

with open("area.txt", "w") as f1, open("truefalse.txt", "w") as f2:
    f1.write(str(area))
    f2.write(str(is_right))

sentence = "The quick brown fox fox fox jumps over the lazy dog."

sentence = sentence.lower().replace(".", "").replace(",", "").replace("!", "").replace("?", "")

words = sentence.split()

word_counts = {}
for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1
most_common_word = max(word_counts, key=word_counts.get)

print(f"Слово, которое встречается чаще всего: {most_common_word}", )




n = int(input())

times = []
for i in range(n):
    h, m, s = map(int, input().split())
    times.append((h, m, s))

times_sorted = sorted(times)

for t in times_sorted:
    print("{:02d}:{:02d}:{:02d}".format(t[0], t[1], t[2]))


