from selenium import webdriver as w
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import time as t


sv = Service(ChromeDriverManager().install())

try: 
    driver = w.Chrome(service=sv)
    driver.get('')
    t.sleep(1)
    driver.find_element(by='xpath', value='//*[@id="username"]').send_keys('')
    t.sleep(1)
    driver.find_element(by='xpath', value='//*[@id="password"]').send_keys('')
    t.sleep(1)
    driver.find_element(by='xpath', value='//*[@id="kt_login_signin_form"]/div[3]/div/label/span').click()
    t.sleep(1)
    driver.find_element(by='xpath', value='//*[@id="kt_login_signin_form"]/button').click()
    t.sleep(1)
    driver.find_element(by='xpath', value='//*[@id="kt_body"]/div[5]/div/div[4]/div/button').click()
    t.sleep(1)
    driver.find_element(by='xpath', value='//*[@id="kt_content"]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/a/div').click()
    t.sleep(1)
    driver.find_element(by='xpath', value='//*[@id="potencia_final"]').send_keys('112,5')
    t.sleep(1)
    driver.find_element(by='xpath', value='//*[@id="formPesquisa"]/div/div[2]/div[2]/div/label[2]/span').click()
    t.sleep(1)
    driver.find_element(by='xpath', value='//*[@id="formPesquisa"]/div/div[2]/div[4]/div/label[1]').click()
    t.sleep(1)
    driver.find_element(by='xpath', value='//*[@id="formPesquisa"]/div/div[2]/div[4]/div/label[3]').click()
    t.sleep(1)
    driver.find_element(by='xpath', value='//*[@id="formPesquisa"]/div/div[2]/div[5]/div/label[1]').click()
    t.sleep(1)
    driver.find_element(by='xpath', value='//*[@id="formPesquisa"]/div/div[2]/div[6]/div/label[2]').click()
    t.sleep(1)
    driver.find_element(by='xpath', value='//*[@id="formPesquisa"]/div/div[3]/div/button').click()
    t.sleep(10)

    


    # elemento.send_keys('tecnosh')
    # driver.quit()
except Exception as e:
    print(f'houve uma exceção: {str(e)}')

# finally:
    # t.sleep(5)
    # driver.quit()