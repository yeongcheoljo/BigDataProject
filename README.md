# BigDataProject(학교주변 버스 이용 현황 통계)

1. 프로젝트 주제 선정
   - 학교주변을 지나가는 버스노선별 이용현황을 조사하여 어떤 버스가 어느시간때에 이용량이 많고, 어떤 사람들이 자주 이용하는지, 어떤 정류장이 이용량이 많은지 자료를 통해 정리하여 학교주변을 지나는 버스노선들의 정보를 알아보기 위해 주제를 선정하였습니다.

2. 데이터 수집
   - 데이터 수집은 교통카드빅데이터 통합정보시스템(https://stcis.go.kr/wps/main.do)사이트에서 노선별 이용량 데이터를 통해 23년도 데이터를 월별로 수집하였습니다.
  
3. 데이터 분석 계획
   - 데이터 분석은 노선별 이용량 데이터를 전처리를 거친 후 노선, 이용자유형, 월별로 그룹화하여 이용량 데이터 중 '합계'열과 '05' ~ '23'까지의 시간대 열의 데이터의 최고값을 각각 추출하여 데이터를 변환한 뒤 해당 데이터들을 결합하여 하나의 데이터로 만들어 이용량이 많은 정류장의 데이터를 만든다.
   - 만들어낸 데이터를 통해 전체 데이터중 이용량이 많은 정류장의 수를 count하여 상위10개 정류장의 데이터를 시각화한다.
   - 이용자유형, 월별로 이용량이 많은 정류장 데이터를 이용하여 전체 데이터와 같이 이용량이 많은 정류장의 수를 count한 뒤 상위10개 정류장의 데이터를 시각화한다.
   - 노선별 데이터는 각 노선별로 지나가는 정류장이 지정되어 있기때문에 이용량이 많은 정류장의 수를 count하여 데이터를 시각화한다.
   - 시간대별로 추출한 데이터를 활용하여 각 시간대별로 어떤 정류장의 이용량이 가장 많은지 count한뒤 시각화한다.

### [데이터 결합 및 전처리](https://github.com/yeongcheoljo/BigDataProject/blob/main/%EB%85%B8%EC%84%A0%EB%B3%84_%EB%8D%B0%EC%9D%B4%ED%84%B0_%EA%B2%B0%ED%95%A9%EB%B0%8F_%EC%A0%84%EC%B2%98%EB%A6%AC.ipynb)

### [데이터 시각화1](https://github.com/yeongcheoljo/BigDataProject/blob/main/%EC%9D%B4%EC%9A%A9%EB%9F%89_%EC%8B%9C%EA%B0%81%ED%99%94.ipynb)

### [데이터 시각화2](https://github.com/yeongcheoljo/BigDataProject/blob/main/%EC%8B%9C%EA%B0%84%EB%8C%80%EB%B3%84_%EC%9D%B4%EC%9A%A9%EB%9F%89_%EC%8B%9C%EA%B0%81%ED%99%94.ipynb)

### [프로젝트 보고서](https://github.com/yeongcheoljo/BigDataProject/blob/main/%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%B2%98%EB%A6%AC%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20%EB%B3%B4%EA%B3%A0%EC%84%9C%20202044089%20%EC%A1%B0%EC%98%81%EC%B2%A0.pdf)
