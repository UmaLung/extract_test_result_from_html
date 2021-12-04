
def extract_item (html_file_name):
    csv_file_name = html_file_name.replace('html', 'csv')
    data = []
    with open('input_HTML.html', 'r', encoding = 'utf-8') as f:
        for line in f:
            data.append(line.strip().replace('<td>', '').replace('</td>', '').replace('<sub>', '').replace('</sub>', ''))
        print(len(data))

    res = [x for x, z in enumerate(data) if '</tr>' in z]   # use '</tr> as seperator'
    print(len(res))
    with open('item.csv', 'w', encoding = 'utf-8') as f:
        for i in range(len(res) - 1):
            item = ''
            for n in range(2, 13):
                item += data[res[i] + n ] + ','
            # print(item)
            f.write(item + '\n')


if __name__ == '__main__':
    import sys
    # extract_item(sys.argv[1])
    extract_item('input_HTML.html')

    
