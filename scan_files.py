cnt=0
def main():
	import os
	import sys

	plat=sys.platform
	if(plat=='win32'):
		slash='\\'
	else:
		slash='/'

	def read_permissions(filepath):
	    '''Checks the read permissions of the specified file'''
	    try:
	    	os.listdir(filepath)
	        # os.access(filepath, os.R_OK)
	        # os.access(filepath, os.W_OK)
	         # Find the permissions using os.access
	    except IOError:
	        return False

	    return True

	def check (str3):
	    try:
	        os.stat(str3).st_size
	    except IOError:
	        return False

	    return True

	
	files=[[-1,'a'],[-1,'b'],[-1,'c'],[-1,'d'],[-1,'e'],[-1,'f'],[-1,'g'],[-1,'h'],[-1,'i'],[-1,'j']]
	def funt(str2):
		if read_permissions(str2):
			
			for x in os.listdir(str2):

				if(str2==slash):
					str=""
				else:
					str=str2
				if os.path.isdir(str+slash+x):
					funt(str+slash+x)# using recursion 
				elif not os.path.islink(str+slash+x):#so that shortcut are counted as files.
					# print(str+slash+x)
					global cnt
					cnt+=1
					print('  Number of files scaned in the given folder-->',cnt,end="\r")
					if check (str+slash+x):

						size_mb=int(os.stat(str+slash+x).st_size)
						for f in files:
							if(size_mb>=f[0]):
								f[0]=size_mb
								f[1]=str+slash+x
								files.sort()
								break
			# else:
		# 	continue
	# except:	
	# 	print(str2)

			#print(size_mb/(1024*1024),'MB')
	# print '\033[1;48mHighlighted Crimson like Chianti\033[1;m'
	print('Please read the documentation of this script before using it')
	print(r'Enter the folder path, example-C:\Users\Admin\Downloads "if you want to scan download" ?')
	folder=input()
	if folder[-1]==':':
		folder+='/'
	# print(folder)
	if not os.path.isdir(folder):
		print("There is no such folder path")
		return 
	else:
		funt(folder)

	#result
	print(" ")
	print("*****************************RESULT*****************************")
	count=0
	for f in reversed(files):
		count+=1
		print(count,end="")
		print(') ',end="")
		# if(f[0]==-1 and count==1 ):
			#print("No files in such folder exits")
		if(f[0]==-1):
			print("No more file exits")
			return 
		else:
			print(round(f[0]/(1024*1024),3),'MB -->',f[1])
	return

if __name__ == "__main__":main()
k=input("Press enter to exit ;)")
