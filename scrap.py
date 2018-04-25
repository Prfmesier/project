from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time 



chrome_path = r"/Users/polruizfarre/Downloads/chromedriver"
driver = webdriver.Chrome(chrome_path)

	
def llistat():
	file = open('llistainf.txt', 'w')
	driver.get("https://influence.co/category/coffee")
	wait = WebDriverWait(driver, 10)
	wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div[1]/div[1]")))
	elem = driver.find_elements_by_xpath("/html/body/div[3]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/p[1]/a")
	elem2 = driver.find_elements_by_xpath("/html/body/div[3]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/p[1]/a")
	file.write(elem[0].text+';')
	file.write(elem2[0].text+';')
	
	for x in range(24):
		for y in range(4):
			elem = driver.find_elements_by_xpath("/html/body/div[3]/div[2]/div/div/div["+str(x+2)+"]/div["+str(1+y)+"]/div[1]/div[1]/p[1]/a")
		
			file.write(elem[0].text+';')
	
	return True


def entrar():
	file = open('llistainf.txt', 'r')
	lla = file.read()
	ll = lla.split(';')
	ll.pop()
	followers = []
	driver.get("https://www.instagram.com/")
	wait = WebDriverWait(driver, 10)

	#LOG IN A IG
	wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')))
	driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')[0].click()
	wait = WebDriverWait(driver, 10)
	wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div[1]')))
	
	#LOG IN A IG
	element = driver.find_element_by_name("username")
	element.send_keys('*********')
	element = driver.find_element_by_name('password')
	element.send_keys('********')
	driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/span/button')[0].click()
	
	#BUSCA CADA INFLUENCER
	"""
	x='@polruizfarre'
	wait = WebDriverWait(driver, 10)
	wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]')))
	el = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
	el.send_keys(x)
	wait = WebDriverWait(driver, 10)
	wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div/div/span')))
	el = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div/div/span')
	if el.text == x[1:]:
		el.click()
	"""
	llista=[]
	for x in ll:
		print(x)
		
		wait = WebDriverWait(driver, 100)
		wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]')))
		el = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
		
		try:
			el.clear()
		except:
			continue
		time.sleep(2)
		try:
			el.send_keys(x)
			#Desplega la llista de contes amb aquell nom

			wait = WebDriverWait(driver, 100)
			wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a/div')))
			time.sleep(0.5)
			el = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div/div/span')
			
		except:
			print('no va send_keys')


		try:
			el2 = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/div')
			print(el2.text)
			ll.remove(x)
			print('algo va mal 1')
			
		except:
			if el.text == x[1:]:
				el.click()
		
		time.sleep(2)


		try:
			
			driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/header/section/ul/li[3]/a').click()
		except:
			print('no va lo de clicar following')
		
		try:
			wait = WebDriverWait(driver, 10)
			wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/div/div[2]/div/div[2]')))
		except:
			print('no va lo de wait')
		try:
			
			
			wait = WebDriverWait(driver,10)
			wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/div/div[2]/div/div[2]')))
			
			
			driver.implicitly_wait(15)
			centerPanel = driver.find_element_by_css_selector("#center-panel > div[class*='hideScroll-wrapper']")
			jsScript = """
     			   function move_up(element) {
      			      element.scrollTop = element.scrollTop - 1000;
      			  }

      			  function move_down(element) {
       			     element.scrollTop = element.scrollTop + 1000;
       			 }

       			 move_down(arguments[0]);
      			  move_down(arguments[0]);
      			  """
			driver.execute_script(jsScript, centerPanel)

			time.sleep(3) 

			jsScript = """
   			     function move_up(element) {
     			       element.scrollTop = element.scrollTop - 1000;
      			  }

      			  function move_down(element) {
       			     console.log('Position before: ' + element.scrollTop);
       			     element.scrollTop = element.scrollTop + 1000;
       			     console.log('Position after: ' + element.scrollTop);
       			 }

      			  move_up(arguments[0]);
     			   """
			driver.execute_script(jsScript, centerPanel)
			
		except:
			print('no va la merda de tira cap avall')
		try:
			
			el = driver.find_elements_by_class_name('_6e4x5')
		except:
			print('no va la merda de recopilar les llistes')

	return llista
	
	

entrar()
		

