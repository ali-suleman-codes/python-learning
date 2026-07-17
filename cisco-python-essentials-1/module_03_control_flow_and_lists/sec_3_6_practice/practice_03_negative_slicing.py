# Statement
# A football league stores the last six match scores.
# [2, 1, 3, 0, 4, 2]
# Print
# last three scores
# last four scores
# all scores except the last one

scores = [2, 1, 3, 0, 4, 2]

last_three_scores = scores[-3 : ]
last_four_scores = scores[-4 : ]
without_last_score = scores[ : -1]

print("Last three   :", last_three_scores)
print("Last four    :", last_four_scores)
print("Without last :", without_last_score)