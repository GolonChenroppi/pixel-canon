<div align="center">
  <a href="./README.md">English</a> | <strong>Русский</strong>
</div>
<hr>

# Pixel-Canon

> Канон для топологии пиксельных данных. Кросс-языковая спецификация для определения логической структуры изображений (порядка осей, ориентации и порядка в памяти).

`Pixel-Canon` — это кросс-языковой проект, нацеленный на решение распространенной проблемы в компьютерном зрении и машинном обучении: неоднозначности форматов данных изображений. Что означают оси N-мерного массива? Это `(Высота, Ширина, Каналы)` или `(Каналы, Высота, Ширина)`? Направлена ли ось Y вверх или вниз?

Этот проект предоставляет простую, декларативную спецификацию и набор инструментов для явного описания этой информации, делая конвейеры обработки данных более надежными.

## Спецификация

С формальной спецификацией, которой должны придерживаться все реализации, можно ознакомиться здесь:
*   **[Спецификация v1.0](./spec/v1.0.ru.md)**

## Реализации

### **[Python](./python/)** (`pixel-canon` на PyPI)

Реализация на Python доступна и включает бэкенд для `numpy`.

**Установка:**
```bash
# Ядро библиотеки
pip install pixel-canon

# С поддержкой NumPy
pip install "pixel-canon[numpy]"
```

**Пример использования:**
```python
import numpy as np
from pixel_canon import CommonLayouts
from pixel_canon.backends.numpy_backend import convert_numpy

# Изображение из OpenCV (HWC, BGR)
# ЗАМЕЧАНИЕ: OpenCV использует BGR, но в примере мы используем RGB лэйаут.
image_hwc = np.zeros((480, 640, 3), dtype=np.uint8)
layout_hwc = CommonLayouts.HWC_ROW_MAJOR_RGB

# Целевой формат для модели PyTorch (CHW, RGB)
layout_chw = CommonLayouts.CHW_ROW_MAJOR_RGB

# Безопасное и явное преобразование формата
image_chw = convert_numpy(image_hwc, src=layout_hwc, dst=layout_chw)

print(f"Исходная форма: {image_hwc.shape}")
print(f"Преобразованная форма: {image_chw.shape}")
# Исходная форма: (480, 640, 3)
# Преобразованная форма: (3, 480, 640)
```

### *Другие языки*
Реализации для Rust, TypeScript, Java и других языков планируются. Ваш вклад приветствуется!

## Лицензия

Этот проект лицензирован под лицензией MIT. Подробности смотрите в файле [LICENSE].
