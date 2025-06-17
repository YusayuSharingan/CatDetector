## CatDetector
Система распознавания тигров и леопардов на снимках фотоловушек

CatDetector предсказывает *bounding box*'ы животного на снимке и определяет принадлежность к одному из двух классов:
- Тигры
- Леопарды

В файле **basesline.ipynb** предоставлен процесс обучения модели детекции SSD для распознавания классов

Полученные [веса](https://drive.google.com/file/d/1sKBSmMBSg3RvJgTRfRPS2D3y6zHtzi4Z/view?usp=sharing) модели как и [исходный датасет](https://drive.google.com/file/d/1TvEXxb6kqDBkrb1_7kdExPkHGTfxvxFX/view?usp=drive_link) можно загрузить с гугл диска.

Файл **CatDetecor.py** хранит код работы детектора

### Для запуска из консоли:

1. Клонируйте репозиторий
```bash
git clone https://github.com/YusayuSharingan/CatDetector.git
```

2. Установите зависимости
```bash
cd CatDetector
pip install -r requirements.txt
```

3. Запустите
```
python CatDetector.py
```

4. Введите путь к изображению

5. Результат будет лежать в папке **output**
