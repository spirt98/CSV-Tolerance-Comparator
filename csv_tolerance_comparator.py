import csv

def read_csv_to_array(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=';')
        data = list(csv_reader)
        header = data[0] if data else []
        content = data[1:] if len(data) > 1 else []
        return header, content

def find_index(array, value):
    try:
        return array.index(value)
    except ValueError:
        return -1  # Возвращаем -1, если значение не найдено

def compare_with_tolerance(a, b, tolerance):
    return abs(float(a) - float(b)) <= tolerance

def is_filter(array1, array2, indices1, indices2, tolerances):
    return all(compare_with_tolerance(array1[i1], array2[i2], tol) for i1, i2, tol in zip(indices1, indices2, tolerances))

def main():
    # Укажите пути к вашим CSV файлам
    file_path1 = '1.csv'
    file_path2 = '2.csv'

    # Читаем CSV файлы и получаем заголовки и содержимое
    header1, content1 = read_csv_to_array(file_path1)
    header2, content2 = read_csv_to_array(file_path2)

    # Заголовки которые надо сравнить
    headers = ['scanId', 'distance', 'bearing', 'radialVelocity']
    # Погрешности
    tolerance = [0, 200, 2, 0.4]

    # Заполняем индексы для каждого заголовка
    header_indexs1 = []
    header_indexs2 = []
    for header in headers:
        header_indexs1.append(find_index(header1, header))
        header_indexs2.append(find_index(header2, header))

    result = [[*header1, '', *header2]]

    size1 = len(content1[0])
    size2 = len(content2[0])
    for row1 in content1:
        matched_rows = [row2 for row2 in content2 if is_filter(row1, row2, header_indexs1, header_indexs2, tolerance)]
        if matched_rows:
            result.append([*row1, '', *matched_rows[0]])
            for row2 in matched_rows[1:]:
                result.append([*([''] * size1), '', *row2])
        else:
            result.append([*row1, '', *([''] * size2)])
        result.append([*([''] * size1), '', *([''] * size2)])

    # Имя выходного CSV файла
    output_file = 'output.csv'

    # Запись массива в CSV файл с разделителем точка с запятой
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(result)

    print(f"Массив успешно записан в файл {output_file}")

if __name__ == "__main__":
    main()