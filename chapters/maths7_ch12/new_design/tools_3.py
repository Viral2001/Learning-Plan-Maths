# -*- coding: utf-8 -*-
"""Tool specs for module M3 (decimals at work)."""
from topics_common import T

TOOLS = {
    "leap_rule_ledger": T(
        "tool_leap_rule_ledger", "Leap Rule Calendar Drift Ledger", "simulation",
        "A year is 365.2422 days, so a calendar rule is judged by comparing the days it gives over many years with the "
        "true total; each new rule fixes the gap left by the last one.",
        "A ledger for a span of years (4, 100, 400, 1000 or 10000); switches for the rules: every 4th year, skip every "
        "100th, keep every 400th; a counter of leap and ordinary years; the calendar total beside the true total "
        "365.2422 × years; the gap in days shown as a bar.",
        ["Predict whether the calendar runs ahead of or behind the Earth.",
         "Switch a rule on and read the counts of 366-day and 365-day years.",
         "Compare the calendar total with the true total.",
         "Propose a rule that shrinks the gap."],
        ["4 years, every 4th year leap (1461 against 1460.9688).",
         "100 years, every 4th year leap (36525 against 36524.22).",
         "100 years, skip the 100th year (36524 against 36524.22).",
         "1000 years with the 400 rule (365242 against 365242.2).",
         "10000 years with the 400 rule (3652425 against 3652422).",
         "Propose a fix for 10000 years and test it."],
        ["A wrong count of leap years is checked year by year on a strip.",
         "The gap bar turns red when the calendar is more than a day off.",
         "A proposed rule is applied and its new gap is shown."],
        "All five spans are checked and one fix for 10000 years is tested.",
        ["years", "rule4", "rule100", "rule400", "leapCount", "calendarDays", "trueDays", "gap", "cardIndex"],
        ["M_UNIT_MIX"],
        ["How many days does the Earth really take for these years?",
         "Multiply 365.2422 by the number of years and compare with the calendar.",
         "Count the leap years under the rules switched on, then add one day for each to 365 times the years.",
         "The ledger shows both totals and the gap; a similar span follows."]),
}
