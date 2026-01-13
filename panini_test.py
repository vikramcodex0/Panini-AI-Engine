# Panini AI Engine - Logic Center v2.0
# Sabhi rules (English + Devanagari) yahan hain

def yan_sandhi(word1, word2):
    """Sutra: Iko Yanachi (6.1.77)"""
    # Devanagari Handling (i/ī -> y)
    if word1.endswith(('इ', 'ई', 'ि', 'ी')) and not word2.startswith(('इ', 'ई', 'ि', 'ी')):
        return word1[:-1] + 'य्' + word2
    
    # English Handling
    if word1.lower().endswith('i') and not word2.lower().startswith('i'):
        return word1[:-1] + "y" + word2
    
    return None

def guna_sandhi(word1, word2):
    """Sutra: Ad Guna (6.1.87)"""
    # 1. Devanagari Rules (a/ā + i/ī = e)
    # Check for 'a', 'ā' or the 'ā' matra (ा)
    if word1.endswith(('अ', 'आ', 'ा')) and word2.startswith(('इ', 'ई', 'ि', 'ी')):
        return word1[:-1] + 'ए' + word2[1:]
    
    # Rule 2: a/ā + u/ū = o
    if word1.endswith(('अ', 'आ', 'ा')) and word2.startswith(('उ', 'ऊ', 'ु', 'ू')):
        return word1[:-1] + 'ओ' + word2[1:]
    
    # Rule 3: a/ā + ṛ = ar
    if word1.endswith(('अ', 'आ', 'ा')) and word2.startswith('ऋ'):
        return word1[:-1] + 'अर्' + word2[1:]

    # 2. English Logic Rules
    w1_low = word1.lower()
    w2_low = word2.lower()
    if w1_low.endswith('a') and w2_low.startswith('i'):
        return word1[:-1] + "e" + word2[1:]
    if w1_low.endswith('a') and w2_low.startswith('u'):
        return word1[:-1] + "o" + word2[1:]
    
    return None

def dirgha_sandhi(word1, word2):
    """Sutra: Akah Savarne Dirghah (6.1.101)"""
    # a + a = ā
    if word1.endswith(('अ', 'आ', 'ा')) and word2.startswith(('अ', 'आ', 'ा')):
        return word1[:-1] + 'आ' + word2[1:]
    
    # English a + a
    if word1.lower().endswith('a') and word2.lower().startswith('a'):
        return word1[:-1] + "aa" + word2[1:]
        
    return None