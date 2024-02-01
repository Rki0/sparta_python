# 모듈 설명
# selenium을 사용하여 웹 크롤링을 진행한다.

# 라이브러리 참고 사항
# 버전 : 4.16.0

# 사용 방법
# 1. 크롤링 하고자하는 사이트의 URL을 입력한다.
# 2. 크롤링 하고자하는 부분의 선택자를 입력한다.
# 3. 크롤링 결과를 확인한다.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 크롤링을 위한 함수
def crawlingWebPage(target_url, twoD_element_list):
    # 브라우저 꺼짐 방지 코드
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])

    # 셀레니움으로 웹 브라우저(크롬) 자동 띄우기
    driver = webdriver.Chrome(options=chrome_options)

    # 첫 번쨰 인자로 입력한 URL에 접근
    driver.get(target_url)

    result = []

    # 2차원 배열 순회 : id, class, selector 순으로 탐색
    # for oneD_elment_list in twoD_element_list:
    for index, oneD_elment_list in enumerate(twoD_element_list):
        # 1차원 배열 순회 : 입력한 정보를 토대로 브라우저 요소 탐색
        for element in oneD_elment_list:
            if(index == 0):
                # id를 사용한 요소 탐색
                result.append(driver.find_element(By.ID, element).text)
            elif(index == 1):
                # class를 사용한 요소 탐색
                result.append(driver.find_element(By.CLASS_NAME, element).text)
            else:
                # selector를 사용한 요소 탐색
                result.append(driver.find_element(By.CSS_SELECTOR, element).text)

    # 웹 브라우저 닫기
    driver.quit()

    return result

# ex 1. 구글 날씨 크롤링
id_element_list = ['wob_tm']
class_element_list = []
selector_element_list = ['span.BBwThe']
element_list = [id_element_list, class_element_list, selector_element_list]
print("이 것은 탐색하고자하는 리스트입니다.")
print(element_list)

# 함수 실행
data = crawlingWebPage("https://www.google.com/search?q=weather", element_list)
print("최종 결과는 다음과 같습니다.")
print(data)

# ex 2. 애플 주가 크롤링
id_element_list = []
class_element_list = []
selector_element_list = [".DoxwDb", ".IsqQVc", 'div[data-attrid="최고"]', 'div[data-attrid="최저"]']
element_list = [id_element_list, class_element_list, selector_element_list]
print("이 것은 탐색하고자하는 리스트입니다.")
print(element_list)

data = crawlingWebPage("https://www.google.com/search?q=애플 주가", element_list)
print("최종 결과는 다음과 같습니다.")
print(data)

# ex 3. 교보문고 상위 20개 책 크롤링
id_element_list = []
class_element_list = ["prod_info", "prod_author", "prod_rank"]
selector_element_list = []
element_list = [id_element_list, class_element_list, selector_element_list]
print("이 것은 탐색하고자하는 리스트입니다.")
print(element_list)

data = crawlingWebPage("https://product.kyobobook.co.kr/bestseller/online#?page=1&per=50&ymw=&period=001&saleCmdtClstCode=&dsplDvsnCode=000&dsplTrgtDvsnCode=001&saleCmdtDsplDvsnCode=", element_list)
print("최종 결과는 다음과 같습니다.")
print(data)