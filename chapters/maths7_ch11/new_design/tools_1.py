# -*- coding: utf-8 -*-
"""Tool specs for module M1 (common factors and HCF)."""
from topics_common import T

TOOLS = {
    "tile_fitter": T(
        "tool_tile_fitter", "Tile Fitter: one minute free try", "simulation",
        "A square tile fits a room exactly only when its side divides both room sides; the largest such side needs the "
        "fewest tiles. The student finds this by trying sizes, not by being told.",
        "A 12 ft by 16 ft floor drawn on a grid; a slider sets the tile side from 1 ft to 16 ft; the floor fills with "
        "square tiles and shows gaps or overhang in red; a counter for tiles used; a one minute countdown ring; a list "
        "of sizes that fitted.",
        ["Slide the tile side and watch whether the floor fills with no gap and no overhang.",
         "Note every size that fits and the tile count it gives.",
         "Try to find the size that uses the fewest tiles before the minute ends.",
         "Press Done to claim a size, or let the minute run out; the tool then moves on by itself."],
        ["Room 12 ft by 16 ft: find every tile side that fits (1, 2 and 4).",
         "Find the fit that uses the fewest tiles (side 4 ft, 12 tiles).",
         "Compare 2 ft tiles (48 tiles) with 4 ft tiles (12 tiles).",
         "Check that a 3 ft tile fails (16 ft is not a multiple of 3).",
         "Check that a 6 ft or 8 ft tile fails on one side."],
        ["A size that fails shows exactly which side leaves a gap or overhang, with the left over length.",
         "A fitting size is kept in the list with its tile count.",
         "Finding the 4 ft tile inside the minute triggers a celebration; running out of time ends the tool quietly "
         "and the next video explains the answer."],
        "The minute ends or the student claims the largest fitting size; either way the tool moves on.",
        ["tileSide", "fits", "tileCount", "foundSizes", "secondsLeft", "claimed"],
        ["M_HCF_BIG", "M_COMMON_ONLY"],
        ["What must be true of the tile side for the 12 ft side to fill exactly?",
         "The side must go into 12 exactly and also into 16 exactly.",
         "Try 1, 2, 3 and 4 and see which leave no gap on both sides.",
         "Sizes 1, 2 and 4 fit; 4 ft is the largest, and it needs 12 tiles."]),

    "common_factor_lister": T(
        "tool_common_factor_lister", "Common Factor Lister", "manipulative",
        "The common factors of two numbers are the factors that appear in both lists; the greatest of them is the HCF, "
        "and it is also the side of the largest square that tiles the rectangle.",
        "Two number cards; for each a row of factor chips filled by tapping divisors; a middle strip where chips "
        "present in both rows glide together; an HCF slot; a rectangle with a square-side slider that shows the "
        "tiling.",
        ["Predict which numbers are common factors before listing.",
         "Tap candidate divisors for each number; wrong taps are shaken out with the remainder shown.",
         "Drag a chip into the common strip when it appears in both rows.",
         "Check the HCF against the biggest square that tiles the rectangle."],
        ["12 and 16 (HCF 4).", "18 and 24 (HCF 6).", "20 and 30 (HCF 10).", "21 and 28 (HCF 7).",
         "15 and 28 (HCF 1).", "36 and 48 (HCF 12)."],
        ["A missed factor is flagged with a divisibility check, for example 24 ÷ 8 = 3.",
         "A chip kept in the common strip that divides only one number is sent back with the failed division shown.",
         "The HCF slot lights up only when it is the greatest chip in the strip."],
        "All six pairs are done with the common strip and the HCF correct.",
        ["numA", "numB", "factorsA", "factorsB", "common", "hcf", "cardIndex"],
        ["M_COMMON_ONLY", "M_HCF_BIG"],
        ["Which numbers divide the first number exactly?",
         "Write the factors of both, then look for the numbers present in both rows.",
         "Check the biggest chip in the common strip against both numbers.",
         "Both factor lists are shown, the shared ones are highlighted and the greatest is the HCF; a new pair follows."]),

    "rice_bags": T(
        "tool_rice_bags", "Rice Bag Packer", "simulation",
        "A bag weight packs a farm's rice exactly only if it is a factor of the farm's weight; for both farms it must "
        "be a common factor, and the greatest one needs the fewest bags.",
        "Two sacks labelled with the weights from each farm; a bag-weight slider; bags appear and fill, with left over "
        "rice shown in red; a table of weights tried with bags used from each farm; a Reveal button.",
        ["Choose a bag weight and see whether both sacks pack with nothing left over.",
         "Record each weight that works and the number of bags from each farm.",
         "Compare totals and pick the weight that gives the fewest bags.",
         "Ask for a hint, or press Reveal after trying."],
        ["84 kg and 108 kg: which weights pack both exactly (1, 2, 3, 4, 6, 12) and which gives the fewest bags (12 kg, "
         "16 bags).",
         "60 kg and 90 kg (30 kg bags, 5 bags).", "48 kg and 72 kg (24 kg bags, 5 bags).",
         "36 kg and 45 kg (9 kg bags, 9 bags).", "40 kg and 56 kg (8 kg bags, 12 bags).",
         "50 kg and 75 kg (25 kg bags, 5 bags)."],
        ["A weight that leaves rice over shows the remainder, for example 84 ÷ 8 leaves 4 kg.",
         "A weight that works for one farm only is marked half correct with the other farm's remainder shown.",
         "After a correct pick the tool shows total bags beside the next smaller common factor to show why it is more."],
        "All six cards are solved with the weight and the bag count correct.",
        ["bagWeight", "bagsA", "bagsB", "total", "weightsTried", "cardIndex"],
        ["M_COMMON_ONLY", "M_HCF_BIG"],
        ["What must be true of a bag weight if the first sack packs with nothing left?",
         "List the weights that pack each sack, then keep the ones in both lists.",
         "Take the heaviest weight in both lists and count the bags.",
         "The common weights are listed, the greatest is chosen, and both bag counts are added; a new card follows."]),

    "jump_jackpot": T(
        "tool_jump_jackpot", "Jump Jackpot", "game",
        "A jump size lands on a number exactly when it is a factor of that number, so the longest jump landing on both "
        "treasure numbers is the HCF.",
        "A number line from 0 to 60 with Jumpy at 0 and two treasure chests; a jump-size picker; Jumpy hops and the "
        "landings are marked; a score counter and a table of jump sizes tried.",
        ["Pick a jump size and press Go to watch where Jumpy lands.",
         "See which treasures are collected.",
         "Search for the longest jump that collects both treasures.",
         "After finding it, compare it with the HCF of the two numbers."],
        ["Treasures on 14 and 30 (longest jump 2).", "Treasures on 7 and 11 (longest jump 1).",
         "Treasures on 30 and 50 (longest jump 10).", "Treasures on 28 and 42 (longest jump 14).",
         "Treasures on 24 and 36 (longest jump 12).", "Treasures on 45 and 60 (longest jump 15)."],
        ["A jump that skips a treasure shows the landing just before and after it.",
         "A jump that collects one chest is marked partly right and the missed chest is highlighted.",
         "On a correct answer the tool shows both numbers as multiples of the jump and names the HCF."],
        "All six treasure pairs are solved and each longest jump is matched with the HCF.",
        ["jump", "landings", "collected", "treasureA", "treasureB", "score", "cardIndex"],
        ["M_COMMON_ONLY", "M_HCF_BIG"],
        ["Which jump sizes land on the first treasure?",
         "A jump lands on a number if it is a factor of it. Find those for both.",
         "Take the longest jump that works for both numbers.",
         "Both lists of landing sizes are shown and the longest shared one is the answer; a new pair follows."]),

    "prime_sorter": T(
        "tool_prime_sorter", "Prime Sorter", "manipulative",
        "A number greater than 1 is prime if it has exactly two factors; counting the factors sorts every number into "
        "prime, composite, or neither, and an odd number is not automatically prime.",
        "A tray of number cards; two bins labelled Prime and Composite plus a small bin for Neither; a factor counter "
        "that fills as the student tests divisors; a Sieve grid from 1 to 100 that crosses out multiples.",
        ["Predict the bin before testing.",
         "Test divisors one by one to count the factors.",
         "Drop the card in a bin; the tool checks the factor count.",
         "Use the Sieve grid to cross out multiples and see which numbers remain."],
        ["1, 2, 3, 4, 5 (1 is neither).", "9, 15, 21, 25, 27 (odd but composite).", "11, 13, 17, 19, 23 (all prime).",
         "49, 51, 57, 91 (look prime, are not).", "37, 41, 43, 47 (prime).", "Find all primes from 1 to 30 on the grid."],
        ["A card in the wrong bin shows a factor pair that proves it, for example 91 = 7 × 13.",
         "Putting 1 in Prime shows it has only one factor.",
         "A correct drop shows the factor list that decided it."],
        "All six sets are sorted correctly and the primes up to 30 are marked on the grid.",
        ["card", "factorsFound", "bin", "sieveMarks", "cardIndex"],
        ["M_PRIME_ONE"],
        ["How many factors does the number have?",
         "A prime has exactly two factors, 1 and itself. Test small divisors in order.",
         "Try dividing by 2, 3, 5 and 7 and see if any goes in.",
         "The factor list is shown and decides the bin; a new set follows."]),

    "prime_splitter": T(
        "tool_prime_splitter", "Prime Splitter", "manipulative",
        "Splitting a composite number until only primes remain gives its prime factorisation; any route gives the same "
        "primes, and the division method does it compactly.",
        "A number card that splits into two branches in a factor tree; a second mode shows the division ladder with a "
        "vertical bar; the leaves are collected in a product line; a Check button multiplies the primes back.",
        ["Predict the primes before splitting.",
         "Split a composite into two factors; prime leaves turn green.",
         "Switch to the division ladder and divide by primes in order.",
         "Press Check to multiply the primes and compare with the number."],
        ["90 by two different trees (2 × 3 × 3 × 5).", "105 and 30 by division (3 × 5 × 7 and 2 × 3 × 5).",
         "1200 by division (2 × 2 × 2 × 2 × 3 × 5 × 5).", "72 by division (2 × 2 × 2 × 3 × 3).",
         "225 by a tree (3 × 3 × 5 × 5).", "13 (a prime is its own factorisation)."],
        ["A leaf that is still composite stays orange with a suggested split.",
         "The Check button shows the product of the leaves beside the number.",
         "Two different trees for the same number end with the same prime leaves side by side."],
        "All six numbers are split to primes and the product check matches.",
        ["number", "tree", "ladder", "primes", "productCheck", "cardIndex"],
        ["M_ORDER", "M_PRIME_ONE"],
        ["Is the number divisible by 2, 3 or 5?",
         "Divide by the smallest prime that goes in and carry the quotient down.",
         "Keep dividing until the number left is prime.",
         "The ladder is shown to the end with the primes collected and multiplied back; a new number follows."]),

    "factor_builder": T(
        "tool_factor_builder", "Factor Builder", "manipulative",
        "Every factor of a number is a subpart of its prime factorisation, so taking the primes one, two, three and "
        "more at a time lists every factor without missing any.",
        "The prime factorisation shown as tiles; the student selects a subset of tiles to form a factor; the product "
        "is shown and added to a growing factor list sorted in order; a counter shows the factor count and a Check "
        "button compares with division.",
        ["Predict how many factors there will be.",
         "Select one prime tile at a time and add each product to the list.",
         "Select two tiles, then three, and so on, skipping repeats.",
         "Check the list by dividing, and see the total count."],
        ["225 (9 factors).", "90 (12 factors).", "105 (8 factors).", "132 (12 factors).",
         "360 (24 factors).", "840 (32 factors)."],
        ["A repeated product is greyed with a note that it is already in the list.",
         "A missing factor is hinted by a gap in the sorted list.",
         "A product not dividing the number cannot occur, because tiles come from the factorisation."],
        "All six numbers have a complete factor list.",
        ["primeTiles", "selected", "factorList", "count", "cardIndex"],
        ["M_ORDER"],
        ["What are the primes in the factorisation?",
         "Combine the primes one at a time, then two, then three.",
         "Skip a product that is already in the list and finish with 1.",
         "The full list is shown with the combinations that make each factor; a new number follows."]),

    "hcf_subparts": T(
        "tool_hcf_subparts", "Common Subparts Matcher", "manipulative",
        "Common factors are the subparts that appear in both prime factorisations; the largest common subpart is the HCF, "
        "and if no prime is shared, the only common factor is 1.",
        "Two prime factorisation strips of tiles; matching tiles join with a thread; a result strip lists the common "
        "subparts and their products; an HCF slot.",
        ["Predict which primes will match.",
         "Drag tiles from one strip against the other to pair equal primes.",
         "Read off every common subpart and the common factors.",
         "Name the HCF as the largest product."],
        ["45 and 75 (HCF 15).", "112 and 84 (HCF 28).", "96 and 275 (HCF 1).", "50 and 60 (HCF 10).",
         "140 and 275 (HCF 5).", "370 and 592 (HCF 74)."],
        ["An unmatched tile stays loose, which shows it is not shared.",
         "If nothing matches, the tool states that 1 is the only common factor and so the HCF.",
         "The HCF slot checks the product of all joined tiles."],
        "All six pairs are matched and the common factors and HCF are correct.",
        ["stripA", "stripB", "matches", "commonFactors", "hcf", "cardIndex"],
        ["M_COMMON_ONLY", "M_COPRIME_ONE_FACTOR"],
        ["Which primes appear in both strips?",
         "Pair each tile with an equal tile; unmatched tiles are not shared.",
         "Multiply the joined tiles to get the HCF.",
         "The pairs are drawn with threads and the HCF is the product of the joined tiles; a new pair follows."]),

    "hcf_min_count": T(
        "tool_hcf_min_count", "Minimum Count Table", "manipulative",
        "The HCF takes each prime shared by all the numbers the minimum number of times it occurs, so the smaller count "
        "decides; this works for two numbers or more.",
        "A table with a row per prime and a column per number showing how many times it occurs; a Min column the "
        "student fills; a product line that builds the HCF from the Min column; an extra number can be added.",
        ["Predict the count of each prime in the HCF.",
         "Fill the Min column for each prime in the table.",
         "Cross out any prime missing in one number.",
         "Multiply the chosen primes to get the HCF."],
        ["30 and 72 (HCF 6).", "225 and 750 (HCF 75).", "24 and 180 (HCF 12).", "42, 75 and 24 (HCF 3).",
         "400 and 2500 (HCF 100).", "36, 60 and 84 (HCF 12)."],
        ["A count taken from the larger number is flagged and the smaller count is highlighted.",
         "A prime missing from any number is crossed out automatically with a short reason.",
         "The final product is checked by dividing each number by the HCF."],
        "All six cards are solved with the correct Min column and HCF.",
        ["primes", "counts", "minColumn", "hcf", "cardIndex"],
        ["M_MIN_MAX", "M_COPRIME_ONE_FACTOR"],
        ["Which primes occur in every number?",
         "For each shared prime, choose the smaller count.",
         "Multiply the primes with their minimum counts.",
         "The table shows the minimum counts and the product; a new card follows."]),
}
