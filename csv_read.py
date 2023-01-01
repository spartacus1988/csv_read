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
        #button_Kontragenty = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/span[6]/span[1]")
        #action = ActionChains(driver)
        #action.move_to_element(button_Kontragenty)
        #action.click(button_Kontragenty)
        #action.perform()

        #button_Ur_litca 
        find_and_click_element_by_path(driver, delay, '/html/body/div[3]/div[3]/div/div/span[1]/span[1]')                                                                   
        #button_Ur_litca = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/span[1]/span[1]")
        #action = ActionChains(driver)
        #action.move_to_element(button_Ur_litca)
        #action.click(button_Ur_litca)
        #action.perform()

        #button_create_new
        find_and_click_element_by_path(driver, delay, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div[1]/div/div[1]/div/div[1]/div')
        #button_create_new = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div[1]/div/div[1]/div/div[1]/div')))
        #action = ActionChains(driver)
        #action.move_to_element(button_create_new)
        #action.click(button_create_new)
        #action.perform()
    
    except TimeoutException:
        print ("Loading took too much time!")
    

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

