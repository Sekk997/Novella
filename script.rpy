# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define m = Character('Макс', color="#ff0000")
define c = Character('Загад', color="#ff00ff")
define l = Character('Лиза', color="#00ff00")
define a = Character('Алиса', color="#0000ff")
define w = Character('Марта', color="#008000")
define r = Character('Рома', color="#008000")

define audio.mus1 = "audio/music1.mp3"
define audio.mus2 = "audio/music2.mp3"
define audio.dec = "audio/dec.mp3"

image cafe = "bg/cafe.png"
image forest = "bg/forest.png"
image home = "bg/home.png"
image kitchen = "bg/kitchen.png"
image library = "bg/library.png"
image room = "bg/room.png"
image rooma = "bg/rooma.png"
image school = "bg/school.png"
image school1 = "bg/school1.png"
image school2 = "bg/school2.png"
image ulica = "bg/ulica.png"
image black = "bg/black.png"

image maks1 = "maks/maks1.png"
image maks2 = "maks/maks2.png"
image maks3 = "maks/maks3.png"
image maks4 = "maks/maks4.png"
image maks5 = "maks/maks5.png"
image maks6 = "maks/maks6.png"
image maks7 = "maks/maks7.png"
image maks8 = "maks/maks8.png"
image maks9 = "maks/maks9.png"

image makss1 = "makss/makss1.png"
image makss2 = "makss/makss2.png"
image makss3 = "makss/makss3.png"
image makss4 = "makss/makss4.png"
image makss5 = "makss/makss5.png"
image makss6 = "makss/makss6.png"
image makss7 = "makss/makss7.png"
image makss8 = "makss/makss8.png"

image alisa1 = "alisa/alisa1.png"
image alisa2 = "alisa/alisa2.png"
image alisa3 = "alisa/alisa3.png"
image alisa4 = "alisa/alisa4.png"
image alisa5 = "alisa/alisa5.png"
image alisa6 = "alisa/alisa6.png"
image alisa7 = "alisa/alisa7.png"
image alisa8 = "alisa/alisa8.png"

image cat1 = "cat/cat1.png"
image cat2 = "cat/cat2.png"
image cat3 = "cat/cat3.png"
image cat4 = "cat/cat4.png"
image cat5 = "cat/cat5.png"
image cat6 = "cat/cat6.png"
image cat7 = "cat/cat7.png"
image cat8 = "cat/cat8.png"

image liza1 = "liza/liza1.png"
image liza2 = "liza/liza2.png"
image liza3 = "liza/liza3.png"
image liza4 = "liza/liza4.png"
image liza5 = "liza/liza5.png"
image liza6 = "liza/liza6.png"
image liza7 = "liza/liza7.png"
image liza8 = "liza/liza8.png"

image marta1 = "marta/marta1.png"
image marta2 = "marta/marta2.png"
image marta3 = "marta/marta3.png"
image marta4 = "marta/marta4.png"
image marta5 = "marta/marta5.png"
image marta6 = "marta/marta6.png"
image marta7 = "marta/marta7.png"
image marta8 = "marta/marta8.png"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

label splashscreen:
    scene sta3
    with Pause(1)

    show text "{i}{b}New Reality...{/b}{/i}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

transform slightleft:
    xalign 0.25
    yalign 1.0

transform slightright:
    xalign 0.75
    yalign 1.0

# Игра начинается здесь:


label start:

    scene forest

    play music mus1

    "(((" "Привет"

    show cat3
    with dissolve

    "Кот" "Эй, я тут!"

    hide cat3
    show cat1
    with dissolve

    "Кот" "Слушай меня внемательно и не отвлекайся"

    "Кот" "Я поведаю тебе историю о парне, который случайным образом попал в другой мир, а правда это или нет, решать тебе"

    hide cat1
    show cat8
    with dissolve

    "Кот" "Приятной игры"

    hide cat8
    scene black

    "Звук будильника"

    "Кот" "Стой!!!"

    scene forest
    show cat6
    with dissolve

    "Кот" "Фух, успел"

    hide cat6
    show cat1
    with dissolve

    "Кот" "Как не культурно было с моей стороны"

    c "Я же совсем забыл представиться, меня зовут Загад"

    c "А теперь, приятной игры"

