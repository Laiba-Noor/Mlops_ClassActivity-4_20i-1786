install:
	pip install -r requirements.txt

run:
	python app.py

docker-build:
	docker build -t iris_model_app .

docker-run:
	docker run -p 5009:5009 iris_model_app
