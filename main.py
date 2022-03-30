from pwn import *
import paramiko
import sshtunnel
from sshtunnel import SSHTunnelForwarder
import sys

def run_tunnel(server, user, psw, port):
	ssh = paramiko.SSHClient()
	ssh.connect(server, username=user, password=psw)
	
	print('Type "quit" to quit the shell')
	
	while True:
		command = str(input("$ "))
		
		if command == "quit":
			ssh.close()
			return
		
		stdin, stdout, stderr = ssh.exec_command(command)
		print(f'{ssh_stdout.read().decode("utf-8")}')
		print(f'Errors: {ssh_stderr.read().decode("utf-8")}')	
		stdin.close()
		stdout.close()
		stderr.close()

#create a tunnel on the localhost
def create_tunnel(ip, user, psw, port):
	with sshtunnel.open_tunnel(
		(ip, 443),
		ssh_username=user,
		ssh_pkey="/var/ssh/rsa_key",
		ssh_private_key_password=pasw,
		remote_bind_address=(ip, 22),
		local_bind_address=('0.0.0.0', 10022)
	) as tunnel:
		client = paramiko.SSHClient()
		client.load_system_host_keys()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect('127.0.0.1', 10022)
		print(server.local_bind_port)
	
		inp = str(input("Enter 1 to stop the tunneling: "))
		
		if inp == 1:
			client.close()
			return
		
#test if the info were actually changed
def tester(a, b, c, d):
	if a == 'none' or b == 'none' or c == 'none' or d == -1:
		return False
	else:
		return True
	
print("[+]=================[+]")
print("|+|WELCOME IN SH3LLY|+|")
print("|+| Made by @not1m3 |+|")
print("[+]=================[+]\n")

info = ['none', 'none', 'none', 22]

while True:
	inp = str(input('$ '))
	
	if '-h' in inp:
		print("+++++++++++++++++++++++++++++++++++")
		print("This programm will help you use ssh")
		print("Commands: ")
		print("-h	show the commands")
		print("-l 	list of variabiles")
		print("-r	run the tunnel")
		print("-c	create a ssh tunnel")
		print("-server 	change the server")
		print("-user 	change the user") 
		print("-pswd	change the password")
		print("-v	show the version of Sh3lly")
		print("-q 	quit the session")
		print("+++++++++++++++++++++++++++++++++++")
	
	elif '-l' in inp:
		print("Server: " + info[0])
		print("User: " + info[1])
		print("Password: " + info[2])
		print("Port : " + str(info[3]))
			
	elif '-q' in inp:
		sys.exit()
	
	elif '-r' in inp:
		if tester(info[0], info[1], info[2], info[3]):
			run_tunnel(info[0], info[1], info[2], info[3])
		else:
			print("You haven't enter any info yet (type -l for see infos)")
	
	elif '-c' in inp:
		if tester(info[0], info[1], info[2], info[3]):
			create_tunnel(info[0], info[1], info[2], info[3])
		else:
			print("You haven't enter any info yet (type -l for see infos)")
	
	elif '-server' in inp:
		info[0] = str(input("Enter the server name: ")).rstrip()
	
	elif '-user' in inp:
		info[1] = str(input("Enter the user name: ")).rstrip()
	
	elif '-pswd' in inp:
		info[2] = str(input("Enter the password: ")).rstrip()
	
	elif '-v' in inp:
		print("1.1.0")
	else:
		print("Unknown command")
