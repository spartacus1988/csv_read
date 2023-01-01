import csv
import config
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time 

timedelay=0.2
Ur_list = []
Fiz_list = []
Trash_list = []
Ur_dictionary = {}
Fiz_dictionary = {}
Trash_dictionary = {}


def main():
    print("Hello World!")
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options) 
    driver.set_window_size(1920, 1080)
    driver.get("https://torsed.voskhod.ru/app/#!")

    
    delay = 25 # seconds
    try:
        login_input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//input')))
        print ("Page is ready!")
        login_input = driver.find_elements(By.XPATH, '//input')
        print(login_input) 
        login_input[0].send_keys(config.username)
        login_input[1].send_keys(config.password)
        
        button_login = driver.find_element(By.XPATH, '//div[@class="v-button v-widget cuba-login-submit v-button-cuba-login-submit v-has-width"]')
        button_login.click()
   
        button_spravochniki = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Справочники"]')))
        button_spravochniki = driver.find_element(By.CSS_SELECTOR, "span[class='v-menubar-menuitem']")
 
        print ("Page is ready!")

        button_spravochniki = driver.find_element(By.CSS_SELECTOR, '.cuba-main-menu.v-menubar')

        print ("tab_names " + button_spravochniki.text)
 
        button_spravochniki = driver.find_element(By.CSS_SELECTOR, "div[tabindex='0']")

        button_spravochniki = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div[1]/div/div/div[3]/div/span[5]")
        action = ActionChains(driver)
        action.move_to_element(button_spravochniki)
        action.click(button_spravochniki)
        action.perform()

        #button_Kontragenty
        find_and_click_element_by_path(driver, delay, '/html/body/div[3]/div[2]/div/div/span[6]/span[1]')
      

        #button_Ur_litca 
        find_and_click_element_by_path(driver, delay, '/html/body/div[3]/div[3]/div/div/span[1]/span[1]')                                                                   
     

        #button_create_new
        find_and_click_element_by_path(driver, delay, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div[1]/div/div[1]/div/div[1]/div')
       
        #name_input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[4]/input')))
        #name_input.send_keys('Наименование')
        
        read_from_csv_and_write_to_database_Ur(driver, delay, filename='Юридическое лицо.csv')
    



    except TimeoutException:
        print ("Loading took too much time!")
    
def write_name_Ur(name_Ur,driver, delay):
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[4]/input')))
    input.send_keys(name_Ur)
    return

def write_fullname_Ur(fullname_Ur,driver, delay):
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[6]/div/textarea')))
    input.send_keys(fullname_Ur)
    return

def write_telephone_Ur(telephone_Ur,driver, delay):
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[10]/input')))
    input.send_keys(telephone_Ur)
    return

def write_fax_Ur(fax_Ur,driver, delay):
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[12]/input')))
    input.send_keys(fax_Ur)
    return

def write_E_mail_Ur(E_mail_Ur,driver, delay):
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[14]/input')))
    input.send_keys(E_mail_Ur)
    return

def write_site_Ur(site_Ur,driver, delay):
    find_and_click_element_by_path(driver, delay, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[16]/div/div/div[3]/div')
    time.sleep(timedelay)
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[16]/div/div/div[1]/div/a')))
    #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[16]/div/div/div[1]/div/a
    #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[16]/div/div/div[1]/div/a/span
    #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[16]/div/div
    #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[16]/div/div/div[1]/div/a/span
    #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[16]/div/div
    #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[16]/div/div/div[1]/div/a
    #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[15]
    time.sleep(timedelay)
    input.send_keys(Keys.RETURN)
    input.send_keys(site_Ur)
    input.send_keys(Keys.RETURN)

    return

def write_INN_Ur(INN_Ur,driver, delay):
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[18]/input')))
    input.send_keys(INN_Ur)
    return

def write_KPP_Ur(KPP_Ur,driver, delay):
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[23]/input')))
    input.send_keys(KPP_Ur)
    return

def write_OGRN_Ur(OGRN_Ur,driver, delay):
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[27]/input')))
    input.send_keys(OGRN_Ur)
    return

def write_OKOPF_Ur(OKOPF_Ur,driver, delay):
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[29]/div/input')))
    input.send_keys(OKOPF_Ur)
    input.send_keys(Keys.RETURN)
    span = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr/td/span')))
                                                                                        #/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr/td/span
                                                                                        #/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr[2]/td
    span.click()
    return

def write_Type_Ur(Type_Ur, driver, delay):
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[41]/div[2]/input')))
    input.send_keys(Type_Ur)
    input.send_keys(Keys.RETURN)

    span = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr/td/span')))
    #/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr[2]/td
    #/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr[10]/td
    #/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr[10]/td/span
    #/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr/td/span
    span.click()
    return

def write_place_of_creating(place_of_creating, driver, delay):
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[8]/div[2]/div/div[1]/input')))
    input.send_keys(place_of_creating)
    input.send_keys(Keys.RETURN)
    span = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr[1]/td/span')))
    span.click()
    return

def write_Nerezident(nerezident, driver, delay):
    if nerezident == 'Нет':
        print('inside nerezident if')
        find_and_click_element_by_path(driver, delay, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[33]/span/label') 
        #chechbox = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[33]/span/label')))
    elif nerezident == 'Да':
        pass
    else:
        pass
    return

def read_from_csv_and_write_to_database_Ur(driver, delay, filename='Юридическое лицо.csv'):
    with open(filename) as f:
        #Ur_list = []
        #Fiz_list = []
        #Trash_list = []
        reader = csv.DictReader(f)
        i=0
        for row in reader:
            print(row)
            i+=1
            #if i == 1:
                #continue
            print(row['Наименование'])
            
            
            write_name_Ur(row['Наименование'],driver, delay)
            time.sleep(timedelay)
            write_fullname_Ur(row['Полное наименование'],driver, delay)
            time.sleep(timedelay)
            write_place_of_creating('Тверская область',driver, delay)
            time.sleep(timedelay)
            write_telephone_Ur(row['Телефон'],driver, delay)
            time.sleep(timedelay)
            write_fax_Ur(row['Факс'],driver, delay)
            time.sleep(timedelay)
            write_E_mail_Ur(row['E-mail'],driver, delay)
            time.sleep(timedelay)
            #write_site_Ur(row['Сайт'],driver, delay)
            #time.sleep(timedelay)
            write_INN_Ur(row['ИНН'],driver, delay)
            time.sleep(timedelay)
            write_KPP_Ur(row['КПП'],driver, delay)
            time.sleep(timedelay)
            write_OGRN_Ur(row['ОГРН'],driver, delay)
            time.sleep(timedelay)
            write_OKOPF_Ur(row['ОКОПФ'],driver, delay)
            time.sleep(timedelay)


            
            driver.execute_script("window.scrollTo(0, 1080)")
            time.sleep(timedelay)
         

            write_Type_Ur(row['Тип организации'],driver, delay) 
            time.sleep(timedelay)
            write_Nerezident(row['Нерезидент'],driver, delay)
            time.sleep(timedelay)
    return


def find_and_click_element_by_path(driver, delay, path):
    button = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, path)))
    action = ActionChains(driver)
    action.move_to_element(button)
    action.click(button)
    action.perform()
    return