label sturt:

    scene black
    with dissolve

    "Звук будильника"

    play sound dec

    m "Еще пять минуток"

    "Звук будильника"

    play sound dec

    m "Да все, встаю я"

    scene rooma

    "..."

    m "Как же хочется еще поспать, хотя бы до завтра"

    m "Не стоило играть в Доту всю ночь"

    m "Знал же, что не высплюсь"

    m "Ладно, пора одеваться"

    "..."

    show makss3
    with dissolve

    "..."

    m "Как же кушать хочется"

    hide makss3
    show makss5
    with dissolve

    m "Надо cходить позавтракать"

    scene kitchen

    ""

    show makss4
    with dissolve

    m "Так, посмотрим, что же у нас тут есть cъедобного"

    ''

    hide makss4
    show makss8
    with dissolve

    m "Пустая пачка печенья"

    m "А они ведь были такими вкусными, постоянно забываю их купить"

    hide makss8
    show makss3
    with dissolve

    m "Хм"

    m "Мертвый таркан, вот это находка"

    m "Надо будет провести генеральную уборку, нельзя ее откладывать"

    hide makss3
    show makss1
    with dissolve

    m "Вдруг, деньги найду"

    hide makss1
    show makss3
    with dissolve

    m "Так, не будем мечтать"

    menu:
        m "Надо думать о том, чем я позавтракаю"
        "Ничего не есть":
            jump tarakan

        "Сходить в кафе":
            jump cafe

    label tarakan:
    m "Ладно, поем вечером"

    scene black

    "..."

    scene ulica

    "..."

    scene black

    "Пришли"

    jump sco

    label cafe:

    hide makss3
    show makss6
    with dissolve

    m "Дамы и господа приготовьтесь, мы отправляемся в кафе"

    scene black

    "..."

    scene ulica

    "..."

    scene black

    "Пришли"

    scene cafe
    show makss3
    with dissolve

    m "Наконец-то, я уже устал идти"

    hide makss3
    show makss4
    with dissolve

    m "Сяду и дождусь официанта"

    hide makss4
    with dissolve

    m "Так, ну, я наверно как обычно"

    show marta1
    with dissolve

    w "Привет, Макс"

    hide marta1
    show marta5
    with dissolve

    w "Тебе как обычно?"

    hide marta5
    show marta4
    with dissolve

    m "Привет, Марта"

    m "Да, как обычно"

    w "С тебя 140 рублей"

    w "У тебя наличные или карта?"

    m "Наличка, вот"

    w "Хорошо"

    hide marta4
    show marta5
    with dissolve

    w "Через 10 минут будет готово"

    m "Жду"

    hide marta5
    scene black

    "A few moments later"

    scene cafe
    show marta1
    with dissolve

    w "Прошу, приятного аппетита"

    m "Cпасибо"

    hide marta1

    ""

    scene black

    "Через 5 минут, сытного обеда"

    scene cafe
    with dissolve

    m "Спасибо, пока"

    w "До завтра"

    scene ulica
    with dissolve

    ""

    label sco:

    scene school

    show makss3
    with dissolve

    m "Только подошел к школе, а уже желание пропало туда идти"

    m "Может быть, пойти домой"

    menu:
        m "Что делать?"
        "Пойти в школу":
            jump cend

        "Прогулять школу":
            jump end

    label end:

    show makss5
    with dissolve

    m "Пойду домой, не очень то и хотелось туда заходить"

    m "Займусь, чем-то полезным"

    hide makss5
    scene black
    with dissolve

    "A few moments later"

    scene rooma
    show makss4
    with dissolve

    m "Так, что же мне делать?"

    hide makss4
    show makss6
    with dissolve

    m "Знаю, я пойду в доту"

    m "Приступим"

    scene black
    with dissolve

    "На следующее утро"

    jump sturt


    label cend:

    scene school1
    with dissolve
    show makss3:
        xalign 0.75
        yalign 1.0
    with dissolve

    m "Так, надо посмотреть в каком кабинете у меня урок"

    show alisa15:
        xalign 0.25
        yalign 1.0
    with dissolve

    a "O, привет"

    m "Привет"

    hide alisa15
    show alisa13:
        xalign 0.25
        yalign 1.0
    with dissolve

    a "Выспался"

    m "Не совсем, всю ночь в доту играл"

    a "Ты как всегда"

    m "Ты не знаешь, в каком кабинете у нас урок?"

    a "Если я не ошибаюсь, 214"

    m "Тогда я уже пойду, спасибо"

    a "Давай"

    scene school2
    show makss3
    with dissolve

    m "Посплю до начала уроков"

    m "Может высплюсь чуть-чуть"

    hide makss3
    with dissolve

    m "Приятных мне снов"

    scene black
    with dissolve

    stop music

    ""

    "Просыпайтесь"

    m "Да-Да, все, я проснулся"

    scene room
    with dissolve

    play music mus2

    m "Где это я"

    m "Я же был в классе, когда ложился"

    show liza6
    with dissolve

    "???" "Доброго утра вам"

    "???" "Как вам спалось?"

    m "Отлично, вроде"

    m "Прошу прощения, а ты кто?"

    hide liza6
    show liza3
    with dissolve

    l "Молодой господин, я Лиза, ваша служанка,"

    m "Господин? Лиза? Служанка?"

    l "Странно, что это вас так удивляет, может вы заболели"

    l "Я сейчас же вызову врача"

    m "Все хорошо, не надо, я просто решил подшутить над тобой"

    hide liza3
    show liza8
    with dissolve

    l "У вас не получается шутить, прекращали бы вы с этим"

    m "Постараюсь"

    hide liza8
    show liza4
    with dissolve

    l "Одевайтесь и спускайтесь вниз, я буду вас ждать"

    m "Хорошо"

    hide liza4
    with dissolve

    m "Так, я пришел в школу, лег на парту и уснул"

    m "Теперь я здесь"

    m "Скорее всего это сон и я еще сплю"

    m "Хотя, не очень похоже, что это сон"

    m "Ладно, надо вставать"

    m "Разберусь в этом по ходу событий"

    show maks4
    with dissolve

    m "А мне нравится эта одежда"

    m "Довольно таки прикольно смотрится"

    m "Мне бы еще трубку и вылитый Шерлок Холмс"

    m "Она вроде говорила, что мне вниз надо спуститься"

    scene holl
    with dissolve

    show maks9:
        xalign 0.75
        yalign 1.0
    with dissolve

    m "Вау, как здесь красиво"

    hide maks9
    show maks4:
        xalign 0.75
        yalign 1.0
    with dissolve

    m "Видимо, мы очень богато живем, такой дом и служанка ничего такая"

    show liza14:
        xalign 0.25
        yalign 1.0
    with dissolve

    l "Вы что-то сказали?"

    hide maks4
    show maks8:
        xalign 0.75
        yalign 1.0
    with dissolve

    m "Нет, ничего, мысли вслух"

    l "Понятно"

    hide maks8
    show maks5:
        xalign 0.75
        yalign 1.0
    with dissolve

    l "Ваши родители уехали на неделю в город"

    l "Поэтому не беспокойтесь, что их нету"

    m "Я и не собирался беспокоиться"

    l "Вот и отлично"

    l "Что вы будете на завтрак?"

    m "Я не голоден, лучше пойду прогуляюсь"

    l "Хорошо, будьте осторожны и не забывайте, что в лес ходить нельзя"

    scene dom
    with dissolve

    show maks9
    with dissolve

    m "А снаружи он еще красивее"

    m "Надо пройтись, и обдумать, что делать здесь дальше"

    menu:
        m "Куда пойти?"
        "В сторону леса":
            jump les

        "в сторону деревни":
            jump der

    label les:

    hide maks9
    show maks2
    with dissolve

    m "Она сказала не ходить в лес"

    m "Интересно, почему"

    scene les1
    with dissolve

    m "Блин, здесь так красиво"

    m "Жаль, что я не могу это заснять"

    m "Пополнил бы свою коллекцию"

    "аууууууууу"

    m "Я слышал вой"

    m "Надо идти дальше"

    m "Не хотелось бы встретить здесь волков"

    scene les2
    with dissolve

    m "Ооо, домик в лесу"

    show zak2
    with dissolve

    "..." "Здравствуй, что привело тебя сюда"

    m "Привет, я просто гуляю"

    hide zak2
    show zak6
    with dissolve

    "..." "Хм, просто гуляешь"

    m "Да, решил подышать свежим воздухом"

    "..." "Мне кажется, что ты не от сюда"

    m "Нет, у меня здесь дом неподалеку"

    "..." "Ты не совсем правильно меня понял"

    "..." "Люди из этих мест знают, что в лес ходить запрещено"

    "..." "Ты же не из этого мира"

    "..." "Верно?"

    m "Да"

    hide zak6
    show zak3
    with dissolve

    m "Но я совершенно не понимаю. как сюда попал"

    m "Уснул за партой, а проснулся в этом мире"

    hide zak3
    show zak1
    with dissolve

    "..." "Давай я помогу тебе, вернуться обратно"

    m "Давай, но как?"

    "..." "Все очень просто"

    "..." "Тебе нужно закрыть глаза, а дальше я все сделаю сам"

    m "Хорошо"

    scene black
    with dissolve

    m "Не думал, что все будет настолько просто"

    m "Кстати, а как тебя зовут?"

    "..." "Это уже не важно"

    scene end
    with dissolve

    "Вас убили"

    "Конец игры"

    return

    label der:

    hide maks9
    show maks5
    with dissolve

    m "Так и сделаем"

    m "Лиза, говорила не ходить в лес"

    m "А выбора особо и нет"

    m "Поэтому, пойду в деревню"

    scene black
    with dissolve

    "Спустя 30 минут"

    scene derevnya1
    with dissolve

    m "Фух, наконец-то"

    m "Думал откинусь"

    m "Так высоко подниматься"

    scene derevnya2
    with dissolve

    m "Главное, на наткунться здесь на неприятности"

    show roma5
    with dissolve

    r "Привет, меня зовут Рома"

    hide roma5
    show roma1
    with dissolve

    m "Круто, очень рад за тебя"

    hide roma1
    show roma5
    with dissolve

    r "А тебя как зовут?"

    m "Макс"

    r "Очень приятно познакомиться"

    r "Ты впервые здесь?"

    m "Если не ошибаюсь, то да"

    r "Могу провести тебе экскурсию"

    m "Буду признателен"

    hide roma5
    show roma6
    with dissolve

    r "Тогда, вперед"


    scene continued

    "To be continued"

    return
