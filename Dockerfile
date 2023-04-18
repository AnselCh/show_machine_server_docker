FROM python:3.10.8

# 複製程式碼到Docker image
COPY . /app
WORKDIR /app

ENV FLASK_APP=server.py

# 安裝所需套件
RUN pip install -r requirements.txt

EXPOSE 5000

# 啟動程式
CMD ["flask", "run" , "--host=0.0.0.0"]
