#dockerfile dosyası bir image oluşturma dosyasıdır.
#BASEIMAGE belli bir zemin var üstüne inşaa et diyoruz. Americayı terar keşfetmeye gerek yok.İlk satır bunu ifade ediyor.
#1. satır yani from ana image dır.
#RUN komutu ise içinde linüx komutları çalıştırmak için kullanılır.Burda mkdir app adında klasör oluşturma komutu anaimajı kapsar.
#ana klasörden oluşturduğum app dizinine gitmek için WORKDIR komutunu kullanıyorum.
#COPY nin sonundaki . image içini ifade eder.nokta bulunulan dizini temsil eder.#soldaki pc yi sağdaki docker ı temsil eder
#ardından run komutu ile pip i güncelleyip sonra paketleri indiriyorum.
#ardından dockera main ve model doyasını göndermek için copy fonk. yazıyorum
#CMD komutu en son çalışır.
#build alıyoruz ardından
FROM python:3.9.18-slim-bullseye
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN pip install update pip && pip install -r requirements.txt
COPY main.py  diabetes_knn_model.pkl /app/
CMD [ "uvicorn","main:app","--host=0.0.0.0","--port=8000" ]

#docker build -t knn_api_image:v1 .                ----> docker ı inşaa ediyoruz.
#docker run -p 8000:8000 --name knn_api_container knn_api_image:v1                 -----> -p lokalimde de görmek için kullandım. 8000 portuna bak diyorum çünkü image ı oluştururken 8000 portu dedim. name in ilk sağındaki oluşacak container ın adını veriyorum, onun sağındaki de  çalıştıracağım image adıdır.
# docker ps        ------> çalıştığım container içine giriyorum

# docker exec -it knn_api_container bash        ---------> comutu ile root@13837b135c8b:/app# böyle bir çıktı alıyorum. çünkü mkdir /app diyerek app i verdim. ardından ls dediğimde de dosyaları  görüyorum