def write_csv(data, name):
    with open(name, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=list(data[0].keys()), extrasaction='ignore', delimiter = ',', quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for d in data:
            writer.writerow(d)
        return


def split_main_csv_to_3(name='Корреспонденты.csv'):
    with open('Корреспонденты.csv') as f:
        #Ur_list = []
        #Fiz_list = []
        #Trash_list = []
        reader = csv.DictReader(f)
        i=0
        for row in reader:
            print(row)
            i+=1
            print(row['ВидКорреспондента'])
            if row['ВидКорреспондента'] == 'Юридическое лицо':
                print('add to Ur.csv')
                Ur_dictionary = row
                Ur_list.append(Ur_dictionary)
            elif row['ВидКорреспондента'] == 'Физическое лицо':
                print('add to Fiz.csv')
                Fiz_dictionary = row
                Fiz_list.append(Fiz_dictionary)
                #i+=1
                #if i>2:
                #    break
            else:
                print('add to NotValid.csv')
                Trash_dictionary = row
                Trash_list.append(Trash_dictionary)
                #i+=1
                #if i>2:
                #    break
              ##if i>400:
        print('Ur_list = ')
        print(Ur_list) 
        write_csv(Ur_list, 'csv_write_Ur.csv')
        print('Fiz_list = ')
        print(Fiz_list)
        write_csv(Fiz_list, 'csv_write_Fiz.csv')
        print('Trash_list = ')
        print(Trash_list)
        write_csv(Trash_list, 'csv_write_Trash.csv')
                ##break
        return


if __name__ == "__main__":
    main()

