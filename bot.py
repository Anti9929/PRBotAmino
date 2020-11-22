import amino
import time
import sys
from colorama import init, Fore, Style
init()

line = "PRBOTAMINO. SCRIPT BY FATZELF"

for x in line:
	print(Fore.GREEN + x, end='')
	sys.stdout.flush()
	time.sleep(0.1)

print(Fore.RED + '\nEnter your email:' + Fore.YELLOW, end='')
email = input( )
print(Fore.RED + 'Enter your password:' + Fore.YELLOW, end='')
password = input( )
print(Fore.RED + 'Enter your message:' + Fore.YELLOW, end='')
ad = input()

lis = []

client = amino.Client()
client.login(email=email, password=password)

subclients = client.sub_clients()
for name, id in zip(subclients.name, subclients.comId):
	print(name, id)

print(Fore.RED + 'Enter communityId: ' + Fore.YELLOW, end='')
comId = input( )

subclient = amino.SubClient(comId=comId, profile=client.profile)

members = subclient.get_online_users()

for name, id in zip(members.profile.nickname, members.profile.userId):
	chatThreads = subclient.get_chat_threads().chatId

	if ad not in chatThreads:
			lis.append(id)
			time.sleep(4)
			subclient.start_chat(userId=lis, message=ad)
			print('Отправил рекламу', name)
			lis.remove(id)
