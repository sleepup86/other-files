import ip
from selenium import webdriver
from selenium.webdriver.support.ui import Select
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

# 구매창 접속
driver.get('https://el.dhlottery.co.kr/game/TotalGame.jsp?LottoId=LO40')

# 자동구매발급
driver.switch_to.frame('ifrm_tab')
driver.find_element('xpath', '//*[@id="num2"]').click()

# 로또 구매 개수 선택
select = Select(driver.find_element('xpath', '//*[@id="amoundApply"]'))
select.select_by_value('5')

# 구매 확인 버튼 클릭
driver.find_element('xpath', '//*[@id="btnSelectNum"]').click()

# 구매하기
driver.find_element('xpath', '//*[@id="btnBuy"]').click()

# 확인 버튼
driver.find_element(
    'xpath', '//*[@id="popupLayerConfirm"]/div/div[2]/input[1]').click()

# 크롬브라우저 종료
# driver.close()

# 마이페이지
driver.get('https://www.dhlottery.co.kr/userSsl.do?method=myPage')
