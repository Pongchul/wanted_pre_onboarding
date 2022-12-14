# wanted_pre_onboarding

## ✅ 과제: 채용 공고 CRUD API 구현
| 구현 내용 | 구현 여부 |
| --- | --- |
| 채용 공고 등록 | ✅ |
| 채용 공고 수정 | ✅ |
| 채용 공고 삭제 | ✅ |
| 채용 공고 리스트 조회 | ✅ |
| 채용 공고 상세 내용 조회 | ✅ |
| (Optional) 채용 공고 검색 | ✅ |
| (Optional) 채용 공고 상세 내용 조회시 해당 기업의 다른 공고 목록도 포함 | ✅ |
| (Optional) 채용 공고 지원 |✅ |


### 1. 채용 공고 등록 
- 요청 URL : `POST: {HOST}/api/post/`
- 채용 포지션, 채용 보상금, 사용 기술, 채용 내용, 채용할 기업의 id 를 입력 받아 채용 공고 데이터 생성
### 2. 채용 공고 수정
- 요청 URL : `PUT: {HOST}/api/post/<int:pk>`
- 채용 공고를 수정 
### 3. 채용 공고 삭제
- 요청 URL : `DELETE: {HOST}/api/post/<int:pk>`
- 기존에 등록했던 공고를 삭제
### 4. 채용 공고 리스트 조회
- 요청 URL : `GET: {HOST}/api/post/`
### 5. 채용 공고 상세 내용 조회
- 요청 URL : `GET: {HOST}/api/post/<int:pk>`
### 6. 채용 공고 검색
- 요청 URL : `GET: {HOST}/api/post/<int:pk>`
### 7. 채용 공고 상세 내용 조회시 해당 기업의 다른 공고 목록
- 요청 URL : `GET: {HOST}/api/company/<int:pk>`
### 8. 채용 공고 지원
- 요청 URL : `GET: {HOST}/api/apply/`


## 🛠 사용 기술
- API<br>
![python badge](https://img.shields.io/badge/Python-3.10-%233776AB?style=plastic&logo=python&logoColor=white)
![django badge](https://img.shields.io/badge/Django-4.1.2-%23092E20?style=plastic&logo=Django&logoColor=white)
