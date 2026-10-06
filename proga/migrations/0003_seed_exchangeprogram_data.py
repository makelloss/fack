from django.db import migrations


INSERT_STATEMENTS = [
    """
    INSERT INTO proga_exchangeprogram
        (university, languages, places, deadline, description)
    VALUES (
        'Uniwersytet Warszawski, Польща',
        'польська, англійська',
        '5',
        '2026-11-15',
        'Найбільший і один з найстаріших університетів Польщі, заснований у 1816 році. Пропонує широкий вибір курсів для студентів з обміну польською та англійською мовами.'
    );
    """,
    """
    INSERT INTO proga_exchangeprogram
        (university, languages, places, deadline, description)
    VALUES (
        'KU Leuven (Бельгія)',
        'English',
        '2 місця',
        '2026-12-01',
        'Один з найстаріших університетів Європи, заснований у 1425 році. Відомий сильними дослідницькими програмами та англомовними курсами для іноземних студентів.'
    );
    """,
    """
    INSERT INTO proga_exchangeprogram
        (university, languages, places, deadline, description)
    VALUES (
        'Vilnius University, Литва',
        'англійська',
        'до 4',
        '2026-10-20',
        'Найстаріший університет країн Балтії, заснований у 1579 році. Пропонує курси англійською мовою для студентів-правників за обміном.'
    );
    """,
    """
    INSERT INTO proga_exchangeprogram
        (university, languages, places, deadline, description)
    VALUES (
        'Uniwersytet Jagielloński, Польща',
        'Польська, Англійська',
        '3',
        '2026-11-15',
        'Найстаріший університет Польщі, заснований у 1364 році в Кракові. Пропонує курси польською та англійською мовами на юридичному факультеті.'
    );
    """,
    """
    INSERT INTO proga_exchangeprogram
        (university, languages, places, deadline, description)
    VALUES (
        'University of Tartu - Естонія',
        'англійська, естонська',
        '2',
        '2027-01-10',
        'Найстаріший і найбільший університет Естонії, заснований у 1632 році. Пропонує курси англійською та естонською мовами, зокрема з міжнародного права.'
    );
    """,
    """
    INSERT INTO proga_exchangeprogram
        (university, languages, places, deadline, description)
    VALUES (
        'Masaryk University, Чехія',
        'англійська',
        '1 місце',
        '2026-09-30',
        'Другий за величиною університет Чехії, розташований у Брно. Юридичний факультет щороку пропонує обмежену кількість місць для студентів за обміном.'
    );
    """,
]

DELETE_STATEMENT = """
DELETE FROM proga_exchangeprogram WHERE university IN (
    'Uniwersytet Warszawski, Польща',
    'KU Leuven (Бельгія)',
    'Vilnius University, Литва',
    'Uniwersytet Jagielloński, Польща',
    'University of Tartu - Естонія',
    'Masaryk University, Чехія'
);
"""


class Migration(migrations.Migration):

    dependencies = [
        ("proga", "0002_exchangeprogram"),
    ]

    operations = [
        migrations.RunSQL(
            sql=INSERT_STATEMENTS,
            reverse_sql=[DELETE_STATEMENT],
        ),
    ]