import pyperclip

input_data = pyperclip.paste()
# output_data = input_data.replace('\t', ', ')
# output_data = output_data.replace('\r\n', '], \r\n[')
# output_data = output_data[:-5]
# output_data = '[\r\n[' + output_data + '\r\n]'
# output_data = output_data.replace('\r\n', ',\n')
output_data = input_data.replace('\r\n', ',\r\n')
output_data = output_data.replace('\r\n,', '')
output_data = output_data[:-3]

pyperclip.copy(output_data)
