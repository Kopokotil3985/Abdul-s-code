﻿define e = Character('Анастасия', color="#b33535")
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
define i = Character('Ильинична', color = "#146311")
define sosed = Character('Сосед')
define v = Character('Василиса', color = "#b93f91")

define end = 0

init:
    $ left2 = Position(xalign=0.2, yalign=1.1)

label start:
    window hide
    scene prolog with fade
    pause
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
    "А мне 25, закончившая истфак."
    "Живу в съемной квартире, в не старом, но и не новом многоквартирном доме."
    "А на что я живу? {w}В основном пишу эротические романы: он полюбил его, а она другого."
    "Он сбросился при виде их свадьбы; {w}он любит ее, она любит его, {w}но есть ещё один, любящий ее, развязки разнообразны; {w}н не любит ее, но родители навязывают ему ее, все плохо у них."
    "Но это не литература, мысли там ноль."
    "Все ради заработка!"
    "Моя мечта - написать книгу настоящую, про смысл жизни."
    "Но такое не пользуется популярностью."
    "Давайте проще жить!"
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
    "Так вот, сидела в отделении, а краснолицый от перевозбуждения мужчина что-то рьяно доказывал женщине в окошке."
    "Он был в мятом костюме, довольно грязном.{w} Не чувствовалась женственная рука."
    "Его лицо изменялось до неузнаваемости, то перекошенное, то отмеченное."
    "До меня долетели обрывки беседы, да это и беседой трудно назвать:"
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
    show egorich at left with dissolve
    show borka at right with dissolve
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
    show kirilovna at left2 with dissolve
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
    "Темные времена начинались в селе."
    "Уже и бельё сняла Василиса Кирилловна. {w}Уже и чай все пьют, сидя молча, смотря на потухающее солнце. {w}На вспаханную землю."
    "Вкусно пахнет в воздухе. Птицы поют."
    "Темнее стало. Уже только с фонарем выйдешь."
    "Все уснуло в деревне."
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
    "Мысль о высоком, в чем смысл его деятельности. Он ищет и старается, отдается ученикам по полной."
    "Никому он не интересен. Нужен орущий учитель-Цербер! Как все сгнило! Все хотят простого!"
    "Мысль о высоком, тот час погасла и пришло сообщение, что на лестничном пролете много бычков."
    "Олег бежит."
    s "Пошли к черту! Я заколебался! Хочу проще!"
    s "Что разобрались там наверху?!"
    "Меня начало это бесить"
    s "Пошла н***й, мелкая ш*****а! Дай отдохнуть хоть дома!"
    s "Для вас ор - это отдых!? Наши взгляды на мир расходятся!"
    s "А мне пофиг!"
    "Бутылка разбилась об пол. Что-то прилетело в стену."
    "Странный"
    "Стук в дверь. А я почти голая, быстро одеваюсь, и лечу."
    "Открываю! А там Егорыч:"
    show anastsia at left with dissolve
    show egorich at right with dissolve
    E "Дамочка, добрый день! {w}Что смотрите?"
    e "На вас."
    E "Я спросил не про одушевлённое существо, на которое обращён ваш взгляд, а про смысл вашего глядения."
    "Зря рот открыла, щас будет лекция."
    E "Я принимаю мысль, что моя внешность достаточно привлекательна,{w} но поставив в виду амплитуду наших возрастов, я с уверенностью…"
    e "Да, да, да, Олег Егорович, зачем вы ко мне пришли?"
    E "Моя дорогуша, а не вы ли курите на лесенках? {w}Выхожу я значит в 6.52 выбросить мусор и,"
    E "Решив пройти по ступенькам этажа так 3, размять, как говорится свои старые ноги,{w} бычок,{w} потом ещё один, 3 и если выражаться точным алгебраическим языком их было 21 штука."
    E "Вы курите?"
    e "Не, я не курю. Своих вредных привычек достаточно."
    E "Я вот не буду разбираться..."
    "Бум, что-то грохнулось сверху и опять пошли крики!"
    "Как говорил Егорыч, сила была равна 1420H, а шум произошел на 76 Дц, если верить точному уху сего джентльмена"
    "Шум меня уже очень сильно бесил."
    "Прям как молодого коня, которого сдерживают уздой."
    E "Даммммммм. Я пошел разбираться, дамочка! Не кури́те!"
    e "Не курю я! До свидания!"
    "Прокричала я в след Егорычу."
    "Так-то не плохой чувачок этот Егорыч, но сплетник и ответственный человек сразу."
    "Вот такое чудо."
    scene black with fade
    "Спустя какое-то вермя."
    scene home with fade
    "Опять стучат в дверь. {w}Ужас!"
    "Я что-ли объект культурного наследия, чтобы ко мне приходить всегда?"
    "Иду опять смотреть, кто пришел и оторвал меня от писания новой книжки."
    "На пороге стоит Ильинична:"
    show ilinichna at right with dissolve
    show anastsia at left with dissolve
    i "Давайте, Анастасия Игоревна, помогите пожалуйста, {w}квартиру Олега Егоровича ограбили!"
    e "Ужас какой, посреди бела дня!"
    i "То-то я и говорю"
    e "А я то чем помочь могу?! Не понимаю"
    i "А ты его соседка сверху и тем более, сегодня он к тебе заходил час назад. Дашь показания."
    e "А что украли?"
    i "Статую Зевса из металла посеребренную! Семейная ценность с 1912 года, от деда!"
    e "Понимаю, скоро буду, дайте оденусь."
    scene black with fade
    "Я нацепила куртёжку, шаровары - как их называют пенсионеры и вышла. За модой я слежу!"
    e "Пропустите, извините, пропустите!"
    "Пришлось говорить, чтобы протолкнуться."
    sosed "А ты кто такая, чтобы я тебя пускал?"
    e "А я соседка!"
    sosed "Ладно, проходи, соседушка."
    scene egorich_crashed_home with fade
    "Войдя в квартиру без двери, та лежала на полу, я увидела разбитый шифоньер,"
    "Достояние Егорыча,"
    "Разбитое окно,"
    "Егоровича, рассказывающего что-то полицейскому"
    "И приготовленный ужин."
    scene black with fade
    "Затем два часа давала показания."
    "Скукотища!"
    "Как можно отменить пытки и оставить нужные вопросы милиционера: "
    "Где были, как выглядел Егорович и т.п"
    "Василиса Кирилловна пригласила к столу, перекусить, но я пошла домой, дела есть."
    scene home with fade
    "Они все подозревают в похищении того мужика сверху."
    "Егорович не видел этого жильца, странное событие."
    "Тем более его квартира опустела."
    "И конечно камеры, очи правительства!"
    "От них не уйти. {w}Но он замел следы…"

    window hide
    scene chapter1 with fade
    pause

    n "В оригинальной версии написана назывными нераспространенными предложениями, но для облегчения читателя будет изменена, но в простой манере."
    n "Все будет происходить в голове нервно спящего человека!"
    nvl clear
    "Детство моё проходило на морском побережье в Астраханской области."
    "Отец - рыбак, много пил."
    "А мать боролась с ним и рано умерла."
    menu:
        "Но она была злой, она никогда меня не любила.":
            $ end -=1
        "Она одна любила меня. Это отец убил ее ночью.":
            "Где он сейчас, не знаю, но при встрече шею сломаю."
            $ end += 1
        
    "Я свернул на плохую дорожку."
    "Чайки, ветер, волны, шторм- самое приятное воспоминание из детства."
    "Берег, крабы, кабаки."
    "Поворот на дорогу пьянства, зла и дьявола. "
    "Черти ходят вокруг меня."
    "Зона, Березники, шесть лет."
    "Пьянство, автобус и в Пермь."
    "Пьян, {w}трезв, {w}пьян."
    "И опа - долг."
    "Картишки, {w}долг."
    "Покер, {w}долг."
    "Ставки, {w}долг."
    "Вначале везло, а потом нет."
    "Должище накопился размером с Евразию."
    "Беру кредит, скрытность от ментов."
    "Одиночество и на дно."
    "Углубляется в днище жизни."
    "Проститутки каждый день."
    "Деньги закончились."
    "Днище."
    "Жизнь надоела."
    "Не могууууууууууууууу."
    "Днище. {w}Долг. {w}Грабеж.{w} Побег."
    "Пришлось бежать в лес, вышел на остановке 666 автобуса, загородный какой-то. {w}Статуя Зевса."
    "Свет."
    "Ночь."
    "Свет."
    "Страх."
    "Прячусь."
    "Страх."
    "Я увидел мощь природы и выбросил деньги и статуйку."
    "А может и не из-за этого ?!"
    "Село."
    "Предгорья."
    "Путь."
    "Урал."
    "Хижина."
    "Жители."
    "Есть среди них деды, бабки, девушки и парни, дети - сплошная деревенщина."
    "Есть умный приезжий священник, но взяточник."
    "Есть девушка, весьма привлекательная, из города, приехала \"к бабушке\", но нет у нее здесь бабушки, врёт. "
    window hide
    scene chapter2 with fade
    pause
    scene village with fade
    E "Это весна!"
    E "Наконец можно будет покопаться в земле!"
    E "Яблочки, вишенки; капуста и морковка!"
    E "Да, у нас конечно не чернозем Воронежской области, но дерново-подзолистая есть на родном Урале!"
    E "У, какой запах: дымок из бани, почва, оттаявшая после зимы, пропиталась влагой и готова к работе."
    E "У, какие звуки: птички поют, стадо коров идёт с прогулки, травы ещё нет, ноги разминают, ой слышен стук топора, мужики дрова колют."
    E "Весело на душе!"
    E "Спокойно!"
    E "Грусть прилетела с ветром и обуяла меня!"
    E "Не слышно запевки молодецкой сейчас!"
    E "Девки и парни дома сидят!"
    E "Где песни?!"
    E "Где, ты народ?!"
    E "А народ спрятался в погреба, ушел глубоко в норы."
    E "Только старики помнят живость деревни!"
    E "Все живут сейчас, как свои маленькие деревушки, а не село."
    E "Где песни?"
    E "Ку-ку - ответила кукушка."
    E "Эй ты, степь широоокаая, степь раздооольнаая, ах ты, Сылва- матушка,  Сылва милая!"
    E "Ой да не степной орёл подымаааается, ой да то речной бурлак разгулчаается."
    E "Не летай орёл близка каа земле!"
    E "Ой, да, не, гуляай ,бурлак, близко к берегу!"
    "По-весеннему сказал Егорович, распевая песни своей молодости!"
    show egorich at left with dissolve
    show vasilisa at right with dissolve
    v "Чаво распался, петушок?"
    "Василиса вышла на порог."
    E "Душа поет, Василиса, кумушка моя!"
    v "Ой, чувствительный ты наш! Давай, Егорыч, подсоби мне: полка упала, дрова не рублены, а ты поешь!"
    E "Ууу, практикантка"
    v "Давай, соловушка Сылвы. Год новый встречать пора!"
    hide vasilisa with dissolve
    "И ушла, оставив его одного. "
    "Да не один он был, с ним рядом природа - мощный собеседник!"
    scene village_tropa with fade
    show Boria with dissolve
    "Дядя Боря шел по просёлочной дорожке, бормоча"
    B " Эти не приехали, этот не приехал, кто хоть есть то?!"
    "И шел дальше, он же живёт здесь круглый год, да ещё парочка колхозников!"
    hide Boria with dissolve
    show Boria at left with dissolve
    show Egorich at right with dissolve
    B "Егорыч, здарова дорогой! Сколько лет сколько зим!"
    E "И тебе привет, Борька! Как жизнь, не замёрз?"
    "Посмеиваясь, говорил Егорович."
    B "Да нет, это вы перегрели свои зады, я хочу в Воркуту."
    E "А нахрена?"
    B "Да поговаривают, шо там хаты дешёвые и мне работёнка мож найдется."
    E "Эва, какой шустрый! Смелый! В Воркуту собрался! Э не, брат, не все так просто!"
    B "А шо?"
    E "Да не перспективное это направление, загнивает потихоньку! Я то знаю, географ!"
    B "А куда ж деваться? Скоро дом отберут! Совсем голый буду ходить!"
    E "Попробуй на Чукотку смотаться! Только туда год идти! Но платят хорошо."
    B "Правда?"
    E "Истинная, купишь себе потом квартирку в Москве, а не в Воркуте!"
    B "Идея то славная, а как добраться то туда?!"
    E "Прочертим маршрут на карте, у меня есть большая. И пойдешь пешком, мож кто и подвезет?"
    B "Пойду! Егорыч , благодарю тебя от всего своего пропитого сердца. Завтра в 10 утра у дуба, около Евдокимовой хаты!"
    E "А, это та ворчливая колдунья"
    B "Да да, мы ее всегда боялись раньше!"
    E "Приду."
    B "Жду."
    scene black with wipeleft
    "Тем временем этот разговор подслушивал Иоганн, не Бах, а Бесский. Так в паспорте написано."
    "Все его звали Йога или Бес. А если хотите узнать побольше о нем: то {w} паспорт поддельный так давно, когда ещё разруха 90-ых царила в России! {w} А настоящее его имя: Анатолий Роговой!"
    "Но это уже покрылось столькими слоями пыли и времени, что никто, даже он сам, не знал об этом. {w} Вот такая интересная история!"
    "Но это ещё не все, дядя Боря, наш знакомый пьяница, тоже имел фамилию Бесский!"
    "Да, да , {w} но по паспорту!"
    "Иоганн скрывался в этой глухой деревне, но надежды на стопроцентную защиту от глаз ментовских было мало и он уже подумывал,"
    "куда бы уехать.{w} А тут Чукотка - даль-далющая, неизведанный край, Дак и с деньгами в придачу!"
    "Ууууууу, как притянуло человека это!"
    "Иоганн пошел придумывать план: да тут и нечего придумывать: найти этого чухлого старика, отобрать паспорт и карту местности, да сбрить усы не помешало бы.{w} И в путь!"
    " Только где это, Евдокимова хата?"
    "Надо поспрашивать у местных, {w}но у стариков опасно, разболтают либо чухлику, либо его дружку, надо молчаливого кого-то.."
    "Опа-па, идёт девушка какая-то."
    "Присмотревшись, он понял, что эта та самая городская, и решил, что его любит Бог, и ,спрыгнув как можно тише, не повредив ни веточки, подошёл к ней."
    scene village_tropa with fade
    show anastsia at right with dissolve
    show Iogan at left with easeintop
    "Я застыла от испуга,{w} дааа, вид у мужчины был не очень привлекательный."
    e "Вы кто такой, и что вам нужно от меня?"
    s "Да вот, подумываю, какая красивая девушка идёт, надо познакомится"
    "C напущенной важностью сказал он."
    e "С такими не знакомлюсь!"
    c "Ой какая. А что во мне не нравится вам?"
    e "Ну какой-то вы смутный!"
    "Хотя заметить можно он был чистенький и опрятный, в новом костюме: футболка и шорты."
    s "Ой, а какие нужны?"
    e "Джентльмены."
    s "Устроим, устроим. {w} Дама, пойдете со мной на свидание?"
    "Ожидая благоприятного ответа, сказал мужчина."
    e "Ладно, пойдем."
    "Mне все равно нечего делать, {w} и с этой мыслью я пошла не пойми куда с не пойми кем."
    pause
    "По дороге к холму, где собирались все парочки села, Йога рассказал мне про себя:"
    "работает в фирме "ЛУКОЙЛ" начальником отделения, а сюда приехал на отдых к родителям, помочь с огородом."
    "Он не женат и никогда не был. {w} Уииху- заорал голос в голове, наконец-то парня найду, а то все подружки уже замужем."
    "По пути он нарвал цветов."
    "Миленький букетик! Ромашки, васильки и даже пижма!"
    "Оригинальный человек, подумала я!"
    scene holmnazakate with dissolve
    "На холме открывался прекраснейший вид на закат."
    "Работники шли с поля. Скот загоняли палками молодые пастушки."
    "А мы сидели, уже обнявшись, как быстро сближаемся. У меня внутри что-то разгоралось. {w} Возбужденно уже я говорила, а щеки все покраснели."
    "Не любила я такие сцены в фильмах и книгах, хоть сама о них и писала."
    "Темные времена начинались в селе."
    "Но вместо того, чтобы идти к бабушке на чай я пошла с Йогой в какой-то дом."
    "Как он и сказал, не хоромы, но поспать можно."
    scene homeEvdokii with dissolve
    "Темнело, {w} но мне не страшно становилось, а наоборот как-то ярче."
    "Вот мы легли на кровать. {w} Он обхватывает мою талию."
    "Пошли бесконечные поцелуи."
    "Я как будто куда-то катилась. Но не на дно, а на Эверест. "
    "Я чувствую одну из вершин, {w} запускаю руку в ….."
    "В один момент я вспоминаю Пашу. 4 года назад, в другой комнате. {w} Но он был убит."
    "Но я не могла долго думать…  {w} Я прыгала по острым вершинам, и постепенно подбиралась к Эвересту… "


