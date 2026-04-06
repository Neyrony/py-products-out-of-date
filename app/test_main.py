from datetime import date
from unittest import mock


import pytest


from app.main import outdated_products


@pytest.mark.parametrize("list_of_food, expected_output", [
    ([
        {
            "name": "salmon",
            "expiration_date": date(2026, 4, 10),
        },
        {
            "name": "chicken",
            "expiration_date": date(2026, 4, 8),
        },
        {
            "name": "duck",
            "expiration_date": date(2026, 4, 1),
        }
    ],
        ["duck"]),
    (
        [],
        []
    ),
    ([
     {
         "name": "turkey",
         "expiration_date": date(2026, 4, 5),
     },
     {
         "name": "cheese",
         "expiration_date": date(2026, 4, 1),
     },
     {
         "name": "chicken",
         "expiration_date": date(2026, 3, 30),
     }
     ],
        ["turkey", "cheese", "chicken"],
     ),
    (
        [
            {
                "name": "beef",
                "expiration_date": date(2026, 4, 10),
            },
            {
                "name": "pork",
                "expiration_date": date(2026, 4, 8),
            },
            {
                "name": "tofu",
                "expiration_date": date(2026, 12, 4),
            }
        ],
        []
    )
])
@mock.patch("app.main.datetime.date")
def test_outdated_products(
        mocked_date_today: mock.MagicMock,
        list_of_food: list[dict],
        expected_output: list) -> None:
    mocked_date_today.today.return_value = date(2026, 4, 6)
    assert outdated_products(list_of_food) == expected_output
