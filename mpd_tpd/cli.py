"""Main program code"""

import argparse
import datetime
from decimal import Decimal


def valid_date(input_date_str: str) -> datetime.datetime:
    """Date parser used by argparse.ArgumentParser().
    Attempts to parse given date string, otherwise raising an error"""
    try:
        return datetime.datetime.strptime(input_date_str, "%Y-%m-%d").date()
    except ValueError:
        raise argparse.ArgumentTypeError(f"not a valid date: {input_date_str!r}")


def mpd_tpd(
    next_payday: datetime.date,
    money_remaining: Decimal,
    fixed_expenses: Decimal,
    include_today: bool,
) -> tuple[int, Decimal]:
    """Calculates how much money can be spent each day until your next payday, distributing remaining money uniformly (i.e. same spend each day)

    Args:
        next_payday (datetime.date): Date on which you will next be paid
        money_remaining (Decimal): Amount of money remaining (which needs to last you until your next payday)
        fixed_expenses (Decimal): Total pending payments (to be paid before your next payday) which are non-negotiable
        include_today (bool): I still want to spend money today (i.e. it is the beginning of the day)

    Returns:
        tuple[int, Decimal]: Tuple containing (number_of_spending_days_remaining, amount_of_money_can_be_spent_per_day)
    """
    today_date: datetime.date = datetime.date.today()
    if today_date >= next_payday:
        raise ValueError("`next_payday` must be in the future")
    days_til_payday: int = (next_payday - today_date).days
    if not include_today:
        days_til_payday -= 1
    money_can_spend_per_day: Decimal = (
        money_remaining - fixed_expenses
    ) / days_til_payday
    return days_til_payday, money_can_spend_per_day


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "-p",
        "--next_payday",
        help="Date on which you will next be paid. Required format is YYYY-MM-DD e.g. 2069-07-24",
        required=True,
        type=valid_date,
    )
    arg_parser.add_argument(
        "-m",
        "--money_remaining",
        help="Amount of money remaining (which needs to last you until your next payday)",
        required=True,
        type=Decimal,
    )
    arg_parser.add_argument(
        "-f",
        "--fixed_expenses",
        help="Total pending payments (to be paid before your next payday) which are non-negotiable",
        default=Decimal("0"),
        type=Decimal,
    )
    arg_parser.add_argument(
        "-t",
        "--include_today",
        help="I still want to spend money today (i.e. it is the beginning of the day)",
        action="store_true",  # set to include_today=True if flag is present
    )
    args = arg_parser.parse_args()
    days_til_payday, money_can_spend_per_day = mpd_tpd(
        next_payday=args.next_payday,
        money_remaining=args.money_remaining,
        fixed_expenses=args.fixed_expenses,
        include_today=args.include_today,
    )
    print(
        f"""
You have {days_til_payday:,} days left until payday ({args.next_payday.strftime("%A")} {args.next_payday}) 
You have {args.money_remaining:,.2f} left to spend and {args.fixed_expenses:,.2f} still to pay in fixed expenses before then.
This means that you have {(args.money_remaining-args.fixed_expenses):,.2f} = ({args.money_remaining:,.2f} - {args.fixed_expenses:,.2f}) in total to spend until payday.
i.e. you can spend {money_can_spend_per_day:,.2f} per day until you will be paid again.
        """
    )
