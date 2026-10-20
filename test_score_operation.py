def calculateSum(score):
    return sum(score)

def calculateAverage(score):
    return sum(score) / len(score)  

print("===== TEST SCORE AVERAGE =====")
score_number = int(input("Enter number range of scores: "))

score_list = []

for i in range(score_number):
    score = float(input("Enter a score: "))
    score_list.append(score)

print(f"\nStudent scores: {score_list}")
print(f"The sum grade is: {calculateSum(score_list)}")
print(f"The average grade is: {calculateAverage(score_list)}\n")

print("John 3:16")
print("Sapagkat gayon na lamang ang pag-ibig ng Diyos sa sangkatauhan, kaya't ibinigay niya ang kanyang kaisa-isang Anak, upang ang sinumang sumampalataya sa kanya ay hindi mapahamak, kundi magkaroon ng buhay na walang hanggan.")