# <a id="texthead"/>Python-learning

#### В качестве IDE используется Visual Studio Code

[Семинар 1](#lesson1)  
[Семинар 2](#lesson2)  
[Семинар 3](#lesson3)  
[Семинар 4](#lesson4)  
[Семинар 5](#lesson5)  
[Семинар 6](#lesson6)  
[Семинар 8](#lesson8)

## <a id="lesson1"/> Задания с семинара 1 - папка lesson01

1. **Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.**  
Программный код в файле [***program1.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson01/program1.py). Необходимо ввести целое число от 1 до 7. Если число 6 или 7, то ответ - "да", иначе - "нет". Если пользователем вводится текст (не число) или число меньше нуля, то предлагается ввести число заново. Если введено число больше 7, то берётся остаток от деления на 7 (в квадратных скобках выводится полученное значение). Если остаток от деления на 7 получился равным нулю, то это означает, что было введено число кратное 7, поэтому производится корректировка - в переменную записывается число 7.
2. **Напишите программу для проверки истинности утверждения  
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z  
для всех значений предикат.**  
Программный код в файле [***program2.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson01/program2.py).Здесь используются три логические переменные, каждая из которых может принимать одно из двух значений (истина или ложь). Всего возможных комбинаций значений 2 в степени 3, т.е. 8. Чтобы не создавать условный оператор под каждую комбинацию (и не запутаться при этом), использованы три вложенных цикла. В каждом цикле переменная принимает значение True или False, и построчно выводится таблица истинности. На каждом шаге идёт проверка истинности логического выражения. Перед циклом задаётся перемнная count = 2^3 = 8. На каждом шаге цикла происходит проверка истинности выражения, если значение True, то count уменьшается на 1. Т.о. при прохождении всех комбинаций count должен быть равен нулю: если ноль, то равенство верно, иначе - равенство не верно, о чём выводится сообщение в конце работы программы.
3. **Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).**
Программный код в файле [***program3.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson01/program3.py). Условие неоднозначно, т.к. сначала оговорено, что X ≠ 0 и Y ≠ 0, а после допускается, что точка лежит на одной из осей координат (т.е. нулевое значение всё-таки допускается). Условным оператором проверяются возможные варианты: если координата (0,0), то выдаётся сообщение, что это точка пересечения координатных прямых (центр плоскости). Если одно из значений равно нулю, то выдаётся сообщение о принадлежности координантной прямой (Ох или Оу). В остальных случаях в зависимости от знака *х* и *у* выдаётся сообщение одной из четвертей. Проверка на корректность ввода исходных данных не производится, т.к. в библиотеках *python* соответствующий метод не нашёл (можно решить проблему используя исключение, но это тема следующих занятий). 
4. ***Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).***  
Программный код в файле [***program4.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson01/program4.py). Задача обратная предыдущей. При вводе номера четверти проверяется введённое число, если оно не входит в диапазон 1..4, то выдаётся сообщение об обшибке. Если всё нормально, то в зависимости от четверти выводится возможный диапазон принимаемых значений для *х* и *у*. Здесь *Infinity* означает *бесконечность*.  
5. ***Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.***  
Программный код в файле [***program5.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson01/program5.pyy). Задача решается с помощью теоремы Пифагора, где искомое расстояние - гипотенуза прямоугольгого треугольника. Катеты треугольника - разность между соответствующими координатами по *х* и по *у*. Здесь на знак разности не обращаем внимания, т.к. идёт возведение в квадрат (всегда положительное значение). Для извлечения квадратного корня возводим сумму квадратов катетов в степень 1/2. При выводе ответа полученное число приводим к строковому типу.  
[В начало](#texthead)  

## <a id="lesson2"/> Задания с семинара 2 - папка lesson02

1. ***Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными.***  
Программный код в файле [***program1.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson02/program1.py).  
Методом *def IsFloatNumber(a)* осуществляется проверка корректности введённого числа, т.е., что введено именно вещественное число (можно и целое), отрицательное или положительное - не важно. *При вводе в качестве разделителя дробной и целой частей допускается использовать как точку, так и запятую.* Затем из числа удаляются символы, не являющиеся цифрами (разделитель-точка, знак минус). Затем сумма цифр находится двумя способами: а) число рассматриватеся как строка, состоящая из цифр; строка перебирается, цифры суммируются; б) число рассматривается как целое число, на каждой итерации цикла суммируем остаток от деления на 10, само число делим на 10; и так до тех пор, пока исходное число не станет равным нулю.  
*Строку не переводил в вещественное число (float), т.к. при приведении типов в вещественном числе в дробной части имеет место быть "мусор", который усложняет задачу. А если мы знаем, что введено дробное число (проверено при вводе) и оно типа string, то проще привести его к целому типу.*  
2. ***Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N. Не используйте функцию math.factorial.***  
Программный код в файле [***program2.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson02/program2.py).  
При вводе количества элементов списка проводится проверка на корректность введённых данных. Список формируется в цикле. Перед началом цикла задаётся переменная *multiply* = 1, это первый элемент в формируемом списке. Далее, на каждом шаге переменная домножается на номер текущего шага, *i*, и заносится новым элементом в список.  
Здесь же представлен второй вариант решения задачи: в цикле по *i* от 1 до N рассчитываются элементы списка; на каждом шаге во вложенном цикле по *j* рассчитывается факториал для текущего значения *i*, который становится новым элементом списка.
3. ***Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак". А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но". Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз. Это происходит до тех пор, пока не будет найден палиндром. Напишите такую программу, которая найдет палиндром введенного пользователем числа.***  
Программный код в файле [***program3.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson02/program3.py).  
Метод *def ReverseNumber(num)* принимает целое число, и возвращает его зеркальное отображение. В цикле сравниваются исходное число и его зеркальное отображение, в соответствии с условием задачи.  
*Интересно. Для числа 4563 палиндромом оказалось число 69696, для этого понадобилось сложить число со своим "зеркалом" три раза.*

4. ***Реализуйте выдачу случайного числа, не использовать random.randint и вообще библиотеку random. Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности Учтите, что есть диапазон: от(минимальное) и до (максимальное)***  
Программный код в файле [***program4.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson02/program4.py).  
 
Случайное целое число генерируется методом *def GetRandomNumber(a, b)*, которому передаются левая и правая границы диапазона возможных значений.  
При запуске программы осуществляется инициализация датчика случайных чисел (получения зерна *t[0]*) - берётся текущее значение *time_ns*. Т.к. при отладке было отмечено, что практически постоянно *time_ns* возвращает целое значение с, как минимум, тремя нулями на конце, эти нули сразу же отсекаются (деление на 10). Новое случайное число вычисляется по формуле:  
t[i] = (a + t[i-1] * c) mod m, где  
a = 1664525, c = 1013904223, m = 2 ^ 32  
Значения a,c,m взяты не с потолка. Как утверждается в некоторых статьях, именно эти значения гарантируют получение неповторяющейся случайной последовательности (если, конечно начальное значение будет разным).  
Для наглядности работы метода-генератора генерируется список, который сначала демонстрирует полученную последовательность. Затем список сортируется по возрастанию - для демонстрации попадания всех чисел в заданный диапазон возможных значений.  
[В начало](#texthead)  

## <a id="lesson3"/> Задания с семинара 3 - папка lesson03

1. ***Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.***  
Програмный код в файле [***program1.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson03/program1.py)  
Список создаётся методом *CreateRandomList(ListLen = 10, MinNum = 0, MaxNum = 25)*, который принимает три параметра: *ListLen* - длина списка (по умолчанию = 10), левая граница диапазона принимаемых значений *MinNum* (по умолчанию = 0), правая граница диапазона принимаемых значений (по умолчанию = 25) включительно.  
Метод *GetSumInOddPosition(AList)* принимает список, в котором суммируются элементы на нечётных позициях и возвращает результат. Подсчёт идёт в цикле *for* начиная с позиции = 1 (первая нечётная позиция) с шагом +2. 
2. ***Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.***  
Програмный код в файле [***program2.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson03/program2.py)  
Для генерации списка используется метод *CreateRandomList* из [***program1.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson03/program1.py).  
Метод *CountMultiplicationOfPairNumbers(AList)* принимает рассматриваемый список и возвращает новый список, сформированный в соответствии с уловием задачи. Здесь задаются две переменные: *LeftIndex* - начальный индекс левой границы рассматриваемого списка, *RightIndex* - соответственно правая граница. Далее в цикле *while* на каждом шаге перемножаются текущие левый и правый элементы списка и заносится в новый формируемый список. Затем левая граница сдвигается вправо на 1, правая сдвигается влево на 1. Цикл останавливается когда *LeftIndex* окажется правее *RightIndex*. Если количество элементов исходного списка нечетное, последним шагом цикла будет ситуация когда *LeftIndex* = *RightIndex*, т.е. текущий элемент просто умножается сам на себя.
3. ***Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.***  
Програмный код в файле [***program3.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson03/program3.py).  
Список вещественных чисел можно было вводить с клавиатуры... Но я решил его генерировать рандомно. Метод *CreateRandomList* формирует список случайных вещественных чисел. К каждому случайному вещественному числу прибавляется случайное целое число, для наглядности решения.  
Метод *GetMaxFractionalPart(List)* получает исходный список, который просматривается в цикле. Т.к. интересует именно дробная часть, на каждом шаге от текущего элемента отнимается его целая часть, вещественная часть сравнивается с текущим максимумом. Метод *GetMinFractionalPart(List)* работает так же, как и на нахождение максимальной дробной части, но возвращает минимум.
4. ***Напишите программу, которая будет преобразовывать десятичное число в двоичное.***  
Програмный код в файле [***program4.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson03/program4.py).  
Метод *def DecToBin(dec)* получает целое число в десятичной системе счисления, возвращает это же число (тип *str*), но уже в двоичной системе счисления. Используется цикл *while*. Т.к. в *Python* цикла с постусловием нет, используется бесконечный цикл с предусловием, в котором после всех проведенных действий проверяется следует ли остановиться, и, если да, то - *break*. Сам алгоритм перевода из 10 в 2 стандартный - на каждом шаге делим на 2, остаток от деления записываем.
5. ***Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.***  
Програмный код в файле [***program5.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson03/program5.py)  
Последовательность Фибоначчи/негаФибоначчи находится двумя способами. Первый - использование цикла, где явно используется формула нахождения k-го числа последовательности. Реализовано в методе *Fibonacci(n)*, который возвращает список, содержащий последовательность от -k-го до +k-го числа. Второй способ - использование рекурсии. Рекурсивно находится k-е число последовательности (методы *RecFibonacci(k)* и *RecNegaFibonacci(k)*). Оба метода используются в циклах в методе *RecFibonacciList(n)*, в котором формируется список.  
[В начало](#texthead)  

## <a id="lesson4"/> Задания с семинара 4 - папка lesson04

1. ***Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.***   
Програмный код в файле [***program1.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson04/program1.py).  
Метод *list_of_multipliers(n)* для заданного натурального числа n выдаёт список всех множителей данного числа из множества простых чисел. Здесь используется метод *prime_numbers(lim)*, который возвращает список всех простых чисел, начиная 2 и заканчивая *lim*. Итоговый список формируется перебором простых чисел с проверкой деления заданного числа на каждое из них без остатка.  
2. ***Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.***  
Програмный код в файле [***program2.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson04/program2.py).  
Метод *analise_list(nums : list)* возвращает список, состоящий из чисел исходного списка, каждое из которых в новом списке присутствет лишь один раз. Создаётся копия исходного списка, которая сортируется в порядке возрастания. Текущее число сохраняется, все дубликаты удаляются.
3. ***В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».***  
Програмный код в файле [***program3.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson04/program3.py).  
В методе *read_from_file(file_path : str)* построчно считывается файл. Каждая строка - элемент формируемого списка. При считывании из строки удаляется символ перехода на новую строку *\n*. Т.к. оценка является последним символом каждой строки сформированного списка, добраться до неё не составляет труда. В методе *upper_better_four(ls : list)* просмтриваются все элементы списка, каждый из которых заканчивающийся оценкой выше 4 приводится к верхнему регистру с помощью функции *upper()*. Метод *write_into_file(file_path : str, list_str : str)* записывает заданный список в файл с заданным именем, каждый элемент списка - с новой строки.
4. ***Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево. Сдвиг часто называют ключом шифрования. Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.***  
Програмный код в файле [***program4.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson04/program4.py).    
Функция *encrypt_text(txt : str, key : int)* шифрует заданный текст *txt*, сдвигая символы на *key* позиций вправо. Используются функции *ord()* и *chr()*. Она же и дешифрует заданный текст - надо только передать *key* с противоположным знаком.  
Функция *write_into_file(file_path : str, txt : str)* записывает заданный текст в файл с заданным именем.
Функция *decrypt_text_from_file(filename : str)* запрашивает ключ шифрования, затем считывает текст из файла и дешифровывает его с помощью функции *encrypt_text*.
5. ***Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.***  
Програмный код в файле [***program5.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson04/program5.py).  
Для считывания текста (шифрованного, дешифрованного) используется функция *read_from_file(file_name : str)*. Запись текста в файл - функция *write_into_file(filename : str, txt : str)*.  
Шифрование текста осуществляется функцией *encode_rle(txt : str)*, дешифрование - функцией *decode_rle(txt : str)*. Для разделения пар количество-символ используется символ '|'.
[В начало](#texthead)  

## <a id="lesson5"/> Задания с семинара 5 - папка lesson05 
1. ***Напишите программу, удаляющую из текста все слова, содержащие ""абв"".***  
Програмный код в файле [***program1.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson05/program1.py).  
Здесь даже комментировать нечего. С помощь *lambda* и *filter* задача решается в одну строку. Красота!  
2. ***Создайте программу для игры с конфетами человек против человека.***
***Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?***
***a) Добавьте игру против бота. Достаточно сделать так, чтобы бот не брал конфет больше положенного или больше чем имеется в куче.***
***b) Подумайте как наделить бота ""интеллектом"". Напоминаю, если перед пользователем будет лежать 29 конфет, то он, однозначно, проиграет. Достаточно довести игру до такой ситуации.***  
Програмный код в файле [***program2.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson05/program2.py).  
При запуске игра инициализируется. Значения по умолчанию указаны в квадратных скобках - досточно просто нажать клавишу Enter. Можно задать свои начальные условия - сколько конфет в коробке, по сколько максимум брать за каждый шаг. На этапе инициализации выбираем второго игрока (человек или бот). Если выбрали бота, выбираем уровень игры: 1 - бот случайное количество конфет, 2 - бот ориентируется на ход оппонента. 
3. ***Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого. Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами. Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков. Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове.***  
Програмный код в файле [***program3.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson05/program3.py).  
4. ***Создайте программу для игры в ""Крестики-нолики"".***  
Програмный код в файле [***program4.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson05/program4.py).  
В начале выбираем режим игры: 1 - оба игрока - люди, 2 - второй игрок - бот. Бота наделять интеллектом не стал, т.к. в условии задачи ничего об этом не сказано. Когда ходит бот выбирается случайным образом незаполненная ячейка. Чей ход первый - определяется случайным образом, первыми всегда ходят крестики.  
5. ***Создать программу, считывающую два полинома из двух файлов и записывающая в третий файл их сумму. ***  
Програмный код в файле [***program5.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson05/program5.py).  
На формат полинома наложены некоторые ограничения:
- между элементами полинома и знаками операций ставится один пробел. Если коэффициент старшего члена отрицательный, то пробел после минуса не ставится
- коэффициенты - целые числа (отрицательные, положительные, ноль)
- между коэффициентом и переменной нет никаких знаков операции (типа *,х )
- степень члена - целое положительное число, отделяемое от переменной справа знаком *^*  
Первый полином считывается из файла *polynom1.txt*, второй - из файла *polynom2.txt*. Результат сложения записывается в файл *polynom3.txt*.  
[В начало](#texthead)  
## <a id="lesson6"/> Задания с семинара 6 - папка lesson06  
1. ***Определить, присутствует ли в заданном списке строк, некоторое число***  
Програмный код в файле [***program1.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson06/program1.py).  
Не совсем понятно задание: некоторое число - это число, заданное пользователем или любое число? Поэтому проверяется и то и другое. Список строк объединяется в один список, состоящий из слов. Далее с помощью функции *filter* находится решение.  
2. ***Найти сумму чисел списка стоящих на нечетной позиции***  
Програмный код в файле [***program2.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson06/program2.py).  
Исходный список состоит из случайных чисел. С помощью *filter* и *lambda* создаётся новый список, в который включаются элементы исходного списка, стоящие на нечетных позициях. Находится сумма элементов нового списка.  
3. ***Найти расстояние между двумя точками пространства(числа вводятся через пробел)***  
Програмный код в файле [***program3.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson06/program3.py).  
Допускается ввод целых и/или вещественных чисел. Для вещественных чисел в качестве разделителя целой и вещественной частей можно указывать как точку, так и запятую. Проверка на корректность ввода производится функцией *is_float_number(a)*, которая принимает на вход строку. Если строка конвертируется в вещественное число, то возвращается это самое число. Если же строка не может быть преобразована в тип *float*, то возвращается строковое *'None'*. Можно было бы возвращать *False* или *NULL*, но они равнозначны нулю. А координата может быть и нулевой.  
4. ***Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.***  
Програмный код в файле [***program4.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson06/program4.py).   
Функция *second_sub(string_list : list, sub_string : str)* принимает на вход список строк и искомую подстроку. Затем список строк с помощью *enumerate* преобразется в список кортежей, где вторым элементом кортежа явлется его индекс в исходном списке. Функцией *filter* отбрасываются все элементы, не содержащие искомую подстроку. Полученный спиок проверяется: если в нём количество кортежей меньше 2, то возвращается -1, если же 2 или более, то возвращается *элемент[1][0]*, где *[1]* - второй элемент в списке, *[0]* - индекс этого элемента в исходном списке.  
5. ***Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.***  
Програмный код в файле [***program5.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson06/program5.py).  
Исходный список, состоящий из случайных чисел, формируется в функции *map* (как альтернатива циклу *for*). Новый список, состоящий из произведений пар чисел в списке, формируется в цикле с количеством шагов, равным половине длины исходного списка.  
Если количество элементов исходного списка чётное, то при делении пополам получаем длину нового списка, равную половине. Здесь всё нормально. Если же количество чисел исходного списка нечётное, то длина нового списка = половина исходного + 1 (средний элемент, без пары, умножается сам на себя).  
6. ***Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.***  
Програмный код в файле [***program6.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson06/program6.py).  
Последовательность представляет собой ряд натуральных степений числа (-3). Результат получен двумя способами: в цикле, связкой map-lambda.  
[В начало](#texthead)  
## <a id="lesson8"/> Задания с семинара 8 - папка [lesson08](https://github.com/dtnfktu/Python-prog/tree/master/lesson08)  
***Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах. Под форматами понимаем структуру файлов, например:в файле на одной строке хранится одна часть записи, пустая строка - разделитель***  
Блок-схема архитектуры представлена на рисунке [***flowchart.png***](https://github.com/dtnfktu/Python-prog/blob/master/lesson08/flowchart.png)  
Программный код состоит из нескольких модулей:  
- [***main.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson08/main.py) - из этого модуля осуществляется запуск программы. Справочник внутри программы представлен в виде списка кортежей. Каждый кортеж *(Имя, Фамилия, Номер телефона, Описание)*. При запуске программы создаётся список *guide=[]*, и при наличии файла *phonebook.csv* заполняется информацией из него. Если файл не обнаружен - работа с чистым, новым, справочником, в котором для начала следует добавить несколько контактов.
- [***dbfiles.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson08/dbfiles.py) - модуль работы с файлами:  
- *loadcsv(fname : str)* - загрузка из файла в формате *csv* с заданным именем, возвращает список кортежей;
- *exportcsv(fname: str, gd : list)* - записывает список *gd* в файл *fname* в ормате *csv* - каждый контакт отдельной строкой, элементы контакта разделены точкой с запятой;
- *exportjson(fname : str, gd : list)* - записывает список *gd* в файл *fname* в ормате *JSON*;
- *importjson(fname : str)* - загрузка из файла в формате *JSON* с заданным именем, возвращает список кортежей;
- *makebackup()* - создаёт **backup-версию** файла *phonebook.csv*. Имя файла - в формате *ггггммдд_ччммсс.backup*
- *logfile(oper : int)* - по коду операции *oper* вносит в файл *phonebook.log* дату, время, какой действие выполнялось. Файл дополняется, логи с прошлых сеансов сохраняются.  
- [***database.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson08/database.py) - модуль работы со справочником (списком):  
- *printtable(guide : list, printall = True)* - выводит на экран справочник в виде таблицы. Параметр *printall* указывает следует или нет под таблицей печатать пункты меню;
- остальные функции данного модуля рассматривать не стоит, т.к. были созданы как заготовки, но, в дальнейшем, все задуманные действия перекочевали в модуль *menu.py*
- [***menu.py***](https://github.com/dtnfktu/Python-prog/blob/master/lesson08/menu.py) - модуль обработки выбранного пункта меню. Для выбора действия следует ввести число ему соответствующее и нажать Enter.
- *inputrec()* - диалог ввода нового контакта в консоли, возрвщает кортеж;
- *delrec()* - диалог удаления контакта - указывается порядковый номер контакта в таблице;
- *searchrec(ls : list)* - диалог и поиск записей по ключу: запрашивается фрагмент имени или фамилии, переводится в нижний регистр букв, с помощью *filter* и *lambda* отфильтровываются удовлетворяющие записи. Если записей нет, то возвращается пустой спиок;
- *exportdata(gd : list)* - диалог выбора формата для сохранения отображаемого справочника в файл;
- *importdata()* - диалог загрузки справочника из файла;
- *editrec(gd : list)* - диалог редактирования контакта - необходимо указать порядковый номер в таблице

<span style="color:red">**Важно! Работа выполнена, отлажена, проверена в Visual Studio Code, операционная система Ubuntu 22.04 LTS (Linux). При запуске в ОС Windows наблюдается некорректная работа части функционала, связанного с вводом с консоли слов на кириллице - добавление новой записи, поиск по фрагменту фамилии и имени. При этом с латиницей таких проблем не обнаружено.**</span>  

[В начало](#texthead)  