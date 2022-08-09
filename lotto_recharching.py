import ip
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import sys
sys.path.append("")


DRIVER_PATH = 'C:/Users/syhyu/Desktop/workspace/python/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

# 동행복권 로그인 창 접속
LOTTO_URL = 'https://dhlottery.co.kr/user.do?method=login&returnUrl='
driver.get(LOTTO_URL)

# 동행복권 아이디 입력
elem_login = driver.find_element('id', 'userId')
elem_login.send_keys(ip.ID)

# 동행복권 비밀번호 입력
elem_login = driver.find_element('name', 'password')
elem_login.clear()
elem_login.send_keys(ip.PW)

# 로그인 버튼 클릭
LOGIN_XPATH = '//*[@id="article"]/div[2]/div/form/div/div[1]/fieldset/div[1]/a'
driver.find_element('xpath', LOGIN_XPATH).click()

# 예치금 충전 페이지 접속
driver.get('https://dhlottery.co.kr/payment.do?method=payment')

# 충전금액 선택 50,000원
select = Select(driver.find_element('xpath', '//*[@id="Amt"]'))
select.select_by_value('50000')

# 확인 클릭
driver.find_element('xpath', '//*[@id="btn2"]/button').click()


print(driver.window_handles)

# 로딩 기다리기
time.sleep(1)

print(driver.window_handles)

# 최근 열린 탭으로 전환
driver.switch_to.window(driver.window_handles[-1])

# 약관동의 전체 선택
driver.find_element('xpath', '//*[@id="content"]/div[2]/div[1]/div[2]/div/div/span/label').click()

# 전화번호 입력
driver.find_element('xpath', '//*[@id="cphoneNo"]').send_keys('87092257')

# 인증번호 보내기 버튼 클릭
driver.find_element('xpath', '//*[@id="sendAuthNoBtn"]').click()
