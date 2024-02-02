# OCR Table Recognition - ДПО УРФУ

Распознавание таблиц с координатами в документах с помощью библиотеки Doctr 
## Структура проекта
```
app/
    main.py #скрпипт запуска
    cer.py
    nms.py
model/
    model.onnx #веса модели
test/
    test.py
example/ #входные pdf документы
    1.pdf    
results/
    1.csv
```
## Использование
1. Положить pdf документы в папку example
2. Установить зависимости 
```
    pip install -r requirements.txt
```
3. Скачать веса модели(https://drive.google.com/file/d/1OFGl3h1wSAK976HvsloZyA21A2ZRRxf5/view) в app/model 
4. Запустить скрипт
```
    python app/main.py
```
5. Результаты обработки в папке "results"

## Авторы
- Решетников Кирилл Игоревич 
- Поляков Станислав Олегович 