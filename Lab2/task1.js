let cipher = "odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo"
// const k = 3;

for(let i = 1; i < 26; i++){
    const text = ceaserCipher(i, cipher);
    console.log("shift:", i, "text:", text );
}



function ceaserCipher(k, cipher){
    let text = '';
for(let i = 0; i < cipher.length; i++){
    
    // let s = (cipher[i]-k)%26;
    let s = cipher[i];
    let d = cipher.charCodeAt(i);
    let base = (d >= 65 && d <= 90) ? 65 : 97;
    let char = String.fromCharCode(((d - base - k + 26)%26) + base);
    text += char;
     
     //cipher[i] = s;
}
//console.log(text);
return text;
}



//console.log(text);

