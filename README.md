


# Moon Trakcer

개인적인 Home Side Project , 카메라 / Mobility 장비 / Computer 로 물체(달,moon)을 추적하며 촬영하는 기계를 만들고자함 

* 카메라 장비 : Smart Phone (Galaxy Note 10)
* Mobility 장비 : Arduino / Lego EV3
* Computer 장비 : Raspberry Pi



## 계획 조감도 

<img width="50%" height="50%" src="https://user-images.githubusercontent.com/23700286/155877486-7156031f-f663-4443-8772-0c189dd28be4.png"/>

## 계획 

단계별 계획 

1. 간단한 물체 (파란 병뚜껑)을 추적하는 기능까지 완성 (추적 및 동심원의 위치를 기록)
2. Drop Box로 1분당 추적 이미지와 동심원 위치를 전송하는 기능 완성
3. 추적 물체를 보름달로 바꾸고 달의 중심 위치를 추적 
4. 쌓인 보름달 이미지를 전처리를 통해 가려진 달이미지를 생성 (반달,초승달등을 생성)
5. 생성된 이미지로 ML로 달 추적 




## 2022 1월


### 1-1 단계 : Camera의 이미지를 Computer에 연결 

* Smart Phone Camera를 이용 IP WebCam app를 중계하여 Computer에서 Video Image 수신 환경 설정 (IP주소)
  --> Opencv와 IP WebCam APP 이용 
* Opencv에서 물체 (HSV로 특징을 mask) 특정 , 특정된 물체의 ROI 설정 및 중심위치 확인 , 현재는 HSV기준으로 물체 추적 (-> 추후에 ML)



### 1-2 단계 : Computer에서 물체 추적 위치 파악 , Lege EV3에 명령 송신

<img width="50%" height="50%" src="https://user-images.githubusercontent.com/23700286/155877178-c437f57e-0741-4931-83ef-c99b18bc0b24.gif"/>


<img width="50%" height="50%" src="https://user-images.githubusercontent.com/23700286/156370209-76f91226-2429-412a-873e-334f7d359c83.gif"/>




### 1-3 단계 : Lego 완성 (일단 , 좌우움직임만 가능)


일단 좌우 움직임으로 물체 추적을 통신으로 움직이게 만들었음 이후 상하로 움직이는 Lego 모빌리티도 추가 예정 


<img width="50%" height="50%" src="https://user-images.githubusercontent.com/23700286/156370126-052ec0a7-a607-4a32-8faa-85f72c7ba4c5.jpg"/>







### 1-4 단계 : DropBox로 Image 전송


더 정확한 추적을 하기위해 추적된 물체의 이미지를 모아서 10초마다 이미지를 Drop Box로 저장 


<img width="50%" height="50%" src="https://user-images.githubusercontent.com/23700286/156368637-f4238e7a-d293-445b-be45-0e81e42e6133.PNG"/>



## 2022년 5월

1. Code 수정 : 각단계 Class 화 
2. Lego 완성 : 상하좌우 움직임 

### 결과 

<img width="50%" height="50%" src="https://user-images.githubusercontent.com/23700286/168474425-89c763fe-0736-401a-ae2d-c4dfd3632dae.gif"/>


<img width="50%" height="50%" src="https://user-images.githubusercontent.com/23700286/168474750-73f29091-af79-4191-85ee-418f2c382e18.gif"/>


<img width="50%" height="50%" src="https://user-images.githubusercontent.com/23700286/168476389-44a21a69-83e8-43ec-bfa8-a2f209c46747.gif"/>










