#<<<to check if the file exist >>>
import os # import the operaing system library in order to communicate with the OS of the laptop
product = []
#if os.path.isfile('product.csv') # relative path
if os.path.isfile('H:\My Drive\Learning\Python\Product\product.csv'): # absolute path, to check if the file exists
	print('the file exists')
	#<<read the file that was saved already >>>
	with open('product.csv','r', encoding = 'utf-8') as file: # encoding is important , otherwise , it will have encoding issues
		for line in file:
			print(x, line)
			# in order to skip the header ,i.e. item , price, continue is introduced 
			if 'item,price' in line:
				continue # continue is to skip the code in this round of loop but break is to jump out of the entire loop 
			name,price = line.strip().split(',') # strip is to remove the end of /n, then split per ,
			#^^^^^^^^^^ equal to the following 
			#name = line(0)
			#price = line(1)
			product.append([name,price])
	print('final',product)
else:
	print('file can not be found')

# <<<記帳program >> 2D list>>> 
while True:
	name = input('input the item name ')
	if name == 'q':
		break
	price = input('input the price ')
	# <<<to build the small list>>>
	
	#p = []
	#p.append(name)
	#p.append(price)
	
	#<<< small list completed >>>
	product.append([name,price]) # put the small list into big list

print(product[0][0]) # the 1st box of Product then the 1st element of the 1st box
print(product[1][1])

# <<<pull the name and price out of product through FOR>>>
for p in product:
	print(p)

with open('product.txt','w') as file:
	for p in product:
		file.write(p[0] + ',' + p[1] + '\n' )

with open('product.csv','w', encoding = 'utf-8') as file:  # utf-8 is the most common "encoding" to avoid error due to Chinese
	#file.write('item,price\n')  # adding header in the table, English is ok
	file.write('項目,價格\n')  # Chinese causing error 

	for p in product:
		file.write(p[0] + ',' + p[1] + '\n' )
