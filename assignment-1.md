# Assignment 1 for Business Intelligence
#### By Disturbed Unit

1. We ran the file through Terminal. Initially firing up under the Virtual Machine, so we could access it using SSH.
  After navigating to the /synced_folder/assignments/assignment_1/ we were able to run the python file using the command
  `python assignment_1.py`.
  We were able to see using the `ls` command that there were only three files prior to running the python script. Afterwards,
  there were five, so it created two files in total:
    1. **price_list.csv**
    1. **prices.png**
    
    ![alt text](https://github.com/semester-groupies/disturbed-unit/blob/master/resources/files.png "Screenshot of generated files")

    
---
    
2. The aforementioned two files is a **comma separated values** file, and an **image** (portable networks graphics).

---

3. **3307228.119047619** (which is what?)

---

4. In the following lines we will walk through the code, explaining what it does:

`import os`
> import os is a python module that enables us to use os dependent functionality. http://www.pythonforbeginners.com/os/pythons-os-module

`import csv`
> import csv enables us to read and write csv files, as well as many other functions

`import requests`
> import requests allows us to make easy http requests 

`import platform`
> import platform allows us to access the underlying platforms data, such as, hardware and os.

`import statistics`
> import statistics helps us to create statistics. Features include mean, median, mode, standard deviation and variance.

`import matplotlib`
> import matplotlib is a plotting library for python, for making graphs, for example (prices.png)
> import matplotlib.pyplot as plt extends the functionality of the plotter.

```
def download_txt(url, save_path='./downloaded'):
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)
```
> The download_txt is a function which takes two parameters. We can tell that actually only one parameter is needed to invoke the function, since the save_path parameter has a default value bound to it, if not specified otherwise.
The function sends out a Get request to a specified URL, and assigns the response into the, well, response variable. Using the open() method, we're accessing the URL's response, and with the specified download filepath and open-mode _wb_, being _write_ and _binary_. So we're opening the file in binary + writing mode, and assigning this writer to the f variable. The function ends off with calling the write() method, generating the content to the file in the /downloaded folder.
```
def generate_csv(txt_input_path, csv_output_path):
    with open(txt_input_path, encoding='utf-8') as f:
        txt_content = f.readlines()

    rows = [['street', 'city', 'price', 'sqm', 'price_per_sqm']]
    for line in txt_content:
        line = line.rstrip().replace('  * ', '')
        address, price, sqm = line.split('\t')
        street, city = address.split('; ')
        price_per_sqm = int(price) // int(sqm)
        row = (street, city, price, sqm, price_per_sqm)
        rows.append(row)

    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None

    with open(csv_output_path, 'w', newline=newline, encoding='utf-8') as f:
        output_writer = csv.writer(f)
        for row in rows:
            output_writer.writerow(row)
```
> The generate_csv is another function with nothing magical over it. It's quite simple a function that generates a comma separated values (CSV) file based on an input_path (to a text file of some sort), and an output_path (now in csv format). Using the open() method to read the existing file, UTF-8 encoded, and assigning it to the txt_content variable.

> A for-loop is now being used to iterate over each line from the file, converting it into csv format. Then there's a check for what operating system is in use since it has an affect on how new lines are written programmatically.

> Lastly we're using the open() method once more, but this time to write to the new file. We give the method our desired parameters, and the output writer now iterates all the rows / lines from our newly converted content, generating a csv file.
```
def read_prices(csv_input_path):
    with open(csv_input_path, encoding='utf-8') as f:
        reader = csv.reader(f)
        _ = next(reader)

        idxs = []
        prices = []
        for row in reader:
            _, _, price, _, _ = row
            idxs.append(reader.line_num)
            prices.append(int(price))

    return list(zip(idxs, prices))
```

```
def compute_avg_price(data):
    _, prices = zip(*data)
    avg_price = statistics.mean(prices)

    with open('/tmp/avg_price.txt', 'w', encoding='utf-8') as f:
        f.write(str(avg_price))

    return avg_price
```

```
def generate_plot(data):
    x_values, y_values = zip(*data)
    fig = plt.figure()
    plt.scatter(x_values, y_values, s=100)
    fig.savefig('./prices.png', bbox_inches='tight')
```

```
def run():
    file_url = 'https://raw.githubusercontent.com/datsoftlyngby/' \
               'soft2017fall-business-intelligence-teaching-material/master/' \
               'assignments/assignment_1/price_list.txt'
    txt_file_name = os.path.basename(file_url)
    txt_path = os.path.join('./', txt_file_name)
    download_txt(file_url, txt_path)
    csv_file_name = 'price_list.csv'
    csv_path = os.path.join(os.getcwd(), csv_file_name)
    generate_csv(txt_path, csv_path)
    data = read_prices(csv_path)
    avg_price = compute_avg_price(data)
    print(avg_price)
    generate_plot(data)
```

```
if __name__ == '__main__':
    run()
```
