﻿define e = Character('Женщина', color="#114e11")
define g = Character('Трамвайный мужчина', color="#31478f")
define p1 = Character('Пацанчик 1')
define p2 = Character('Пацанчик 2')
define p3 = Character('Пацанчик 3')
define n = Character(None, kind = nvl)
define s = Character('Сосед сверху', color="#dd825e")
define p = Character('Сотрудница банка')
define E = Character('Олег Егорьевич', color="#205d86")
define B = Character('Дядя Боря', color="#303b7c")
define K = Character('Кирилловна', color="#dac23a")


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
    scene black with fade
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
    scene black with fade
    "Какая-то деревня. Пятью годами ранее..."
    scene village with fade
    "Дачный сезон в самом разгаре."
    "Олег Егорович и его жена Василиса Кирилловна работают."
    "Пилит доски, {w}борется с сорниками. {w}Трудные задачи!"
    "Василиса пошла отдохнуть."
    "Идёт дядя Боря, пьяница и бездельник, на что живёт?"
    "Только Бог знает."
    B "Привет, Егорыч!"
    E "Привет, Борька!"
    B "Ой, а не найдется ли пятачок в долг?"
    E "Окоянный попрошайка! Ты мне уже полтинник должен!"
    B "А как же пять выполотых грядок!"
    E "Давай пятьдесят!"
    B "Завтра!"
    E "У тебя каждый день завтра завтра! Наглец!"
    B "А ты знаешь, что сегодня за праздник?"
    E "Нет"
    B "Сегодня день Ивана Купалы! Поставишь по 50 грамм?"
    "Кирилловна вышла и, увидев Борю , закричала:"
    K "Ты то что пришел? А ну марш отсюда!"
    B "Ты что, Василисушка, так гостей не гоже принимать, лучше налей нам по 100 грамм!"
    K "Да ты не одурел черт..."
    B "Заткнись баба!"
    scene black with fade
    "Спустя какое-то время..."
    scene vilage_home with fade
    B "Ой спасибо, Егорыч, уважил друга! Давай, до завтрени."
    E "До скорого."
    scene black with fade
    "Вернемся обратно..."
    scene home with fade
    "Олег Егорыч это мой сосед снизу."
    "Он председатель ТСЖ, и кстати очень трудолюбивый!"
    "Он в школе ведёт географию, в которой души не чает."
    "А дети, бестолочи и остолопы, как он выражается, не любят географию, считая ее ненужной!"
    "Как такое может быть! {w}Жуть!"
    "Вот Олег Егорович дома, есть пара дел: {w}в 308 трубу прорвало, {w}в 206 взорвалась плита, {w}а в 204 поселились какие-то наркошки."
    "Все лежит на плечах председателя, говорит Олег."
    "Так вот, сидел он однажды дома и читал Верховского."
    "Вдруг прилетела мысль, такая как всегда прилетает людям, способным думать."
    "Мысль о высоком, тот час погасла и пришло сообщение, что на лестничном пролете много бычков."
    "Олег бежит."
    "Стук в дверь. А я почти голая, быстро одеваюсь, и лечу."
    "Открываю! А там Егорыч:"
    show e  at left with dissolve
    show E  at right with dissolve
    E "Дамочка, добрый день! Курите на лесенках?"
    "Вообще-то я не курю, но хватает вредных привычек и увлечений."
    e "Я не курю."
    E "Я что-ли? На вашем этаже 134 бычка, выражаясь алгебраически, очень много, выражаясь быдлинским, {w}вам он ближе?!"
    e "Не хамите, Олег Егорович. Может соседи сверху курят?"
    E "Я вот не буду разбираться..."
    "Бум, что-то грохнулось сверху и опять пошли крики!"
    E "Я пошел разбираться, дамочка! До встречи!"
    e "До свидания!"
    "Так-то не плохой чувачок этот Егорыч."
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
    # jump battle
    return
