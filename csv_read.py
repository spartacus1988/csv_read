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
    #firefox_options = Options()
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    #driver = webdriver.Firefox(options=firefox_options)
    driver = webdriver.Chrome(options=chrome_options) 
    #driver.maximize_window()
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
        
        #button_spravochnikiiiii = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Справочники")]')))
        
        #WebDriverWait wait = new WebDriverWait(driver, 3)
        #wait.until(ExpectedConditions.elementToBeClickable(By.XPATH, '//span[@class="v-menubar-menuitem-caption"]'))
        #WebDriverWait(driver, delay).until(EC.element_to_be_clickable('//span[@class="v-menubar-menuitem-caption"]'))
        
        
        #button_spravochniki = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//span[@class="v-menubar-submenu-indicator"]'))) #exeption 
        button_spravochniki = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Справочники"]')))
        button_spravochniki = driver.find_element(By.CSS_SELECTOR, "span[class='v-menubar-menuitem']")
        #button_spravochniki = driver.find_element(By.XPATH, "//*[contains(@div,'Справочники')]")
        
        #select = Select(driver.find_element(By.XPATH, '//span[@class="v-menubar-menuitem"]'))
        #select.select_by_visible_text('Справочники')
        print ("Page is ready!")
        #button_spravochniki = driver.find_element(By.XPATH, '//span[@class="v-menubar-menuitem-caption"]')


        #button_spravochniki.click()

        button_spravochniki = driver.find_element(By.CSS_SELECTOR, '.cuba-main-menu.v-menubar')


       
        print ("tab_names " + button_spravochniki.text)
        #print ("tab_names " + button_spravochniki.location_once_scrolled_into_view)
        #print ("tab_names " + button_spravochniki.location_once_scrolled_into_view)
        
        #button_spravochniki = driver.find_element(By.ID, 'span')
        #button_spravochniki.click()

        #parent_page1 = driver.find_element((By.NAME, "Справочники"))  


        button_spravochniki = driver.find_element(By.CSS_SELECTOR, "div[tabindex='0']")
        #button_spravochniki.select_by_visible_text('Справочники')
        #selectedOption = Select(driver.find_element(By.CSS_SELECTOR, "div[tabindex='0']"))
        #roleOptions = driver.find_element(By.XPATH, "v-button v-widget cuba-login-submit v-button-cuba-login-submit v-has-width")[0]

        #roleOptions.click()

        
        button_spravochniki = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div[1]/div/div/div[3]/div/span[5]")
        action = ActionChains(driver)
        action.move_to_element(button_spravochniki)
        action.click(button_spravochniki)
        action.perform()


        #driver.execute_script("arguments[0].click();", button_spravochniki)
        

        #print ("button_spravochniki is ready!")
        #print (button_spravochniki)
        #print (button_spravochniki.get_property("text_length"))
        #option = button_spravochniki.get_property('class')

        #for option in button_spravochniki:
            #print("Value is: %s" % option.get_attribute("value"))
            #option.click()



        
    except TimeoutException:
        print ("Loading took too much time!")
    


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

