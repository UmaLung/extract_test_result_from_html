html_file_name = 'input_HTML.html'
csv_file_name = html_file_name.replace('html', 'csv')

def extract_item ():
    data = []
    with open(html_file_name, 'r', encoding = 'utf-8') as f:
        for line in f:
            data.append(line.strip().replace('<td>', '').replace('</td>', '').replace('<sub>', '').replace('</sub>', ''))

    res = [x for x, z in enumerate(data) if '</tr>' in z]   # use '</tr> as anchor'
    with open(csv_file_name, 'w', encoding = 'utf-8') as f:
            for i in range(len(res) - 1):
                item = ''
                for n in range(2, 13):
                    item += data[res[i] + n ] + ','
                # print(item)
                f.write(item + '\n')


    
if __name__ == '__main__':
     extract_item ()