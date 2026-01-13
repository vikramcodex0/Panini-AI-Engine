from gtts import gTTS
import os

# Panini's Master Database (The 14 Shiva Sutras)
# Inhe lists mein divide kar rahe hain

shiva_sutras = [
    "aiuṇ",      # 1. Vowels
    "ṛḷk",        # 2. More Vowels
    "eoṅ",        # 3. Diphthongs
    "aiauc",      # 4. Diphthongs
    "hayavaraṭ",  # 5. Semi-vowels
    "laṇ"         # 6. Nasal
]

print("--- Panini Data Structures: Phase 1 ---")
for i, sutra in enumerate(shiva_sutras, 1):
    print(f"Sutra {i}: {sutra}")

# Challenge: In 14 lines se hi pura 'Pratyahara' (Compression) banta hai.
# Panini's Search Logic: Pratyahara
# Agar humein pehle 4 sutras ke saare vowels chahiye, toh use 'Ac' kehte hain

# 1. Database: Shiva Sutras ki list hona zaroori hai
shiva_sutras = [
    "aiuṇ",      # 1. Vowels
    "ṛḷk",       # 2. More Vowels
    "eoṅ",       # 3. Diphthongs
    "aiauc",     # 4. Diphthongs
    "hayavaraṭ", # 5. Semi-vowels
    "laṇ"        # 6. Nasal
]

print("--- Panini Data Structures: Phase 1 ---")
for i, sutra in enumerate(shiva_sutras, 1):
    print(f"Sutra {i}: {sutra}")

# 2. Search Logic: 'Ac' Pratyahara (Vowels)
vowels_list = []
# Hum pehle 4 sutras se vowels nikal rahe hain
for sutra in shiva_sutras[:4]: 
    # [:-1] se hum aakhri 'marker' (ṇ, k, ṅ, c) ko hata rahe hain
    vowels_list.append(sutra[:-1]) 

pure_vowels = "".join(vowels_list)

print("\n--- Panini Logic: The 'Ac' Pratyahara ---")
print(f"Compressed Code: 'Ac'")
print(f"Decompressed Vowels: {pure_vowels}")

# Panini Search Engine - Phase 2
def get_panini_range(start_sutra_idx, end_marker):
    result_chars = ""
    
    # 1. Loop chalao jahan se shuru karna hai
    for sutra in shiva_sutras[start_sutra_idx:]:
        # Agar iss sutra mein wo 'Stop Sign' mil gaya
        if end_marker in sutra:
            # Marker tak ke akshar lo aur ruk jao
            result_chars += sutra.split(end_marker)[0]
            break
        else:
            # Marker nahi mila toh poora sutra (minus last marker) lo
            result_chars += sutra[:-1]
            
    return result_chars

# Test: 'Hal' (Consonants ka ek hissa) nikalte hain
# Sutra 5 (Index 4) se shuru karke Sutra 6 tak
print("\n--- Custom Range Search ---")
consonants_sample = get_panini_range(4, "ṇ") # 'Ha' se 'Laṇ' tak
print(f"Logic: Sutra 5 to 'ṇ' marker")
print(f"Result: {consonants_sample}")

# Audio banane ka kaam yahan hoga
awaaz = gTTS(text="ai u n. ri li k. e o n. ai au c. hayavara", lang='hi')
awaaz.save("panini_shakti.mp3")
print("\n--- Audio File Ban Gayi Hai! ---")

# --- Phase 4: The Panini Sandhi Engine ---

def apply_guna_sandhi(first_word_end, second_word_start):
    # Rule: Agar word 'a' par khatam ho aur naya word 'i' se shuru ho
    # Toh 'a + i' milkar 'e' ban jata hai. (Sutra: Ad Guna)
    
    if first_word_end == "a" and second_word_start == "i":
        return "e"
    else:
        return "Logic under construction"

# Example: Maha + Indra
part1 = "Maha"
part2 = "Indra"

# Part 1 ka aakhri akshar aur Part 2 ka pehla akshar check karo
result_vowel = apply_guna_sandhi(part1[-1], part2[0].lower())

final_word = part1[:-1] + result_vowel + part2[1:]

print("\n--- Panini Sandhi Result ---")
print(f"{part1} + {part2} = {final_word}")

# Ab is result ko bhi computer se bulwaate hain
final_speech = gTTS(text=f"Maha plus Indra equals {final_word}", lang='hi')
final_speech.save("sandhi_result.mp3")
print("Nayi audio file 'sandhi_result.mp3' ban gayi hai!")

# --- Universal Sandhi Engine ---

