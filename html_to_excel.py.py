# This script converts the test result from the html output of a TLF3000 to .csv file. 
# Type "py html_to_excel.py <name1>, where <name1> is the html file.

def read_html_file(html_file_name):
    data = []
    with open(html_file_name, 'r', encoding = 'utf-8') as f:
        for line in f:  # remove unnecessary lines
            data.append(line)
    return data


def extract_wanted_lines(data):
    new = []
    for line in data:
        if '<h1>' in line:
            new.append(line.strip().replace('<h1>', '***'))
        elif '<th>' in line:
            new.append(line.strip().replace('<th>', '').replace('</th>', ''))        
        elif '<td>' in line:
            new.append(line.strip().replace('<td>', '').replace('</td>', ''))
        else:
            continue        
    return new


def concatenate_items(new):
    merge = []
    item = None
    for line in new:
        if '***' in line:
            merge.append(line.replace('</h1>', '***'))
            continue
        elif '_LE_CA_' in line:
            item = line + ','
            continue
        elif 'Test' in line:
            item = line + ','
            continue
        elif 'PASS' in line:
            merge.append(item + line)
            item = None
            continue
        elif 'FAIL' in line:
            merge.append(item + line)
            item = None
            continue
        elif 'Result' in line:
            merge.append(item + line)
            item = None
            continue
        if item:
            item += line + ','
    return merge


def save_to_csv(csv_file_name, merge):
    with open(csv_file_name, 'w', encoding = 'utf-8-sig') as f:
        for line in merge:  # remove unnecessary lines
            f.write(line + '\n')


def main(html_file_name):
    csv_file_name = html_file_name.replace('html', 'csv')
    data = read_html_file(html_file_name)
    new = extract_wanted_lines(data)
    merge = concatenate_items(new)
    save_to_csv(csv_file_name, merge)



if __name__ == '__main__':
    import sys
    main(sys.argv[1])

    
