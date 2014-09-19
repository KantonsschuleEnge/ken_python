#!/usr/bin/python3

# gregor luedi
# 17.9.2014

def main():
	max = int(input('Geben Sie die maximale Anzahl ein: '))
	for i in range(1,max+1):
    		if i%7==0 or str(i).find('7')!=-1:
        		print('Hugo')
    		else:
        		print(i, end=' ')
	input('Press Enter to stop')


if __name__ == '__main__':main()

