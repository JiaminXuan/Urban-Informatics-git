import sys,os
name= ['Agency','# Of Positions','Business Title','Civil Service Title','Salary Range From','Salary Range To','Salary Frequency','Work Location','Division/Work Unit','Job Description','Minimum Qual Requirements','Preferred Skills','Additional Information','Posting Date']
def executeCommands(commandFileName):
	f = open(commandFileName)
	for line in f:
		executeCommand(line.strip())
def executeCommand(commandLine):
	tokens = commandLine.split('|') #assume that this symbol is not part of the data
	command = tokens[0]
	parameters = tokens[1:]

	if command == 'insert':
		insert(parameters)
	elif command == 'delete_all':
		delete_all(parameters)
	elif command == 'update_all':
		update_all(parameters)
	elif command == 'find':
		find(parameters)
	elif command == 'clear':
		clear()
	elif command == 'dump':
		dump()
	elif command == 'view':
		view(parameters)
	else:
		print 'ERROR: Command %s does not exist' % (command,)
		assert(False)
def clear():
	job_list.clear()

def insert(params):
	job_id=int(params[0])
	job_detail=params[1:]
	if job_id in job_list.keys():
		pass
	else:
		job_list[job_id]=job_detail
def dump():
		for job_id in sorted(job_list.keys()):
			print_word=str(job_id)+"|"+"|".join(job_list[job_id])
			print print_word
def save():
	open('job_file.txt','w').close()
	with open('job_file.txt','w') as print_file:

		for job_id in sorted(job_list.keys()):
			print_word=str(job_id)+"|"+"|".join(job_list[job_id])
			print_file.writelines(print_word+'\n')
def update_all(params):
	find_id=params[0]
	find_val=params[1]
	update_id=params[2]
	update_val=params[3]
	counter=0
	if find_id=='Job ID':
		if int(find_val) in job_list.keys():
			job_list[int(find_val)][name.index(update_id)]=update_val
			counter+=1
	else:
		for job in job_list.values():
			if job[name.index(find_id)]==find_val:
				counter+=1
				job[name.index(update_id)]=update_val
	print counter

def delete_all(params):
	find_id=params[0]
	find_val=params[1]
	if find_id=='Job ID':
		del job_list[int(find_val)]
	else:
		rmint=[]
		for job_id in job_list:
			if job_list[job_id][name.index(find_id)]==find_val:
				rmint.append(job_id)
		for item in rmint:
			del job_list[item]
def view(params):
	output=[]
	for job_id, job in job_list.iteritems():
		for find_id in params:
			if find_id=='Job ID':
				print str(job_id)+'|',
			else:
				print job[name.index(find_id)]+'|',
		print 
def find(params):
	find_id=params[0]
	find_val=params[1]
	if find_id=='Job ID':
		if int(find_val) in job_list.keys():
			print_word=find_val+"|"+"|".join(job_list[int(find_val)])
			print print_word
	else:
		rmint=[]
		for job_id in job_list:
			if job_list[job_id][name.index(find_id)]==find_val:
				rmint.append(job_id)
		for item in rmint:
			print_word=str(item)+"|"+"|".join(job_list[item])
			print print_word
def load():
	if os.path.isfile('job_file.txt'):
		with open('job_file.txt','r') as print_file:
			for line in print_file:
				records=line.split('|')
				job_id=int(records[0])
				job_detail=records[1:]
				job_list[job_id]=job_detail
	else:
		open('job_file.txt','w').close()
if __name__ == '__main__':
	job_list={}
	load()
	clear()
	executeCommands(sys.argv[1])
	save()
