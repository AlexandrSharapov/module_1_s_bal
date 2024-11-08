#Задание "Средний балл":

#содержит списки оценок для каждого ученика в алфавитном порядке Например:
grades = [
         [5, 3, 3, 5, 4],
         [2, 2, 2, 3],
         [4, 5, 5, 2],
         [4, 4, 3],
         [5, 5, 5, 4, 5]]

#содержит неупорядоченную последовательность имён всех учеников в классе
students = {
            'Johnny',
            'Bilbo',
            'Steve',
            'Khendrik',
            'Aaron'}
#сортировка студентов в алфавитном порядке
students = list(students)
students.sort()


#(sum)сумма всех значений []/ (len)на количество значений[]
medium_ball = (sum(grades[0]) / len(students[0]),
                sum(grades[1]) / len(students[1]),
                sum(grades[2]) / len(students[2]),
                sum(grades[3]) / len(students[3]),
                sum(grades[4]) / len(students[4]))


#принял функцию zip() для связки сразу двух листов список учеников + средняя оценка в кортеж
journal = {students : grades for students, grades  in
           zip(students, medium_ball)}

print(dict(journal)) #переводим в словарь



