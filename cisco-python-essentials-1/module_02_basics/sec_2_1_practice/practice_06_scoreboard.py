"""Practice 6: The Tabbed Scoreboard
The Concepts: The tab escape sequence (\t) for perfect column alignment, and the sep= keyword.

The Goal: Create a clean, aligned scoreboard table using tabs so that all columns line up perfectly, regardless of the word lengths.

Expected output : """
# RANK	PLAYER		SCORE
# 1.	AliSuleman	9900
# 2.	CPU_Bot		850

print("RANK", "PLAYER\t", "SCORE", sep = "\t")
print("1.", "AliSuleman", "9900", sep = "\t")
print("2.", "CPU_Bot\t", "850", sep = "\t")
