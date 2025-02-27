# Регулярки очень быстрые в python, они тягаются по скорости с C и C++

import re

text = """История России насчитывает более тысячи лет, начиная с переселения восточных славян на Восточно-Европейскую 
(Русскую) равнину в VI-VII веках, впоследствии разделившихся на русских, украинцев и белорусов. Историю страны можно
 поделить примерно на семь периодов: древнейшая (догосударственная) (до конца IX века н. э.), Киевская Русь 
 (древнерусское государство) (до середины XII века), период раздробленности (до начала XVI века), единое государство 
 (с 1547 года царство) (конец XV века-1721), империя (1721-1917), советский период (1917-1991) и новейшая история 
 (с 1991 года).
"""

info = '10 EUR, 20 EUR, 30 EUR - EURO EUROPE'

text_2 = '''Знаки препинания: первая и вторая запятая - причастный оборот, третья запятая - подчинительная связь между
предложениями, четвертая запятая - сочинительная связь между предложениями, пятая запятая - сочинительная связь между
предложениями, шестая запятая - подчинительная связь между предложениями, седьмая запятая - подчинительная свзяь между
предложениями.'''

# Когда сложные регулярки, лучше указывать комментарием, что она делает, как ниже
# Находит года в тексте, четырёхзначные
years = re.findall(r'\d{4}', text)
periods = re.findall(r'\d{4}-\d{4}', text)
result = re.sub(r'\bEUR\b', 'USD', info)
words = re.split(r'\W+', text_2)

if __name__ == '__main__':
    print(years)
    print(periods)
    print(result)
    print(words)
    # В выводе есть пустая строка в конце, её нужно обрезать