import ip
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.service import Service     # 다운로드 받아서 설치할 때 #
# from webdriver_manager.chrome import ChromeDriverManager  # 다운로드 받아서 설치할 때 #
import sys
import time

sys.path.append("")

# 브라우저 꺼짐 방지 옵션
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# DRIVER_PATH = 'C:/Users/사용자/Desktop/workspace/python/chromedriver.exe'
driver = webdriver.Chrome(options=chrome_options)

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 동행복권 로그인 창 접속
LOTTO_URL = "https://dhlottery.co.kr/user.do?method=login&returnUrl="
driver.get(LOTTO_URL)

# 동행복권 아이디 입력
elem_login = driver.find_element("id", "userId")
elem_login.send_keys(ip.ID)

# 동행복권 비밀번호 입력
elem_login = driver.find_element("name", "password")
elem_login.clear()
elem_login.send_keys(ip.PW)

# 로그인 버튼 클릭
LOGIN_XPATH = '//*[@id="article"]/div[2]/div/form/div/div[1]/fieldset/div[1]/a'
driver.find_element("xpath", LOGIN_XPATH).click()


"""
로또 구매
"""

# 구매창 접속(로또)
driver.get("https://el.dhlottery.co.kr/game/TotalGame.jsp?LottoId=LO40")

# 자동구매발급(로또)
driver.switch_to.frame("ifrm_tab")
driver.find_element("xpath", '//*[@id="num2"]').click()

# 로또 구매 개수 선택(로또)
select = Select(driver.find_element("xpath", '//*[@id="amoundApply"]'))
select.select_by_value("5")

# 개수 확인 버튼 클릭(로또)
driver.find_element("xpath", '//*[@id="btnSelectNum"]').click()

# 구매하기(로또)
driver.find_element("xpath", '//*[@id="btnBuy"]').click()

# 확인 버튼(로또)
driver.find_element("xpath", '//*[@id="popupLayerConfirm"]/div/div[2]/input[1]').click()


""" 
연금복권720 구매
"""

# 구매창 접속(연금복권720)
driver.get("https://el.dhlottery.co.kr/game/TotalGame.jsp?LottoId=LP72")

# 자동구매발급(연금복권720)
driver.switch_to.frame("ifrm_tab")

# 자동번호(연금복권720)
driver.find_element("xpath", '//*[@class="lotto720_btn_auto_number"]').click()

# 선택완료(연금복권720)
driver.find_element("xpath", '//*[@class="lotto720_btn_confirm_number"]').click()

# 빨간 구매하기 버튼 클릭(연금복권720)
driver.find_element("xpath", '//*[@class="lotto720_btn_pay"]').click()

# 파란 구매하기 버튼(연금복권720)
driver.find_element(
    "xpath", '//*[@id="lotto720_popup_confirm"]/div/div[3]/a[1]/span'
).click()

# 구매완료 후 닫기 버튼 클릭(연금복권720)
driver.find_element("xpath", '//*[@id="lotto720_popup_pay"]/div/div[3]/a[1]/span').click()


# 크롬브라우저 종료
# driver.close()

# 로딩 기다리기
# time.sleep(5)

# 마이페이지
driver.get("https://dhlottery.co.kr/userSsl.do?method=myPage")
