# Money Per Day 'Til PayDay (mpd-tpd)

Command-line tool for helping you make your money last until you get paid again

```bash
$ mpd-tpd --help

usage: mpd-tpd [-h] -p NEXT_PAYDAY -m MONEY_REMAINING [-f FIXED_EXPENSES] [-c CURRENCY_FORMAT] [-t]

    +-------------------------------------+
    | Money Per Day 'Til PayDay (mpd-tpd) |
    +-------------------------------------+
    Command-line tool for helping you make your money last until you get paid again

    Examples:
        $ mpd-tpd --next_payday '2024-07-24' --money_remaining 100

        # if you still intend to spend money today, then include flag '--include_today':
        $ mpd-tpd --next_payday '2024-07-24' --money_remaining 99.99 --include_today

        # if you have known bills which you want pre-removed before doing the calculation,
        #   use parameter '--fixed_expenses':
        $ mpd-tpd --next_payday '2024-08-01' --money_remaining 80000 --fixed_expenses 25000

        # if you want the numbers formatted with a specific currency, specify the format
        #   using parameter '--currency_format'
        $ mpd-tpd --next_payday '2024-07-24' --money_remaining 50 --currency_format '£x'
        $ mpd-tpd --next_payday '2024-07-24' --money_remaining 99999 --currency_format 'x GBP'
```
