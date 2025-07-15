# task manager
import csv
try:
	with open("tasks.csv","r")as file:
		read = list(csv.reader(file))
		print("last added task: ",read[-1])
except FileNotFoundError:
	with open("tasks.csv","w",newline='')as file:
		write = csv.writer(file)
		write.writerow(["taskname","lastdate","status"])
while True:
	ask = input("1. Add New Task\n2. View All Tasks\n3. Mark Task as Completed\n4. Delete a Task\n5. View Pending Tasks\n6. Exit\n enter: ")
	if ask =="1":
		a = input("enter in format(taskname,lastdate,status)\n ")
		with open ("tasks.csv","a",newline="")as file:
			write = csv.writer(file)
			write.writerow(a.split(","))
	elif ask=="2":
		with open("tasks.csv","r")as file:
			read = csv.reader(file)
			for row in read:
				print(row)
	elif ask=="3":
		a = input("which task you wanna mark/update format(taskname,lastdate,status): ")
		b = a.split(",")[0].strip().lower()
		print(b)
		with open("tasks.csv","r")as file:
			read = list(csv.reader(file))
		with open("tasks.csv","w",newline='')as file:
			write = csv.writer(file)
			for row in read:
				if row[0].strip().lower() == b:
					write.writerow(a.split(","))
				else:
					write.writerow(row)
	elif ask=="4":
		a = input("what do you wanna remove(just name)")
		with open("tasks.csv","r")as file:
			read = list(csv.reader(file))
		with open("tasks.csv","w",newline='')as file:
			write = csv.writer(file)
			for row in read:
				if a.strip().lower() != row[0].strip().lower():
					write.writerow(row)
	elif ask=="5":
		with open("tasks.csv","r")as file:
			read = csv.reader(file)
			for row in read:
				if row[-1].strip().lower() == "pending":
					print(row)
	elif ask=="6":
		print("thx")
		break
	else:
		print("select from 1-6")