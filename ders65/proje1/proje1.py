import os 

def load_questions(filename):
    questions = []
    script_path = os.path.dirname(__file__)
    abs_path = os.path.join(script_path,filename)
    with open(abs_path, 'r', encoding='utf-8') as f:
        for line in f:
            if '|' in line:
                q, a = line.strip().split('|')
                questions.append((q, a))
    return questions

def run_quiz(questions):
    correct = 0
    for i, (q, a) in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q}")
        user_ans = input("Your answer: ").strip()
        if user_ans.lower() == a.lower():
            print("Correct!")
            correct += 1
        else:
            print(f"Wrong! Correct answer: {a}")
    total = len(questions)
    percent = (correct / total) * 100
    print(f"\nYou got {correct}/{total} correct. Success rate: {percent:.2f}%")
    print("Result:", "Passed ✅" if percent >= 60 else "Failed ❌")

if __name__ == "__main__":
    qs = load_questions("proje1.txt")
    print(qs)
    run_quiz(qs)
