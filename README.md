# sokoban_python
Игра "Sokoban" на python.
- Что делать?
  - Нужно расставить все ящики на карте в определнные места
- Как запустить?
- ```
  git clone https://github.com/evgeniyARCH/sokoban_python.git
- ```
  python3 /home/$USER/sokoban_python/new_polig.py
- Как создать свою карту?
  - Создаем файл в папке с программой с расширением .py
  - Добавляем туда следующий код:
  - ```
    from paint_mass_gen import * #генератор массива(основы карты)
    from paint_addons import * #дополнения(всякие фигуры)
    from new_funk import * #собственно говоря сама игра
    mass = [] #создание массива
    mass = mass_gen_custom(a,b,symbol) #генерация массива с шириной <a>, высотой <b>, символом заполнения <symbol>
    paint_rectangle_nofill(a, b, smb, x, y, mass) #контур прямоугольника(как основной барьер) со сторонами <x> и <y>, символом заполнения <smb>, координатами расположения(верхний левый угол прямоугольника) <x> и <y> и массивом для редактирования <mass>
    xy = sokoban_game(x,y,character_game,mass,bonus,walk,bonuscords,wins) #сама игра: <x> и <y> - координаты расположения игрока; <character_game> - символ игрока; <mass> - массив; bonus - символ ящика; <walk> - символ барьера; <bonuscords> - массив с заданными координатами расположиния ящиков(типа [x1,y1,x2,y2,...]); <wins> - массив с заданными координатами расположения точек, куда необходимо принести ящики(типа [x1,y1,x2,y2,...])
