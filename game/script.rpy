﻿define e = Character('Женщина', color="#114e11")
define g = Character('Трамвайный мужчина', color="#31478f")
define p1 = Character('Пацанчик 1')
define p2 = Character('Пацанчик 2')
define p3 = Character('Пацанчик 3')
define n = Character(None, kind = nvl)
define s = Character('Сосед сверху', color="#dd825e")
define p = Character('Сотрудница банка')


label start:
    scene tramvai with fade
    g "Вышел, вышел, стоят тут всякие!"
    show man1 with dissolve
    "Нервный мужчина, рассталкивая подростков, стоящих в дверях, пытался выйти из битком набитого трамвая."
    hide man1 with dissolve
    show man1 at left with dissolve
    show child at right with dissolve
    "На его пути возник пацанчик, и мужик резким движением руки отодвинул его. Тот чуть не упал."
    p1 "Не трогай Паху, чертов маразматик!"
    p2 "Психопад поганый!"
    p3 "Сукин сын!"
    "Слышались возмущенные возгласы подростков, защищали своих!"
    "Мужчина удалялся."
    "А я стояла, не хотела заходить в этот адок."
    scene black
    "А я черемуха, закончившая истфак."
    "Живу в съемной квартире, в не старом, но и не новом доме."
    "В основном пишу эротические романы: он полюбил его, а она другого."
    "Он сбросился при виде их свадьбы; {w}он любит ее, она любит его, {w}но есть ещё один, любящий ее, развязки разнообразны; {w}н не любит ее, но родители навязывают ему ее, все плохо у них."
    "Но это не литература, мысли там ноль."
    "Моя мечта- написать книгу настоящую, про смысл жизни."
    "Но такое не пользуется популярностью."
    scene home with fade
    "Раздались крики сверху."
    "Что-то упало на пол!"
    "Ещё, как будто пошел дождь из предметов."
    "Кричали наверху или это был один человек, я не знаю."
    "Кричали что по типу: "
    s "Почему я должен подчинятся!"
    s "Я свободный человек!"
    s "Они меня задушили!"
    s "Не Обязан!"
    s "НЕ ОБЯЗАН!"
    s "ЗАКОЛЕБАЛИ, ****ИНЫ!!!"
    "Видимо там живёт какой-то ненормальный или какие-то."
    "Но голос мужской."
    "И пока что других не слышно."
    "Да, пока что не пойду разбираться."
    "Кстати,"
    "Я увидела трамвайного мужчину вчера в банке."
    "Я приходила разбираться, почему у меня с карты сняли пятьсот рублей непонятно за что!"
    "Так вот, сидела в отделение, а мужчина что-то рьяно доказывал женщине в окошке."
    g "Вы кто такая, чтобы мне здесь указывать?!"
    p "Я сотрудник банка и скорее всего понимаю банковскую систему лучше вас."
    g "Ты ничего не понимаешь, ш***а!"
    p "Не надо мне грубить! Я сейчас вызову охрану."
    g "Вызывай, людей грабят посреди бела дня! А ей пофиг!"
    "Дальше меня вызвали, и я не дослушала."
    #"Бой начинается!"
    # n "Обучение боевой системе!"
    # n "Основные обозначения: ОЗ - очки здоровья, ОУ - очки урона."
    # n "Боевая система основана на системе бросания кубиков d4, d6, d10, d20. У этих кубиков 4, 6, 10 и 20 граней соответственно."
    # n "Когда пришло время хода нужно будет выбрать между легкой и тяжелой атакой."
    # n "Во время легкой атаки кидается кубик d10. Если выпадет значение от 2-ух до 8-ми, то получится обычная атака, размер которой равен значению кубика d4."
    # n "Если выпадет значение больше 8-ми, то получится критическая атака, равная сумме результатов на кубиках d4 и d6."
    # n "Если выпадет значение меньше 2-ух, то никакой атаки не получится."
    # n "При выборе тяжелой атаки кидается кубик d10."
    # n "Если выпадет значение больше 9-ти, то сработает супер атака."
    # n "Супер атака высчитывается из удвоенной суммы результатов на кубиках d4 и d6."
    # n "При выпадении значений от 5-ти до 8-ми будет обычная тяжелая атака, равная значению кубика d6 плюс еще 2 ОУ."
    # n "Если выпало значение d10 менее 5-ти, то никакой атаки не будет."
    # n "На этом все, прочитать обучение потом будет уже нельзя!"
    # jump battle
    return