def smart_sandhi(word1, word2):
    last_char = word1[-1].lower()
    first_char = word2[0].lower()
    
    # Rule 1: Guna Sandhi (a + i = e)
    if last_char == "a" and first_char == "i":
        return word1[:-1] + "e" + word2[1:]
    
    # Rule 2: Dirgha Sandhi (a + a = aa)
    elif last_char == "a" and first_char == "a":
        return word1[:-1] + "aa" + word2[1:]
    
    # Rule 3: Vriddhi Sandhi (a + e = ai)
    elif last_char == "a" and first_char == "e":
        return word1[:-1] + "ai" + word2[1:]
        
    else:
        return word1 + word2 # Simple join if no rule matches

# Multiple Tests ek saath
tests = [("Maha", "Indra"), ("Hima", "Alaya"), ("Maha", "Eshwar")]

print("\n--- Testing Universal Sandhi Engine ---")
for w1, w2 in tests:
    result = smart_sandhi(w1, w2)
    print(f"{w1} + {w2} = {result}")

    # --- Phase 5: The Panini Pratyahara Decoder ---

def decode_panini_code(code):
    # 'Ac' -> shuru karo 'a' se, khatam karo 'c' marker par
    start_char = code[0]
    end_marker = code[1]
    
    decoded_result = ""
    found_start = False
    
    for sutra in shiva_sutras:
        if start_char in sutra:
            found_start = True
            
        if found_start:
            if end_marker in sutra:
                # Marker mil gaya, yahan tak ka data lo aur ruko
                decoded_result += sutra.split(end_marker)[0]
                break
            else:
                # Beech wale saare akshar lo (aakhri marker chhod kar)
                decoded_result += sutra[:-1]
                
    return decoded_result

# Testing our Decoder
print("\n--- Panini AI Decoder Interface ---")
codes_to_test = ["ac", "hal"] # 'ac' = vowels, 'hal' = consonants
for c in codes_to_test:
    print(f"Decoding '{c}': {decode_panini_code(c)}")

    # --- Phase 6: The Panini AI Interactive Menu ---

def main_menu():
    print("\n========= PANINI AI SYSTEM =========")
    print("1. Sanskrit Alphabet (Shiva Sutras)")
    print("2. Word Joiner (Sandhi Engine)")
    print("3. Decoder (Pratyahara Logic)")
    print("4. Play Panini Audio")
    print("====================================")
    
    choice = input("Aap kya check karna chahte ho? (1-4): ")
    
    if choice == '1':
        for s in shiva_sutras: print(s)
    elif choice == '2':
        w1 = input("Pehla shabd (e.g. Maha): ")
        w2 = input("Dusra shabd (e.g. Indra): ")
        print(f"Result: {smart_sandhi(w1, w2)}")
    elif choice == '3':
        code = input("Decoder code daalo (e.g. ac): ")
        print(f"Decoded: {decode_panini_code(code)}")
    elif choice == '4':
        os.system("start panini_shakti.mp3")
    else:
        print("Sahi option chuno bhai!")

def smart_sandhi(word1, word2):
    last_char = word1[-1].lower()
    first_char = word2[0].lower()
    
    # Rule 1: Guna Sandhi (a + i = e)
    if last_char == "a" and first_char == "i":
        result = word1[:-1] + "e" + word2[1:]
        print("\n[AI Explain]: Yahan Panini ka Sutra 6.1.87 (Ad Guna) apply hua.")
        print(f"Logic: '{last_char}' + '{first_char}' milkar 'e' ban gaye.")
        return result
    
    # Rule 2: Dirgha Sandhi (a + a = aa)
    elif last_char == "a" and first_char == "a":
        result = word1[:-1] + "aa" + word2[1:]
        print("\n[AI Explain]: Yahan Panini ka Sutra 6.1.101 (Akah Savarne Dirghah) apply hua.")
        print(f"Logic: Same vowels milkar bade '{result[-2:]}' ban gaye.")
        return result
        # Rule 3: Yan Sandhi (i + any other vowel = y)
    # Sutra: Iko Yanachi (6.1.77)
    elif last_char == "i" and first_char != "i":
        result = word1[:-1] + "y" + word2
        print("\n[AI Explain]: Yahan Panini ka Sutra 6.1.77 (Iko Yanachi) apply hua.")
        print(f"Logic: '{last_char}' badal kar 'y' ban gaya kyunki aage alag vowel '{first_char}' hai.")
        return result
    return word1 + word2
# Menu ko start karne ke liye
# Isse program tab tak chalega jab tak aap band nahi karte
while True:
    main_menu()  # Ye thoda aage hai
    input("\nAgla kaam karne ke liye 'Enter' dabao...") # Ye bhi aage hai
