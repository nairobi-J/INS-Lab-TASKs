
cipher2 = `aceah toz puvg vcdl omj puvg yudqecov, omj loj auum klu thmjuv hs klu zlcvu shv
zcbkg guovz, upuv zcmdu lcz vuwovroaeu jczoyyuovomdu omj qmubyudkuj vukqvm. klu
vcdluz lu loj avhqnlk aodr svhw lcz kvopuez loj mht audhwu o ehdoe eunumj, omj ck toz
yhyqeoveg auecupuj, tlokupuv klu hej sher wcnlk zog, klok klu lcee ok aon umj toz sqee hs
kqmmuez zkqssuj tckl kvuozqvu. omj cs klok toz mhk umhqnl shv sowu, kluvu toz oezh lcz
yvhehmnuj pcnhqv kh wovpue ok. kcwu thvu hm, aqk ck zuuwuj kh lopu eckkeu ussudk hm
wv. aonncmz. ok mcmukg lu toz wqdl klu zowu oz ok scskg. ok mcmukg-mcmu klug aunom kh
doee lcw tuee-yvuzuvpuj; aqk qmdlomnuj thqej lopu auum muovuv klu wovr. kluvu tuvu zhwu
klok zlhhr klucv luojz omj klhqnlk klcz toz khh wqdl hs o nhhj klcmn; ck zuuwuj qmsocv klok 
omghmu zlhqej yhzzuzz (oyyovumkeg) yuvyukqoe ghqkl oz tuee oz (vuyqkujeg)
cmubloqzkcaeu tuoekl. ck tcee lopu kh au yocj shv, klug zocj. ck czm'k mokqvoe, omj kvhqaeu
tcee dhwu hs ck! aqk zh sov kvhqaeu loj mhk dhwu; omj oz wv. aonncmz toz numuvhqz tckl
lcz whmug, whzk yuhyeu tuvu tceecmn kh shvncpu lcw lcz hjjckcuz omj lcz nhhj shvkqmu. lu

vuwocmuj hm pczckcmn kuvwz tckl lcz vueokcpuz (ubduyk, hs dhqvzu, klu zodrpceeu-
aonncmzuz), omj lu loj womg juphkuj ojwcvuvz owhmn klu lhaackz hs yhhv omj

qmcwyhvkomk sowcecuz. aqk lu loj mh dehzu svcumjz, qmkce zhwu hs lcz ghqmnuv dhqzcmz
aunom kh nvht qy. klu uejuzk hs kluzu, omj aceah'z sophqvcku, toz ghqmn svhjh aonncmz.
tlum aceah toz mcmukg-mcmu lu ojhykuj svhjh oz lcz lucv, omj avhqnlk lcw kh ecpu ok aon
umj; omj klu lhyuz hs klu zodrpceeu- aonncmzuz tuvu scmoeeg jozluj. aceah omj svhjh
loyyumuj kh lopu klu zowu acvkljog, zuykuwauv 22mj. ghq loj aukkuv dhwu omj ecpu luvu,
svhjh wg eoj, zocj aceah hmu jog; omj klum tu dom dueuavoku hqv acvkljog-yovkcuz
dhwshvkoaeg khnukluv. ok klok kcwu svhjh toz zkcee cm lcz ktuumz, oz klu lhaackz doeeuj klu
cvvuzyhmzcaeu ktumkcuz auktuum dlcejlhhj omj dhwcmn hs onu ok klcvkg-klvuu`

englishFrequency = 'etaonhisrdlcufmwgybpvkxjqz'

function breakSubstitutionCipher(cipher) {
   
    const frequency = {};
    for (let char of cipher.toLowerCase()) {
        if (char >= 'a' && char <= 'z') {
            frequency[char] = (frequency[char] || 0) + 1;
        }
    }
    const sortedFrequency = Object.entries(frequency).sort((a, b) => b[1] - a[1]);
    const commonLetters = sortedFrequency.map(entry => entry[0]);
    const updatedFrequency = 'etaoihsnrdlbufmgwcypvkxxqz'.split('');
    const mapping = {};
    for (let i = 0; i < commonLetters.length; i++) {
        mapping[commonLetters[i]] = updatedFrequency[i];
    }
    let decrypted = '';
    for (let char of cipher) {
        if (char >= 'a' && char <= 'z') {
            decrypted += mapping[char] || char;
        } else if (char >= 'A' && char <= 'Z') {
            const lowerChar = char.toLowerCase();
            decrypted += mapping[lowerChar] ? mapping[lowerChar].toUpperCase() : char;
        } else {
            decrypted += char;
        }
    }
    return decrypted;
}

const decryptedText = breakSubstitutionCipher(cipher2);
console.log("Decryption for Cipher 2: "+decryptedText);

/**
Decryption for Cipher 2: bilbo was very rich and very peculiar, and had been the wonder of the shire for
sixty years, ever since his remarkable disappearance and unexpected return. the
riches he had brought back from his travels had now become a local legend, and it was
popularly believed, whatever the old folk might say, that the hill at bag end was full of
tunnels stuffed with treasure. and if that was not enough for fame, there was also his
prolonged vigour to marvel at. time wore on, but it seemed to have little effect on
mr. baggins. at ninety he was much the same as at fifty. at ninety-nine they began to
call him well-preserved; but unchanged would have been nearer the mark. there were some
that shook their heads and thought this was too much of a good thing; it seemed unfair that
anyone should possess (apparently) perpetual youth as well as (reputedly)
inexhaustible wealth. it will have to be paid for, they said. it isn't natural, and trouble
will come of it! but so far trouble had not come; and as mr. baggins was generous with
his money, most people were willing to forgive him his oddities and his good fortune. he

remained on visiting terms with his relatives (except, of course, the sackville-
bagginses), and he had many devoted admirers among the hobbits of poor and

unimportant families. but he had no close friends, until some of his younger cousins
began to grow up. the eldest of these, and bilbo's favourite, was young frodo baggins.
when bilbo was ninety-nine he adopted frodo as his heir, and brought him to live at bag
end; and the hopes of the sackville- bagginses were finally dashed. bilbo and frodo
happened to have the same birthday, september 22nd. you had better come and live here,
frodo my lad, said bilbo one day; and then we can celebrate our birthday-parties
comfortably together. at that time frodo was still in his tweens, as the hobbits called the
irresponsible twenties between childhood and coming of age at thirty-three
 */