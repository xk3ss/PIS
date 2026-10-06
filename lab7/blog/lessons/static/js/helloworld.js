var lessons = [
    {
        "subject": "Педагогика",
        "lesson_type": "Лекция",
        "teacher": "Иванов И.И.",
        "group": "ПК-21",
        "hours": 20,
        "rate": 500
    },
    {
        "subject": "Педагогика",
        "lesson_type": "Практика",
        "teacher": "Иванов И.И.",
        "group": "ПК-21",
        "hours": 10,
        "rate": 450
    },
    {
        "subject": "Информационные технологии",
        "lesson_type": "Лекция",
        "teacher": "Солдатенко М.П.",
        "group": "ПК-22",
        "hours": 30,
        "rate": 600
    },
    {
        "subject": "Методика преподавания",
        "lesson_type": "Лекция",
        "teacher": "Шилина М.О.",
        "group": "ПК-23",
        "hours": 25,
        "rate": 550
    }
];

console.log(lessons);

var rpad = function(str, length) {
    str = str.toString();
    while (str.length < length) str = str + ' ';
    return str;
};

var printLessons = function(items) {
    console.log(
        rpad("Предмет", 30),
        rpad("Вид", 12),
        rpad("Преподаватель", 20),
        rpad("Группа", 8),
        rpad("Часов", 8),
        rpad("Оплата", 8)
    );
    for (var i = 0; i < items.length; i++) {
        console.log(
            rpad(items[i]['subject'], 30),
            rpad(items[i]['lesson_type'], 12),
            rpad(items[i]['teacher'], 20),
            rpad(items[i]['group'], 8),
            rpad(items[i]['hours'], 8),
            rpad(items[i]['rate'], 8)
        );
    }
    console.log('\n');
};

printLessons(lessons);

var filterByGroup = function(items, groupName) {
    var result = [];
    for (var i = 0; i < items.length; i++) {
        if (items[i]['group'] === groupName) {
            result.push(items[i]);
        }
    }
    return result;
};

var groupName = prompt("Введите название группы (ПК-21, ПК-22, ПК-23):");
console.log("Занятия группы " + groupName + ":");
printLessons(filterByGroup(lessons, groupName));

var filterByHours = function(items, minHours) {
    var result = [];
    for (var i = 0; i < items.length; i++) {
        if (items[i]['hours'] >= minHours) {
            result.push(items[i]);
        }
    }
    return result;
};

var minHours = parseInt(prompt("Введите минимальное количество часов:"));
console.log("Занятия с часами >= " + minHours + ":");
printLessons(filterByHours(lessons, minHours));