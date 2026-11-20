# -*- coding: utf-8 -*-
"""Step builders for Class 5 Chapter 9 (division). They write the numbered working of a division the way the book does
(taking away groups of the divisor, or sharing by place value) as plain sentences, and they ASSERT every number as they
go, so a wrong figure stops the import. The sentences follow the authoring rules of DESIGN.md section 1:
  * a division with a remainder is never one chain "n ÷ d = q": it is written "quotient q, remainder r" and the check
    "n = d × q + r" (a true chain);
  * place value words are words (thousands, hundreds, tens, ones), never the letters Th H T O;
  * minus is U+2212;
  * a parenthesis is never opened directly before a chain: the equation gate skips "(6 × 7 = 42)" at the first number and
    then reads "7 = 42" as a false chain.
Used by topics_1.py to topics_4.py; nothing here is read by build.py."""
from __future__ import annotations

MINUS = "−"
_PLACES = ["ones", "tens", "hundreds", "thousands", "ten thousands"]
_SINGULAR = {"ones": "one", "tens": "ten", "hundreds": "hundred", "thousands": "thousand", "ten thousands": "ten thousand"}


def fmt(x, comma=False):
    return "{:,}".format(x) if comma else str(x)


def unit(count, place):
    """'1 ten', '2 tens', '0 tens'."""
    return "%d %s" % (count, _SINGULAR[place] if count == 1 else place)


def pq(n, d, parts, comma=False):
    """Susie's way: take away `parts` groups of d one after the other. Returns (steps, quotient, remainder)."""
    f = lambda x: fmt(x, comma)
    cur, steps = n, []
    for k in parts:
        x = d * k
        assert x <= cur, ("group too big", n, d, parts)
        word = "group" if k == 1 else "groups"
        steps.append("Take away %s %s of %d: %d × %s = %s, and %s %s %s = %s." %
                     (f(k), word, d, d, f(k), f(x), f(cur), MINUS, f(x), f(cur - x)))
        cur -= x
    q, r = sum(parts), cur
    assert n == d * q + r and 0 <= r < d, ("wrong parts", n, d, parts, r)
    if len(parts) > 1:
        steps.append("Add the groups taken away: %s = %s." % (" + ".join(f(k) for k in parts), f(q)))
    if r == 0:
        steps.append("Nothing is left, so %s ÷ %d = %s." % (f(n), d, f(q)))
        steps.append("Check: %d × %s = %s." % (d, f(q), f(n)))
    else:
        steps.append("%s is left. It is less than %d, so no more groups of %d can be taken away." % (f(r), d, d))
        steps.append("So %s ÷ %d: quotient %s, remainder %s." % (f(n), d, f(q), f(r)))
        steps.append("Check: %s = %d × %s + %s." % (f(n), d, f(q), f(r)))
    return steps, q, r


def split(n, d, a, b, sign="+", comma=False):
    """Split n into a + b (or a − b), divide each part by d, put the answers together. Returns (steps, quotient)."""
    f = lambda x: fmt(x, comma)
    if sign == "+":
        assert a + b == n
        s0 = "Split %s into %s + %s: %s + %s = %s." % (f(n), f(a), f(b), f(a), f(b), f(n))
    else:
        assert a - b == n
        s0 = "Split %s as %s %s %s: %s %s %s = %s." % (f(n), f(a), MINUS, f(b), f(a), MINUS, f(b), f(n))
    assert a % d == 0 and b % d == 0
    x, y = a // d, b // d
    z = x + y if sign == "+" else x - y
    assert n == d * z
    steps = [s0,
             "%s ÷ %d = %s and %s ÷ %d = %s." % (f(a), d, f(x), f(b), d, f(y)),
             "Put the answers together: %s %s %s = %s." % (f(x), "+" if sign == "+" else MINUS, f(y), f(z)),
             "Check: %d × %s = %s." % (d, f(z), f(n))]
    return steps, z


def halve(n, times, comma=False):
    """Halve n `times` times. Returns (steps, result)."""
    f = lambda x: fmt(x, comma)
    cur, steps = n, []
    for _ in range(times):
        assert cur % 2 == 0
        steps.append("Half of %s is %s." % (f(cur), f(cur // 2)))
        cur //= 2
    d = 2 ** times
    assert n == d * cur
    steps.append("Check: %d × %s = %s." % (d, f(cur), f(n)))
    return steps, cur


def pv(n, d, comma=False, short=False):
    """Division by place value: share each place, regroup what is left into the next place.
    short=True writes one short line per place. Returns (steps, quotient, remainder, quotient_digits)."""
    f = lambda x: fmt(x, comma)
    digits = [int(c) for c in str(n)]
    m = len(digits)
    steps, qd, carry = [], [], 0
    for i, dig in enumerate(digits):
        p = m - 1 - i
        pname = _PLACES[p]
        if i == 0:
            v = dig
            lead = "Start with the %s." % unit(dig, pname)
        else:
            prev = _PLACES[p + 1]
            v = carry * 10 + dig
            if carry == 0:
                lead = "Nothing is left from the %s. Bring down the %s: %s to share." % (prev, unit(dig, pname), unit(v, pname))
            else:
                lead = "%s left, regrouped as %s; with the %s that makes %s to share." % (
                    unit(carry, prev).capitalize(), unit(10 * carry, pname), unit(dig, pname), unit(v, pname))
        q, r = divmod(v, d)
        if q == 0:
            share = "%s cannot be shared among %d equal parts, so each part gets 0 %s: write 0." % (unit(v, pname), d, pname)
        else:
            left = "nothing is left" if r == 0 else "%s left" % unit(r, pname)
            share = "Share %s among %d equal parts: %s each, because %d × %d = %d, and %s." % (unit(v, pname), d, unit(q, pname), d, q, d * q, left)
        if short:
            left = "nothing left" if r == 0 else "%s left" % unit(r, pname)
            steps.append("%s: %s to share among %d, %d each, %s." % (pname.capitalize(), unit(v, pname), d, q, left))
        else:
            steps.append(lead + " " + share)
        qd.append(q)
        carry = r
    Q = int("".join(str(x) for x in qd))
    assert n == d * Q + carry and carry < d, (n, d, Q, carry)
    ds = ", ".join(str(x) for x in qd)
    if carry == 0:
        steps.append("The quotient digits are %s, so %s ÷ %d = %s." % (ds, f(n), d, f(Q)))
        steps.append("Check: %d × %s = %s." % (d, f(Q), f(n)))
    else:
        steps.append("The quotient digits are %s, so the quotient is %s and the remainder is %d." % (ds, f(Q), carry))
        steps.append("Check: %s = %d × %s + %d." % (f(n), d, f(Q), carry))
    return steps, Q, carry, qd


def nqdr(n, d, comma=False):
    """The check line N = D × Q + R for any division. Returns (sentence, q, r)."""
    f = lambda x: fmt(x, comma)
    q, r = divmod(n, d)
    if r == 0:
        return "%s ÷ %d: quotient %s, remainder 0. Check: %d × %s = %s." % (f(n), d, f(q), d, f(q), f(n)), q, r
    return "%s ÷ %d: quotient %s, remainder %s. Check: %s = %d × %s + %s." % (f(n), d, f(q), f(r), f(n), d, f(q), f(r)), q, r
