import sys
if len(sys.argv) > 1:
    scores = [int(x) for x in sys.argv[1:]]
else:
    scores = [50, 60, 70, 80, 90]   
total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)
print("\n--- LOCAL BRANCH OUTPUT ---")
print("Scores:", scores)
print("Total Score:", total)
print("Average Score:", average)
print("Maximum Score:", maximum)
print("Minimum Score:", minimum)
