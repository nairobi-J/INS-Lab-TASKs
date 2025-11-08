import string
from collections import Counter

# English letter frequency (from your data)
ENGLISH_FREQ = {
    'a': 8.05, 'b': 1.67, 'c': 2.23, 'd': 5.10, 'e': 12.22, 'f': 2.14, 'g': 2.30,
    'h': 6.62, 'i': 6.28, 'j': 0.19, 'k': 0.95, 'l': 4.08, 'm': 2.33, 'n': 6.95,
    'o': 7.63, 'p': 1.66, 'q': 0.06, 'r': 5.29, 's': 6.02, 't': 9.67, 'u': 2.92,
    'v': 0.82, 'w': 2.60, 'x': 0.11, 'y': 2.04, 'z': 0.06
}

def frequency_analysis_decrypt(ciphertext):
    ciphertext_lower = ciphertext.lower()
    letters_only = [ch for ch in ciphertext_lower if ch in string.ascii_lowercase]
    
    letter_counts = Counter(letters_only)
    total_letters = len(letters_only)
    
    cipher_freq = {ch: (count / total_letters) * 100 for ch, count in letter_counts.items()}
    
    sorted_cipher_letters = sorted(cipher_freq.keys(), key=lambda x: cipher_freq[x], reverse=True)
    sorted_english_letters = sorted(ENGLISH_FREQ.keys(), key=lambda x: ENGLISH_FREQ[x], reverse=True)
    
    mapping = {}
    for i in range(min(len(sorted_cipher_letters), len(sorted_english_letters))):
        mapping[sorted_cipher_letters[i]] = sorted_english_letters[i]
    
    result = []
    for char in ciphertext:
        if char.lower() in mapping:
            decrypted_char = mapping[char.lower()]
            if char.isupper():
                result.append(decrypted_char.upper())
            else:
                result.append(decrypted_char)
        else:
            result.append(char)
    
    return ''.join(result)

cipher1 = "af p xpkcaqvnpk pfg, af ipqe qpri, gauuikifc tpw, ceiri udvk tiki afgarxifrphni cd eao--wvmd popkwn, hiqpvri du ear jvaql vfgikrcpfgafm du cei xkafqaxnir du xrwqedearcdkw pfg du ear aopmafpcasi xkdhafmr afcd fit pkipr. ac tpr qdoudkcafm cd lfdt cepc au pfwceafm epxxifig cd ringdf eaorinu hiudki cei opceiopcaqr du cei uaing qdvng hi qdoxnicinw tdklig dvc--pfg edt rndtnw ac xkdqiigig, pfg edt odvfcpafdvr cei dhrcpqnir--ceiki tdvng pc niprc kiopaf dfi mddg oafg cepc tdvng qdfcafvi cei kiripkqe"

cipher2 = "aceah toz puvg vcdl omj puvg yudqecov, omj loj auum klu thmjuv hs klu zlcvu shv zcbkg guovz, upuv zcmdu lcz vuwovroaeu jczoyyuovomdu omj qmubyudkuj vukqvm. klu vcdluz lu loj avhqnlk aodr svhw lcz kvopuez loj mht audhwu o ehdoe eunumj, omj ck toz yhyqeoveg auecupuj, tlokupuv klu hej sher wcnlk zog, klok klu lcee ok aon umj toz sqee hs kqmmuez zkqffuj tckl kvuozqvu. omj cs klok toz mhk umhqnl shv sowu, kluvu toz oezh lcz yvhehmnuj pcnhqv kh wovpue ok. kcwu thvu hm, aqk ck zuuwuj kh lopu eckkeu ussudk hm wv. aonncmz. ok mcmukg lu toz wqdl klu zowu oz ok scskg. ok mcmukg-mcmu klug aunom kh doee lcw tuee-yvuzuvpuj; aqk qmdlomnuj thqej lopu auum muovuv klu wovr. kluvu tuvu zhwu klok zlhhr klucv luojz omj klhqnlk klcz toz khh wqdl hs o nhhj klcmn; ck zuuwuj qmsocv klok CSE-478: Introduction to Computer Security Lab Lab-2 omghmu zlhqej yhzzuzz (oyyovumkeg) yuvyukqoe ghqkl oz tuee oz (vuyqkujeg) cmubloqzkcaeu tuoekl. ck tcee lopu kh au yocj shv, klug zocj. ck czm'k mokqvoe, omj kvhqaeu tcee dhwu hs ck! aqk zh sov kvhqaeu loj mhk dhwu; omj oz wv. aonncmz toz numuvhqz tckl lcz whmug, whzk yuhyeu tuvu tceecmn kh shvncpu lcw lcz hjjckcuz omj lcz nhhj shvkqmu. lu vuwocmuj hm pczckcmn kuvwz tckl lcz vueokcpuz (ubduyk, hs dhqvzu, klu zodrpceeu aonncmzuz), omj lu loj womg juphkuj ojwcvuvz owhmn klu lhaackz hs yhhv omj qmcwyhvkomk sowcecuz. aqk lu loj mh dehzu svcumjz, qmkce zhwu hs lcz ghqmnuv dhqzcmz aunom kh nvht qy. klu uejuzk hs kluzu, omj aceah'z sophqvcku, toz ghqmn svhjh aonncmz. tlum aceah toz mcmukg-mcmu lu ojhykuj svhjh oz lcz lucv, omj avhqnlk lcw kh ecpu ok aon umj; omj klu lhyuz hs klu zodrpceeu- aonncmzuz tuvu scmoeeg jozluj. aceah omj svhjh loyyumuj kh lopu klu zowu acvkljog, zuykuwauv 22mj. ghq loj aukkuv dhwu omj ecpu luvu, svhjh wg eoj, zocj aceah hmu jog; omj klum tu dom dueuavoku hqv acvkljog-yovkcuz dhwshvkoaeg khnukluv. ok klok kcwu svhjh toz zkcee cm lcz ktuumz, oz klu lhaackz doeeuj klu cvvuzyhmzcaeu ktumkcuz auktuum dlcejlhhj omj dhwcmn hs onu ok klcvkg-klvuu"

print("Cipher 1 Decrypted:")
print(frequency_analysis_decrypt(cipher1))
print("\n" + "="*80 + "\n")
print("Cipher 2 Decrypted:")
print(frequency_analysis_decrypt(cipher2))