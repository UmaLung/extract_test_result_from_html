# This script converts the test result from the html output of a TLF3000 to .csv file. 
# Type "py html_to_excel.py <name1>, where <name1> is the html file.
# Modify the judge condition of "# start of a row" for the latest html format: name of test items have been changed.

def read_html_file(html_file_name):
    data = []
    with open(html_file_name, 'r', encoding = 'utf-8') as f:
        for line in f:  # remove unnecessary lines
            data.append(line)
    return data


def concatenate_items(new):
    """Extract necessary information from raw data.
    Reconstruct as 2D format """

    merge = []
    item = None
    for line in new:
        if ('<p>' in line) or ('<h1>' in line):
            merge.append(line.strip().replace('<h1>', '***').replace('</h1>', '***').replace('<p>', 'Start/Stop Time:').replace('</p>', ''))
            continue
        elif ('_LE_CA_' in line) or ('<th>Test</th>' in line) or ('RF-PHY' in line):   # start of a row   
            item = line.strip().replace('<th>', '').replace('</th>', '').replace('<td>', '').replace('</td>', '') + ','
            continue
        elif ('<th>Result</th>' in line) or ('<td>PASS</td>' in line) or ('<td>FAIL</td>' in line):   # end of a row
            merge.append(item + line.strip().replace('<th>', '').replace('</th>', '').replace('<td>', '').replace('</td>', ''))
            item = None
            continue
        if item:
            item += line.strip().replace('<th>', '').replace('</th>', '').replace('<td>', '').replace('</td>', '') + ','
    return merge


def save_to_csv(csv_file_name, merge):
    with open(csv_file_name, 'w', encoding = 'utf-8-sig') as f:
        for line in merge:
            f.write(line + '\n')


def main(html_file_name):
    csv_file_name = html_file_name.replace('html', 'csv')
    data = read_html_file(html_file_name)
    merge = concatenate_items(data)
    save_to_csv(csv_file_name, merge)



if __name__ == '__main__':
    import sys
    main(sys.argv[1])

    
