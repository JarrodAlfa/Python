loop: int = 1
score: int = 0
number: int = int(input("Toets de tafel in die je wilt oefenen: "))
while loop < 11:
    print(f"Wat is {loop} x {number}")
    if int(input()) == loop * number:
        print("Goed")
        score += 1
        if loop == 11:
            break
        else: loop += 1
    else:
        print("Fout")
        score -= 1
print(f"Je hebt {score} punten gescored!!")

# while True:
#     try:
#         if input() != loop * number:
#             print("Fout")
#             pass
#         else:
#             if input() == loop * number:
#                 print("Goed")
#                 loop += 1
#                 break


