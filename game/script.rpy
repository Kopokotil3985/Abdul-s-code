﻿define e = Character('Егор Грегорьевич', color="#114e11")
define g = Character('Герман', color="#31478f")
define n = Character(None, kind = nvl)

label start:

    scene park
    show german at left with dissolve
    show egor at right with dissolve

    e "Стоять! Куда по газону?!"
    g "Могу себе позволить!"
    e "Я тебе лицо набью!"
    g "Только попробуй"
    "Бой начинается!"
    n "Обучение боевой системе!"
    n "Основные обозначения: ОЗ - очки здоровья, ОУ - очки урона."
    n "Боевая система основана на системе бросания кубиков d4, d6, d10, d20. У этих кубиков 4, 6, 10 и 20 граней соответственно."
    n "Когда пришло время хода нужно будет выбрать между легкой и тяжелой атакой."
    n "Во время легкой атаки кидается кубик d10. Если выпадет значение от 2-ух до 8-ми, то получится обычная атака, размер которой равен значению кубика d4."
    n "Если выпадет значение больше 8-ми, то получится критическая атака, равная сумме результатов на кубиках d4 и d6."
    n "Если выпадет значение меньше 2-ух, то никакой атаки не получится."
    n "При выборе тяжелой атаки кидается кубик d10."
    n "Если выпадет значение больше 9-ти, то сработает супер атака."
    n "Супер атака высчитывается из удвоенной суммы результатов на кубиках d4 и d6."
    n "При выпадении значений от 5-ти до 8-ми будет обычная тяжелая атака, равная значению кубика d6 плюс еще 2 ОУ."
    n "Если выпало значение d10 менее 5-ти, то никакой атаки не будет."
    n "На этом все, прочитать обучение потом будет уже нельзя!"
    jump battle
    return
