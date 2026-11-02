# -*- coding: utf-8 -*-
"""Tool specs for module M2 (common multiples and LCM)."""
from topics_common import T

TOOLS = {
    "toran_builder": T(
        "tool_toran_builder", "Toran Builder", "simulation",
        "Strips of one length laid end to end reach only multiples of that length; a toran of two strip lengths is "
        "complete where both reach the same total, and the first such length is the LCM.",
        "Two rows of coloured strips of chosen lengths laid end to end on a ruler; a marker line for each total; common "
        "totals light up on both rows; an LCM slot.",
        ["Choose the two strip lengths and add strips to each row.",
         "Watch the totals each row reaches and spot where both rows end at the same mark.",
         "Name the shortest length where both rows end together.",
         "Check the answer against the multiple lists shown beside the rows."],
        ["Strips of 6 cm and 8 cm (first match at 24 cm).", "Strips of 4 cm and 10 cm (20 cm).",
         "Strips of 9 cm and 12 cm (36 cm).", "Strips of 5 cm and 7 cm (35 cm).",
         "Strips of 8 cm and 12 cm (24 cm).", "Strips of 6 cm and 15 cm (30 cm)."],
        ["A length where only one row ends is marked, with the other row's gap shown.",
         "A common length that is not the first is accepted as a common multiple but not as the lowest.",
         "The LCM slot lights up only for the first common mark."],
        "All six pairs are done with the lowest common length correct.",
        ["stripA", "stripB", "countA", "countB", "totalsA", "totalsB", "lcm", "cardIndex"],
        ["M_LCM_BIG", "M_LCM_PRODUCT"],
        ["Where does the first row end after one strip, two strips, three strips?",
         "Write the totals for each row and look for a number in both lists.",
         "Take the smallest number that appears in both lists.",
         "Both lists are shown, the shared totals are highlighted and the smallest is the LCM; a new pair follows."]),

    "schedule_matcher": T(
        "tool_schedule_matcher", "Schedule Matcher", "simulation",
        "Two events repeating every few days coincide on the days that are common multiples of both gaps; the first "
        "such day is the LCM.",
        "A calendar strip of days; for each event a row of dots on its repeating days; days where both dots fall "
        "together are circled; a day counter and a gap picker for each event.",
        ["Choose the repeat gap for each event.",
         "Run the calendar and watch the days each event happens.",
         "Circle the first day both events happen together.",
         "Say the next day after that and compare with the LCM."],
        ["Gaps 10 days and 7 days (first together on day 70).", "Gaps 4 days and 6 days (day 12).",
         "Gaps 6 days and 9 days (day 18).", "Gaps 5 days and 8 days (day 40).",
         "Gaps 12 days and 18 days (day 36).", "Gaps 10 days and 15 days (day 30)."],
        ["A day where only one event happens is shown with the other event's nearest days.",
         "After the first match the tool shows that the next matches repeat after the same number of days.",
         "The match is confirmed by dividing the day by both gaps with no remainder."],
        "All six pairs are done with the first matching day correct.",
        ["gapA", "gapB", "daysA", "daysB", "firstDay", "cardIndex"],
        ["M_LCM_PRODUCT", "M_LCM_BIG"],
        ["On which days does the first event happen? Write the first few.",
         "List the days for both events and look for a day in both lists.",
         "Find the smallest day that both gaps divide exactly.",
         "Both day lists are shown, the shared days are circled and the first is the LCM; a new pair follows."]),

    "lcm_builder": T(
        "tool_lcm_builder", "LCM Builder", "manipulative",
        "The LCM takes the most copies of every prime from the two prime factorisations; building it from tiles of "
        "primes shows why nothing smaller works.",
        "Two prime factorisations shown as rows of prime tiles; a build tray; each prime has a counter showing its "
        "copies in each number; a check button that tests divisibility by both numbers.",
        ["Break both numbers into prime tiles.",
         "For each prime, compare the copies in the two rows and place the larger count in the tray.",
         "Multiply the tray to get the LCM.",
         "Press Check to test that both numbers divide it and that removing a tile breaks this."],
        ["14 and 35 (LCM 70).", "96 and 360 (LCM 1440).", "12 and 18 (LCM 36).", "20 and 30 (LCM 60).",
         "45 and 75 (LCM 225).", "84 and 90 (LCM 1260)."],
        ["Taking the smaller count of a prime fails the divisibility check, with the number that does not divide shown.",
         "Adding an extra tile passes the check but is marked as not the lowest.",
         "Using only the shared primes fails, and the missing primes are highlighted."],
        "All six pairs are done with the right tray and the LCM correct.",
        ["numA", "numB", "primesA", "primesB", "tray", "lcm", "cardIndex"],
        ["M_MIN_MAX", "M_COMMON_PRIMES_ONLY"],
        ["Which primes make up each number?",
         "For each prime, which number has more copies of it?",
         "Put the larger count of each prime into the tray, including primes that are in only one number.",
         "Each prime's larger count is placed in the tray and multiplied to give the LCM; a new pair follows."]),
}
